#!/usr/bin/env python3
"""export_audit.py — is a structure field actually opened anywhere in a proof? (version 2)

Reads a lean4export (format 3.1.0) NDJSON stream in ONE pass, without building anything, and reports
for every field of the structures you name:

    OPENED IN PROOF   the field is pulled out inside the proof/definition body of some declaration
    MENTIONED ONLY    the field appears only in statements (declaration types), never in a body
    UNOPENED          the field never appears

For opened fields it lists every declaration that opens it (the evidence) and how each one uses it:

    re-wrapped        the field goes straight into a constructor (packed into another structure)
    passed on         the field is handed to a function or theorem (follow that one by hand)
    used directly     the field is returned or bound as it is

It also reports declarations that take the whole structure apart (`rec`/`casesOn`/...), which unpacks every
field at once; in export mode it does NOT say which unpacked fields that branch then uses.

The structure's own auto-generated declarations (its field accessors, `casesOn`, `mk.injEq`, ...) never count
as openings.

Usage
    zstd -dc --long=30 solution.ndjson.zst | python export_audit.py \
        --struct GlobalTheory.Mem.Top.Bl.OAt \
        --true-pred GlobalTheory.Mem.Top.Bl.anyGeometry \
        --expect GlobalTheory.Mem.Top.Bl.OAt.lam=OPENED \
        --out audit.json --md audit.md

    python export_audit.py --self-test          # seconds; runs before any real use
    python export_audit.py --write-fixture f.ndjson [--use-c]

Controls (a "never opened" means nothing unless the tool is shown to see an opening):
  * --self-test runs a hand-built export with known answers, a positive control (a use of field `c` must
    flip it to OPENED) and a negative control (a deliberately wrong --expect must make the run VOID).
  * --expect FIELD=LABEL on a real run: if the tool does not report LABEL for FIELD, the whole run is VOID
    (exit code 2). Use a field you know is opened, e.g. OAt.lam in the RH export.

--true-pred NAME checks, from the export itself, that NAME's body is `fun ... => True`, and lists where it
is used. A proof of `True` carries no information, so a field whose type is that predicate cannot pass any
on. (Checking that every instance of the structure really uses NAME is NOT done in this version.)

Memory: one byte per expression id for the "headed by a constructor" flag (about 1 GB for the RH export);
--no-transport skips it and the re-wrapped/passed-on split. Everything else is sparse.

Written by Claude (Opus, chat) for Timothy Wesley Stone, 25 Nov 2026, extending export_scan.py.
"""
import sys, re, json, time, argparse
from array import array

TRUE_NAME = "True"
ELIM_SUFFIXES = {"rec", "recOn", "casesOn", "below", "brecOn", "binductionOn", "ibelow", "ndrec", "ndrecOn"}

re_const = re.compile(rb'^\{"const":\{"name":(\d+),"us":\[[^\]]*\]\},"ie":(\d+)\}')
re_app = re.compile(rb'^\{"app":\{"arg":(\d+),"fn":(\d+)\},"ie":(\d+)\}')
re_forall = re.compile(rb'^\{"forallE":\{"binderInfo":"[a-zA-Z]+","body":(\d+),"name":\d+,"type":(\d+)\},"ie":(\d+)\}')
re_lam = re.compile(rb'^\{"ie":(\d+),"lam":\{"binderInfo":"[a-zA-Z]+","body":(\d+),"name":\d+,"type":(\d+)\}\}')
re_let = re.compile(rb'^\{"ie":(\d+),"letE":\{"body":(\d+),"name":\d+,"nondep":(?:true|false),"type":(\d+),"value":(\d+)\}\}')
re_proj = re.compile(rb'^\{"ie":(\d+),"proj":\{"idx":(\d+),"struct":(\d+),"typeName":(\d+)\}\}')
CHILD_KEYS = ("arg", "fn", "body", "type", "value", "struct", "expr")


class Audit:
    def __init__(self, structs, true_preds, transport=True, progress=50_000_000, log=sys.stderr):
        self.structs = list(structs)
        self.true_preds = list(true_preds)
        self.transport = transport
        self.progress = progress
        self.log = log
        targets = set(self.structs) | set(self.true_preds) | {TRUE_NAME}
        self.prefixes = set()
        for t in targets:
            parts = t.split(".")
            for k in range(1, len(parts) + 1):
                self.prefixes.add(".".join(parts[:k]))
        # name table (all names; 4+4 bytes each) and tracked full names (only target prefixes)
        self.parent = array("I")
        self.strid = array("I")
        self.strings = [""]
        self.strmap = {"": 0}
        self.tracked = {}          # name id -> full name, only for prefixes of targets
        self.struct_id = {}        # struct full name -> name id
        self.struct_of = {}        # name id -> struct full name
        self.child_of_struct = {}  # name id -> (struct, component) for direct children of a target struct
        self.true_pred_id = {}     # name id -> full name
        self.true_id = None
        # bits
        self.bits = {}
        self.bit_key = {}
        # sparse expression state
        self.mark = {}             # expr id -> mask
        self.occ = {}              # expr id -> field key, for accessor-headed spines and projections
        self.projtel = {}          # expr id -> field key, for `fun .. => proj S i _` telescopes
        self.truetel = set()       # expr ids that are `True` or `fun .. => True`
        self.ch = bytearray()      # expr id -> 1 if headed by a constructor
        # declaration-level facts
        self.ctor_names = set()
        self.accessor = {}         # name id -> field key
        self.field_name = {}       # field key -> field name
        self.nfields = {}          # struct -> number of fields
        self.elim_name = {}        # name id -> struct
        self.true_verified = {}    # true-pred full name -> bool
        self.hits = []             # (name id, kind, type mask, value mask, own)
        self.lines = 0
        self.decls = 0
        self.by_kind = {}
        self.fallback = 0

    # ---- helpers -------------------------------------------------------------------------------
    def bit(self, key):
        b = self.bits.get(key)
        if b is None:
            b = 1 << len(self.bits)
            self.bits[key] = b
            self.bit_key[b] = key
        return b

    def ensure_name(self, n):
        if n >= len(self.parent):
            grow = max(n + 1 - len(self.parent), 1_000_000)
            self.parent.extend(array("I", [0]) * grow)
            self.strid.extend(array("I", [0]) * grow)

    def ensure_ch(self, ie):
        if ie >= len(self.ch):
            self.ch.extend(bytes(max(ie + 1 - len(self.ch), 1 << 24)))

    def fullname(self, n):
        out = []
        while n:
            s = self.strings[self.strid[n]]
            out.append(s if s else "#")
            n = self.parent[n]
        return ".".join(reversed(out))

    def is_own(self, n):
        """true if a target structure is a proper ancestor of name n (its auto-generated declarations)"""
        n = self.parent[n] if n < len(self.parent) else 0
        while n:
            if n in self.struct_of:
                return True
            n = self.parent[n]
        return False

    def mask_of(self, ids):
        g = self.mark.get
        m = 0
        for i in ids:
            m |= g(i, 0)
        return m

    # ---- names ---------------------------------------------------------------------------------
    def on_name(self, j):
        n = j["in"]
        self.ensure_name(n)
        if "str" in j:
            p = j["str"]["pre"]
            s = j["str"]["str"]
            k = self.strmap.get(s)
            if k is None:
                k = len(self.strings)
                self.strings.append(s)
                self.strmap[s] = k
            self.parent[n] = p
            self.strid[n] = k
            pf = "" if p == 0 else self.tracked.get(p)
            if pf is not None:
                full = s if p == 0 else pf + "." + s
                if full in self.prefixes:
                    self.tracked[n] = full
                    if full in self.structs:
                        self.struct_id[full] = n
                        self.struct_of[n] = full
                    if full in self.true_preds:
                        self.true_pred_id[n] = full
                    if full == TRUE_NAME:
                        self.true_id = n
            st = self.struct_of.get(p)
            if st is not None:
                self.child_of_struct[n] = (st, s)
                if s in ELIM_SUFFIXES:
                    self.elim_name[n] = st
        else:
            self.parent[n] = j["num"]["pre"]
            self.strid[n] = 0

    # ---- main loop -----------------------------------------------------------------------------
    def run(self, stream):
        t0 = time.time()
        mark = self.mark
        mget = mark.get
        occ = self.occ
        oget = occ.get
        transport = self.transport
        ch = self.ch
        for raw in stream:
            self.lines += 1
            if self.progress and self.lines % self.progress == 0:
                print(f"{self.lines/1e6:.0f}M lines, {time.time()-t0:.0f}s, marks {len(mark):,}, "
                      f"decls {self.decls:,}", file=self.log, flush=True)
            c1 = raw[:6]
            if c1 == b'{"in":':
                self.on_name(json.loads(raw))
                continue
            if c1 == b'{"il":':
                continue
            if c1 == b'{"app"':
                m = re_app.match(raw)
                if m:
                    a = int(m.group(1)); f = int(m.group(2)); ie = int(m.group(3))
                    mm = mget(a, 0) | mget(f, 0)
                    if transport:
                        if ie >= len(ch):
                            self.ensure_ch(ie)
                        if ch[f]:
                            ch[ie] = 1
                    k = oget(f)
                    if k is not None:
                        occ[ie] = k            # the accessor spine continues
                    ka = oget(a)
                    if ka is not None:
                        if transport:
                            mm |= self.bit(("W", ka)) if ch[f] else self.bit(("O", ka))
                        else:
                            mm |= self.bit(("O", ka))
                    if mm:
                        mark[ie] = mm
                    continue
            if c1 == b'{"cons':
                m = re_const.match(raw)
                if m:
                    nid = int(m.group(1)); ie = int(m.group(2))
                    mm = 0
                    k = self.accessor.get(nid)
                    if k is not None:
                        mm |= self.bit(("F", k))
                        occ[ie] = k
                    st = self.elim_name.get(nid)
                    if st is not None:
                        mm |= self.bit(("E", st))
                    tp = self.true_pred_id.get(nid)
                    if tp is not None:
                        mm |= self.bit(("T", tp))
                    if nid == self.true_id:
                        self.truetel.add(ie)
                    if transport and nid in self.ctor_names:
                        self.ensure_ch(ie)
                        self.ch[ie] = 1
                    if mm:
                        mark[ie] = mm
                    continue
            if c1 == b'{"fora':
                m = re_forall.match(raw)
                if m:
                    mm = mget(int(m.group(1)), 0) | mget(int(m.group(2)), 0)
                    if mm:
                        mark[int(m.group(3))] = mm
                    continue
            if c1 == b'{"bvar':
                continue
            if c1 == b'{"ie":':
                head = raw[:48]
                if b'"sort"' in head:
                    continue
                if b'"lam"' in head:
                    m = re_lam.match(raw)
                    if m:
                        ie = int(m.group(1)); body = int(m.group(2)); ty = int(m.group(3))
                        mm = mget(body, 0) | mget(ty, 0)
                        if mm:
                            mark[ie] = mm
                        pk = self.projtel.get(body)
                        if pk is not None:
                            self.projtel[ie] = pk
                        if body in self.truetel:
                            self.truetel.add(ie)
                        continue
                if b'"proj"' in head:
                    m = re_proj.match(raw)
                    if m:
                        ie = int(m.group(1)); idx = int(m.group(2)); sx = int(m.group(3)); tn = int(m.group(4))
                        mm = mget(sx, 0)
                        st = self.struct_of.get(tn)
                        if st is not None:
                            key = (st, idx)
                            mm |= self.bit(("F", key))
                            occ[ie] = key
                            self.projtel[ie] = key
                        if mm:
                            mark[ie] = mm
                        continue
                if b'"letE"' in head:
                    m = re_let.match(raw)
                    if m:
                        mm = self.mask_of((int(m.group(2)), int(m.group(3)), int(m.group(4))))
                        if mm:
                            mark[int(m.group(1))] = mm
                        continue
                # lit, mdata, fvar, mvar, or an unexpected spelling: generic path
                self.fallback += 1
                j = json.loads(raw)
                ids = []
                for v in j.values():
                    if isinstance(v, dict):
                        for k2 in CHILD_KEYS:
                            if isinstance(v.get(k2), int):
                                ids.append(v[k2])
                mm = self.mask_of(ids)
                if mm:
                    mark[j["ie"]] = mm
                continue
            if c1 == b'{"meta':
                continue
            if c1 in (b'{"app"', b'{"cons', b'{"fora'):
                # the fast pattern did not match (unexpected key order): generic path
                self.fallback += 1
                self.generic_expr(json.loads(raw))
                continue
            self.on_decl(json.loads(raw))
        self.seconds = time.time() - t0
        return self

    def generic_expr(self, j):
        ie = j["ie"]
        if "app" in j:
            ids = [j["app"]["fn"], j["app"]["arg"]]
        elif "forallE" in j:
            ids = [j["forallE"]["body"], j["forallE"]["type"]]
        elif "const" in j:
            ids = []
        else:
            ids = [v for k, v in j.items() if isinstance(v, int) and k != "ie"]
        mm = self.mask_of(ids)
        if mm:
            self.mark[ie] = mm

    # ---- declarations --------------------------------------------------------------------------
    def on_decl(self, d):
        kind = next(iter(d))
        body = d[kind]
        self.decls += 1
        self.by_kind[kind] = self.by_kind.get(kind, 0) + 1
        if kind == "inductive":
            for c in body.get("ctors", []):
                self.ctor_names.add(c["name"])
            types = body.get("types", [])
            nid = types[0]["name"] if types else 0
            st = self.struct_of.get(nid)
            if st is not None and body.get("ctors"):
                self.nfields[st] = body["ctors"][0].get("numFields")
            troots = [t["type"] for t in types] + [c["type"] for c in body.get("ctors", [])] + \
                     [r["type"] for r in body.get("recs", [])]
            vroots = [ru["rhs"] for r in body.get("recs", []) for ru in r.get("rules", [])]
        else:
            nid = body.get("name", 0)
            troots = [body["type"]] if "type" in body else []
            vroots = [body["value"]] if "value" in body else []
            if kind in ("def", "thm", "opaque") and vroots:
                cs = self.child_of_struct.get(nid)
                pk = self.projtel.get(vroots[0])
                if cs is not None and pk is not None and pk[0] == cs[0]:
                    self.accessor[nid] = pk
                    self.field_name[pk] = cs[1]
                if nid in self.true_pred_id:
                    self.true_verified[self.true_pred_id[nid]] = vroots[0] in self.truetel
        tm = self.mask_of(troots)
        vm = self.mask_of(vroots)
        if tm or vm:
            self.hits.append((nid, kind, tm, vm, self.is_own(nid) or nid in self.struct_of))

    # ---- report --------------------------------------------------------------------------------
    def report(self):
        fields = {}
        for st in self.structs:
            n = self.nfields.get(st)
            idxs = set(range(n)) if isinstance(n, int) else set()
            idxs |= {k[1] for k in self.field_name if k[0] == st}
            for i in sorted(idxs):
                fields[(st, i)] = self.field_name.get((st, i), f"#{i}")
        res = {"lines": self.lines, "seconds": round(getattr(self, "seconds", 0), 1),
               "declarations": self.decls, "by_kind": self.by_kind, "fallback_lines": self.fallback,
               "transport_split": self.transport, "structs": {}, "true_preds": {}}
        for st in self.structs:
            sres = {"found": st in self.struct_id, "fields_declared": self.nfields.get(st),
                    "accessors_found": sum(1 for k in self.field_name if k[0] == st),
                    "fields": {}, "taken_apart_in": []}
            eb = self.bits.get(("E", st), 0)
            for (nid, kind, tm, vm, own) in self.hits:
                if eb and (vm & eb) and not own:
                    sres["taken_apart_in"].append(self.fullname(nid))
            for (s2, i), fname in fields.items():
                if s2 != st:
                    continue
                key = (st, i)
                fb = self.bits.get(("F", key), 0)
                wb = self.bits.get(("W", key), 0)
                ob = self.bits.get(("O", key), 0)
                opened, mentioned = [], []
                for (nid, kind, tm, vm, own) in self.hits:
                    if own or not fb:
                        continue
                    if vm & fb:
                        if ob and (vm & ob):
                            how = "passed on"
                        elif wb and (vm & wb):
                            how = "re-wrapped"
                        else:
                            how = "used directly"
                        opened.append({"decl": self.fullname(nid), "kind": kind, "how": how,
                                       "also_in_statement": bool(tm & fb)})
                    elif tm & fb:
                        mentioned.append({"decl": self.fullname(nid), "kind": kind})
                if opened:
                    label = "OPENED IN PROOF"
                    hows = {o["how"] for o in opened}
                    if self.transport and hows == {"re-wrapped"}:
                        note = "every opening re-wraps it into a constructor (transport candidate; check by hand)"
                    elif "passed on" in hows:
                        note = "at least one opening passes it to a function or theorem: follow those by hand"
                    else:
                        note = "opened; see 'how' per declaration"
                elif mentioned:
                    label, note = "MENTIONED ONLY", "appears only in statements"
                else:
                    label, note = "UNOPENED", "never appears outside the structure's own declarations"
                sres["fields"][f"{st}.{fname}"] = {"index": i, "label": label, "note": note,
                                                   "opened_in": opened, "mentioned_in": mentioned}
            res["structs"][st] = sres
        for tp in self.true_preds:
            tb = self.bits.get(("T", tp), 0)
            used = [self.fullname(nid) for (nid, kind, tm, vm, own) in self.hits if tb and ((tm | vm) & tb)]
            res["true_preds"][tp] = {"found": tp in self.true_pred_id.values(),
                                     "body_is_fun_to_True": self.true_verified.get(tp),
                                     "used_in": used}
        return res


def check_expectations(res, expects):
    """expects: list of 'FIELD=LABEL' with LABEL in OPENED, MENTIONED, UNOPENED. Returns (ok, lines)."""
    want = {"OPENED": "OPENED IN PROOF", "MENTIONED": "MENTIONED ONLY", "UNOPENED": "UNOPENED"}
    allf = {}
    for s in res["structs"].values():
        allf.update(s["fields"])
    ok, out = True, []
    for e in expects:
        name, _, lab = e.partition("=")
        lab = lab.strip().upper()
        got = allf.get(name.strip(), {}).get("label")
        good = got == want.get(lab)
        ok &= good
        out.append(f"control {name}: expected {want.get(lab, lab)}, got {got} -> {'OK' if good else 'FAILED'}")
    return ok, out


def to_markdown(res, ctrl_lines, void):
    L = ["# Field audit", ""]
    if void:
        L += ["**VOID: a control failed, so no result below can be trusted.**", ""]
    L += [f"Read {res['lines']:,} lines, {res['declarations']:,} declarations in {res['seconds']} s.", ""]
    for c in ctrl_lines:
        L.append(f"- {c}")
    if ctrl_lines:
        L.append("")
    for st, s in res["structs"].items():
        L += [f"## `{st}`" + ("" if s["found"] else " (NOT FOUND in this export)"), "",
              f"Fields declared: {s['fields_declared']}; accessors recognised: {s['accessors_found']}.", ""]
        L += ["| Field | Label | Note |", "|---|---|---|"]
        for f, v in s["fields"].items():
            L.append(f"| `{f}` | {v['label']} | {v['note']} |")
        L.append("")
        for f, v in s["fields"].items():
            if v["opened_in"]:
                L.append(f"`{f}` opened in:")
                for o in v["opened_in"]:
                    L.append(f"- `{o['decl']}` ({o['kind']}): {o['how']}")
                L.append("")
        if s["taken_apart_in"]:
            L.append(f"Whole structure taken apart (all fields unpacked; per-field use not determined) in:")
            for d in s["taken_apart_in"]:
                L.append(f"- `{d}`")
            L.append("")
    for tp, v in res["true_preds"].items():
        L += [f"## Always-true check: `{tp}`", "",
              f"Found: {v['found']}. Body is `fun ... => True`: {v['body_is_fun_to_True']}. "
              f"Used in {len(v['used_in'])} declarations.", ""]
    return "\n".join(L)


# ---- test export with known answers ------------------------------------------------------------
def build_fixture(use_c=False):
    """A tiny lean4export-shaped stream. Structure T.S with fields a b c d; structure T.W with one field."""
    lines, names, exprs = [], {}, {}
    nid = [0]; eid = [0]

    def out(o):
        lines.append(json.dumps(o, sort_keys=True, separators=(",", ":")).encode())

    def name(full):
        if full in names:
            return names[full]
        parts = full.split(".")
        pre = 0 if len(parts) == 1 else name(".".join(parts[:-1]))
        nid[0] += 1
        out({"in": nid[0], "str": {"pre": pre, "str": parts[-1]}})
        names[full] = nid[0]
        return nid[0]

    def ex(o):
        key = json.dumps(o, sort_keys=True)
        if key in exprs:
            return exprs[key]
        eid[0] += 1
        o2 = dict(o); o2["ie"] = eid[0]
        out(o2)
        exprs[key] = eid[0]
        return eid[0]

    out({"meta": {"exporter": {"name": "fixture", "version": "0"}, "format": {"version": "3.1.0"},
                  "lean": {"githash": "", "version": ""}}})
    prop = ex({"sort": 0})
    C = lambda n: ex({"const": {"name": name(n), "us": []}})
    A = lambda f, a: ex({"app": {"fn": f, "arg": a}})
    B = lambda i: ex({"bvar": i})
    def Pi(nm, ty, body):
        return ex({"forallE": {"name": name(nm), "type": ty, "body": body, "binderInfo": "default"}})
    def Lam(nm, ty, body):
        return ex({"lam": {"name": name(nm), "type": ty, "body": body, "binderInfo": "default"}})
    def Proj(st, i, e):
        return ex({"proj": {"typeName": name(st), "idx": i, "struct": e}})
    def decl(kind, nm, ty, val=None):
        d = {"name": name(nm), "levelParams": [], "type": ty}
        if kind == "axiom":
            d["isUnsafe"] = False
        else:
            d["value"] = val; d["all"] = [name(nm)]
            if kind == "def":
                d["hints"] = {"regular": 1}; d["safety"] = "safe"
        out({kind: d})

    name("True")
    decl("axiom", "T.P", prop)
    P = C("T.P")
    # inductive True (so the name and constant exist)
    out({"inductive": {"types": [{"name": name("True"), "levelParams": [], "type": prop, "numParams": 0,
                                  "numIndices": 0, "all": [name("True")], "ctors": [name("True.intro")],
                                  "numNested": 0, "isRec": False, "isUnsafe": False, "isReflexive": False}],
                       "ctors": [{"name": name("True.intro"), "levelParams": [], "type": C("True"),
                                  "induct": name("True"), "cidx": 0, "numParams": 0, "numFields": 0,
                                  "isUnsafe": False}], "recs": []}})
    # structure T.S : Prop with fields a b c d : T.P
    S = C("T.S")
    mk_ty = Pi("a", P, Pi("b", P, Pi("c", P, Pi("d", P, S))))
    rec_rhs = Lam("motive", prop, Lam("mk", prop, B(0)))
    out({"inductive": {"types": [{"name": name("T.S"), "levelParams": [], "type": prop, "numParams": 0,
                                  "numIndices": 0, "all": [name("T.S")], "ctors": [name("T.S.mk")],
                                  "numNested": 0, "isRec": False, "isUnsafe": False, "isReflexive": False}],
                       "ctors": [{"name": name("T.S.mk"), "levelParams": [], "type": mk_ty, "induct": name("T.S"),
                                  "cidx": 0, "numParams": 0, "numFields": 4, "isUnsafe": False}],
                       "recs": [{"name": name("T.S.rec"), "levelParams": [], "type": Pi("motive", prop, prop),
                                 "all": [name("T.S")], "numParams": 0, "numIndices": 0, "numMotives": 1,
                                 "numMinors": 1, "rules": [{"ctor": name("T.S.mk"), "nfields": 4, "rhs": rec_rhs}],
                                 "k": False, "isUnsafe": False}]}})
    for i, f in enumerate("abcd"):      # auto-generated accessors: fun self => self.i
        decl("thm", f"T.S.{f}", Pi("self", S, P), Lam("self", S, Proj("T.S", i, B(0))))
    decl("def", "T.S.casesOn", Pi("t", S, prop), Lam("t", S, A(C("T.S.rec"), B(0))))   # own: not an opening
    # structure T.W : Prop with one field
    W = C("T.W")
    out({"inductive": {"types": [{"name": name("T.W"), "levelParams": [], "type": prop, "numParams": 0,
                                  "numIndices": 0, "all": [name("T.W")], "ctors": [name("T.W.mk")],
                                  "numNested": 0, "isRec": False, "isUnsafe": False, "isReflexive": False}],
                       "ctors": [{"name": name("T.W.mk"), "levelParams": [], "type": Pi("x", P, W),
                                  "induct": name("T.W"), "cidx": 0, "numParams": 0, "numFields": 1,
                                  "isUnsafe": False}], "recs": []}})
    decl("axiom", "T.f", Pi("x", P, P))
    decl("axiom", "T.Q", Pi("x", P, prop))
    decl("axiom", "T.qax", P)
    # a: opened in proof, passed to a function (accessor form and raw projection form)
    decl("thm", "T.useA", Pi("s", S, P), Lam("s", S, A(C("T.f"), A(C("T.S.a"), B(0)))))
    decl("def", "T.projA", Pi("s", S, P), Lam("s", S, A(C("T.f"), Proj("T.S", 0, B(0)))))
    # b: mentioned only in a statement
    decl("thm", "T.mentionB", Pi("s", S, A(C("T.Q"), A(C("T.S.b"), B(0)))), Lam("s", S, C("T.qax")))
    # c: never used, unless the positive-control variant adds a use
    if use_c:
        decl("thm", "T.useC", Pi("s", S, P), Lam("s", S, A(C("T.f"), A(C("T.S.c"), B(0)))))
    # d: opened only to be re-wrapped into another structure's constructor
    decl("thm", "T.wrapD", Pi("s", S, W), Lam("s", S, A(C("T.W.mk"), A(C("T.S.d"), B(0)))))
    # the whole structure taken apart
    decl("thm", "T.elim", Pi("s", S, prop), Lam("s", S, A(C("T.S.casesOn"), B(0))))
    # always-true predicate, and a decoy
    decl("def", "T.vac", Pi("x", P, Pi("y", P, prop)), Lam("x", P, Lam("y", P, C("True"))))
    decl("def", "T.notvac", Pi("x", P, prop), Lam("x", P, P))
    decl("thm", "T.usesVac", A(A(C("T.vac"), C("T.qax")), C("T.qax")), C("True.intro"))
    return [ln for ln in lines if ln is not None]


EXPECTED = {"T.S.a": "OPENED IN PROOF", "T.S.b": "MENTIONED ONLY", "T.S.c": "UNOPENED", "T.S.d": "OPENED IN PROOF"}


def self_test(log=sys.stdout):
    ok = True
    def say(msg, good):
        nonlocal ok
        ok &= good
        print(f"[{'PASS' if good else 'FAIL'}] {msg}", file=log)

    res = Audit(["T.S"], ["T.vac", "T.notvac"], progress=0).run(build_fixture()).report()
    f = res["structs"]["T.S"]["fields"]
    for k, v in EXPECTED.items():
        say(f"{k} is {v} (got {f.get(k, {}).get('label')})", f.get(k, {}).get("label") == v)
    op = lambda k: f.get(k, {}).get("opened_in", [])
    hows_a = sorted({o["how"] for o in op("T.S.a")})
    decls_a = sorted(o["decl"] for o in op("T.S.a"))
    say(f"T.S.a openings are 'passed on' in T.useA and T.projA (got {hows_a}, {decls_a})",
        hows_a == ["passed on"] and decls_a == ["T.projA", "T.useA"])
    got_d = [(o["decl"], o["how"]) for o in op("T.S.d")]
    say(f"T.S.d is re-wrapped only, in T.wrapD (got {got_d})", got_d == [("T.wrapD", "re-wrapped")])
    men_b = [m["decl"] for m in f.get("T.S.b", {}).get("mentioned_in", [])]
    say(f"T.S.b mentioned in T.mentionB (got {men_b})", men_b == ["T.mentionB"])
    say(f"structure taken apart in T.elim only, not in its own T.S.casesOn "
        f"(got {res['structs']['T.S']['taken_apart_in']})", res["structs"]["T.S"]["taken_apart_in"] == ["T.elim"])
    tp = res["true_preds"]
    say(f"T.vac body is fun..=>True (got {tp['T.vac']['body_is_fun_to_True']}), used in T.usesVac "
        f"(got {tp['T.vac']['used_in']})", tp["T.vac"]["body_is_fun_to_True"] is True and
        "T.usesVac" in tp["T.vac"]["used_in"])
    say(f"T.notvac is not fun..=>True (got {tp['T.notvac']['body_is_fun_to_True']})",
        tp["T.notvac"]["body_is_fun_to_True"] is False)
    # positive control: add a use of c, it must flip to OPENED
    res_c = Audit(["T.S"], [], progress=0).run(build_fixture(use_c=True)).report()
    gc = res_c["structs"]["T.S"]["fields"].get("T.S.c", {}).get("label")
    say(f"positive control: with a use of c added, T.S.c becomes OPENED IN PROOF (got {gc})", gc == "OPENED IN PROOF")
    # negative control: a wrong expectation must make the run VOID
    good, _ = check_expectations(res, ["T.S.c=OPENED"])
    say("negative control: a wrong --expect is caught (run would be VOID)", good is False)
    good2, _ = check_expectations(res, ["T.S.a=OPENED", "T.S.c=UNOPENED"])
    say("correct --expect lines pass", good2 is True)
    # without the transport split, d is still OPENED but its use is not called 're-wrapped'
    res_nt = Audit(["T.S"], [], transport=False, progress=0).run(build_fixture()).report()
    fd = res_nt["structs"]["T.S"]["fields"].get("T.S.d", {})
    hd = [o["how"] for o in fd.get("opened_in", [])]
    say(f"--no-transport: T.S.d still OPENED, never called re-wrapped (got {hd})",
        fd.get("label") == "OPENED IN PROOF" and "re-wrapped" not in hd)
    print(f"SELF-TEST {'PASSED' if ok else 'FAILED'}", file=log)
    return ok


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--struct", action="append", default=[], help="full name of a structure to audit (repeatable)")
    ap.add_argument("--true-pred", action="append", default=[], help="full name of a predicate expected to be fun..=>True")
    ap.add_argument("--expect", action="append", default=[], help="control FIELD=OPENED|MENTIONED|UNOPENED (repeatable)")
    ap.add_argument("--input", help="NDJSON file (default: standard input)")
    ap.add_argument("--out", default="audit.json")
    ap.add_argument("--md", help="also write a Markdown summary here")
    ap.add_argument("--no-transport", action="store_true", help="skip the re-wrapped/passed-on split (saves ~1 byte/expr)")
    ap.add_argument("--progress", type=int, default=50_000_000)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--write-fixture")
    ap.add_argument("--use-c", action="store_true", help="with --write-fixture: include the positive-control use of c")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(0 if self_test() else 1)
    if a.write_fixture:
        with open(a.write_fixture, "wb") as fh:
            fh.write(b"\n".join(build_fixture(use_c=a.use_c)) + b"\n")
        print("wrote", a.write_fixture)
        return
    if not a.struct:
        ap.error("give at least one --struct (or --self-test)")
    if not self_test(log=open("/dev/null", "w") if sys.platform != "win32" else open("nul", "w")):
        print("self-test FAILED: refusing to run", file=sys.stderr)
        sys.exit(1)
    stream = open(a.input, "rb") if a.input else sys.stdin.buffer
    au = Audit(a.struct, a.true_pred, transport=not a.no_transport, progress=a.progress).run(stream)
    res = au.report()
    ok, ctrl = check_expectations(res, a.expect)
    res["controls"] = ctrl
    res["void"] = not ok
    json.dump(res, open(a.out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    if a.md:
        open(a.md, "w", encoding="utf-8").write(to_markdown(res, ctrl, not ok))
    for c in ctrl:
        print(c, file=sys.stderr)
    print(("VOID: a control failed. " if not ok else "") + f"wrote {a.out}", file=sys.stderr)
    sys.exit(2 if not ok else 0)


if __name__ == "__main__":
    main()
