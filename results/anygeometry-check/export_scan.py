#!/usr/bin/env python3
"""Scan Andrew Sutherland's lean4export of the headline proof for uses of the geometry stamp.

Usage (the file is 61.5 GB unpacked; never write it to disk, stream it):

    zstd -dc --long=30 solution.ndjson.zst | python export_scan.py --out export_scan_results.json

Format: lean4export 3.1.0, one JSON object per line. Names `{"in":N,"str":{"pre":P,"str":S}}` or
`{"in":N,"num":{"i":I,"pre":P}}`; expressions `{"ie":N,<kind>:...}` whose children always have
smaller ids than their parent; declarations `{"thm"|"def"|"axiom"|"inductive"|"quot": ...}`.

What it marks (bit classes), propagating "contains a marked node" from children to parents in the same
pass (children are always emitted before parents):

    1  OAt.geo        a `const` named <NS>.OAt.geo, or a `proj` on structure OAt with index 0
    2  GeoCl eliminator   a `const` <NS>.GeoCl.<x> where x is not a constructor (base, step)
    4  anyGeometry    a `const` <NS>.anyGeometry
    8  OAt.lam        a `const` named <NS>.OAt.lam, or a `proj` on OAt with index 1
   16  OAt eliminator a `const` <NS>.OAt.<x> for x in rec, recOn, casesOn, below, brecOn, binductionOn

where <NS> is GlobalTheory.Mem.Top.Bl. A declaration "contains" a class if the type or value (for an
inductive: any constructor type, recursor type or rule right-hand side) contains a marked node.

Memory: the name table is two arrays of 4 bytes per name; marks are a sparse dict.
"""
import sys, re, json, time, argparse
from array import array

NS = ["GlobalTheory", "Mem", "Top", "Bl"]
OAT_ELIM = {"rec", "recOn", "casesOn", "below", "brecOn", "binductionOn", "ibelow", "ndrec", "ndrecOn"}
GEOCL_CTORS = {"base", "step"}
INTEREST = {"OAt", "GeoCl", "anyGeometry", "geoCl", "geoCl_of", "geo", "lam", "mk"} | OAT_ELIM | GEOCL_CTORS | \
    {"below", "brecOn", "binductionOn", "ibelow", "ndrec", "ndrecOn", "casesOn", "recOn", "rec"}

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="export_scan_results.json")
ap.add_argument("--progress", type=int, default=50_000_000)
args = ap.parse_args()

# ---- name table -----------------------------------------------------------------------------
parent = array("I")
strid = array("I")
strings = [""]
strmap = {"": 0}
numvals = {}


def ensure(n):
    if n >= len(parent):
        grow = max(n + 1 - len(parent), 1_000_000)
        parent.extend(array("I", [0]) * grow)
        strid.extend(array("I", [0]) * grow)


def comp(n):
    return numvals.get(n) if strid[n] == 0 and n in numvals else strings[strid[n]]


def components(n):
    out = []
    while n:
        out.append(comp(n))
        n = parent[n]
    out.reverse()
    return out


def fullname(n):
    return ".".join(str(c) for c in components(n))


oat_id = geocl_id = None
class_of_name = {}      # name id -> bit
present = {}            # full name string -> name id, for the names asked about in the task
TASK_NAMES = {"OAt", "OAt.geo", "OAt.lam", "OAt.mk", "OAt.rec", "OAt.casesOn", "GeoCl", "GeoCl.base", "GeoCl.step",
              "GeoCl.rec", "GeoCl.casesOn", "GeoCl.recOn", "anyGeometry", "geoCl", "geoCl_of"}
extra_names = {}        # other OAt.* / GeoCl.* names seen, for the report


def on_new_name(n, p, s):
    global oat_id, geocl_id
    if s not in INTEREST:
        return
    comps = components(n)
    if comps[:4] != NS:
        return
    rest = comps[4:]
    full = ".".join(rest)
    if full in TASK_NAMES:
        present[full] = n
    if full == "OAt":
        oat_id = n
    elif full == "GeoCl":
        geocl_id = n
    elif full == "anyGeometry":
        class_of_name[n] = 4
    elif len(rest) == 2 and rest[0] == "OAt":
        x = rest[1]
        if x == "geo":
            class_of_name[n] = 1
        elif x == "lam":
            class_of_name[n] = 8
        elif x in OAT_ELIM:
            class_of_name[n] = 16
        extra_names[full] = n
    elif len(rest) == 2 and rest[0] == "GeoCl":
        x = rest[1]
        if x not in GEOCL_CTORS:
            class_of_name[n] = 2
        extra_names[full] = n


# ---- line patterns --------------------------------------------------------------------------
re_const = re.compile(rb'^\{"const":\{"name":(\d+),"us":\[[^\]]*\]\},"ie":(\d+)\}')
re_app = re.compile(rb'^\{"app":\{"arg":(\d+),"fn":(\d+)\},"ie":(\d+)\}')
re_forall = re.compile(rb'^\{"forallE":\{"binderInfo":"[a-zA-Z]+","body":(\d+),"name":\d+,"type":(\d+)\},"ie":(\d+)\}')
re_lam = re.compile(rb'^\{"ie":(\d+),"lam":\{"binderInfo":"[a-zA-Z]+","body":(\d+),"name":\d+,"type":(\d+)\}\}')
re_let = re.compile(rb'^\{"ie":(\d+),"letE":\{"body":(\d+),"name":\d+,"nondep":(?:true|false),"type":(\d+),"value":(\d+)\}\}')
re_proj = re.compile(rb'^\{"ie":(\d+),"proj":\{"idx":(\d+),"struct":(\d+),"typeName":(\d+)\}\}')

mark = {}               # expr id -> bit mask (only nonzero)
decl_hits = []          # (kind, name id, mask)
decl_total = 0
decl_by_kind = {}
decl_mask_counts = {1: 0, 2: 0, 4: 0, 8: 0, 16: 0}
seed_lines = {1: [], 2: [], 4: [], 8: [], 16: []}
fallback_lines = 0
lines = 0
t0 = time.time()
CHILD_KEYS = ("arg", "fn", "body", "type", "value", "struct", "expr")


def mask_of(ids):
    m = 0
    g = mark.get
    for i in ids:
        m |= g(i, 0)
    return m


def set_mark(ie, m):
    if m:
        mark[ie] = m


def decl_roots(d):
    """expression ids that make up a declaration (type/value; for inductives all constructor/recursor parts)"""
    r = []
    for k in ("type", "value"):
        if k in d:
            r.append(d[k])
    for t in d.get("types", []):
        if "type" in t:
            r.append(t["type"])
    for c in d.get("ctors", []):
        if isinstance(c, dict) and "type" in c:
            r.append(c["type"])
    for c in d.get("recs", []):
        if "type" in c:
            r.append(c["type"])
        for ru in c.get("rules", []):
            r.append(ru["rhs"])
    return r


for raw in sys.stdin.buffer:
    lines += 1
    if lines % args.progress == 0:
        print(f"{lines/1e6:.0f}M lines, {time.time()-t0:.0f}s, marks {len(mark):,}, decls {decl_total:,}, "
              f"hits {len(decl_hits):,}, distinct name strings {len(strings):,}", file=sys.stderr, flush=True)
    c1 = raw[:6]
    if c1 == b'{"in":':
        j = json.loads(raw)
        n = j["in"]
        ensure(n)
        if "str" in j:
            p = j["str"]["pre"]
            s = j["str"]["str"]
            k = strmap.get(s)
            if k is None:
                k = len(strings)
                strings.append(s)
                strmap[s] = k
            parent[n] = p
            strid[n] = k
            on_new_name(n, p, s)
        else:
            parent[n] = j["num"]["pre"]
            strid[n] = 0
            numvals[n] = j["num"]["i"]
    elif c1 == b'{"il":':
        pass
    elif c1 == b'{"ie":' or c1 == b'{"app"' or c1 == b'{"bvar' or c1 == b'{"cons' or c1 == b'{"fora':
        if c1 == b'{"cons':
            m = re_const.match(raw)
            if m:
                bit = class_of_name.get(int(m.group(1)))
                if bit:
                    ie = int(m.group(2))
                    mark[ie] = mark.get(ie, 0) | bit
                    if len(seed_lines[bit]) < 20:
                        seed_lines[bit].append((ie, int(m.group(1))))
            continue
        if c1 == b'{"app"':
            m = re_app.match(raw)
            if m and mark:
                mm = mark.get(int(m.group(1)), 0) | mark.get(int(m.group(2)), 0)
                if mm:
                    mark[int(m.group(3))] = mm
            continue
        if c1 == b'{"fora':
            m = re_forall.match(raw)
            if m and mark:
                mm = mark.get(int(m.group(1)), 0) | mark.get(int(m.group(2)), 0)
                if mm:
                    mark[int(m.group(3))] = mm
            continue
        if c1 == b'{"bvar':
            continue
        # starts with {"ie":
        rest = raw[6:20]
        if b'"sort"' in raw[:40]:
            continue
        if b'"lam"' in raw[:40]:
            m = re_lam.match(raw)
            if m and mark:
                mm = mark.get(int(m.group(2)), 0) | mark.get(int(m.group(3)), 0)
                if mm:
                    mark[int(m.group(1))] = mm
            continue
        if b'"proj"' in raw[:50]:
            m = re_proj.match(raw)
            if m:
                ie = int(m.group(1))
                idx = int(m.group(2))
                tn = int(m.group(4))
                mm = mark.get(int(m.group(3)), 0)
                if tn == oat_id and idx == 0:
                    mm |= 1
                    if len(seed_lines[1]) < 20:
                        seed_lines[1].append((ie, "proj"))
                elif tn == oat_id and idx == 1:
                    mm |= 8
                if mm:
                    mark[ie] = mm
            continue
        if b'"letE"' in raw[:40]:
            m = re_let.match(raw)
            if m and mark:
                mm = mask_of((int(m.group(2)), int(m.group(3)), int(m.group(4))))
                if mm:
                    mark[int(m.group(1))] = mm
            continue
        # anything else (lit, mdata, fvar, mvar, ...): generic fallback
        fallback_lines += 1
        j = json.loads(raw)
        if mark:
            ids = []
            for v in j.values():
                if isinstance(v, dict):
                    for k2 in CHILD_KEYS:
                        if k2 in v and isinstance(v[k2], int):
                            ids.append(v[k2])
            mm = mask_of(ids)
            if mm:
                mark[j["ie"]] = mm
    else:
        # a declaration (or the meta line)
        if c1 == b'{"meta':
            continue
        d = json.loads(raw)
        kind = next(iter(d))
        body = d[kind]
        decl_total += 1
        decl_by_kind[kind] = decl_by_kind.get(kind, 0) + 1
        if not mark:
            continue
        if kind == "inductive":
            nm = body["types"][0]["name"]
            roots = decl_roots(body)
        else:
            nm = body.get("name")
            roots = decl_roots(body)
        mm = mask_of(roots)
        if mm:
            decl_hits.append((kind, nm, mm))
            for b in (1, 2, 4, 8, 16):
                if mm & b:
                    decl_mask_counts[b] += 1
# ---- report ---------------------------------------------------------------------------------
print(f"done: {lines:,} lines in {time.time()-t0:.0f}s; decls {decl_total:,}; marks {len(mark):,}; "
      f"fallback lines {fallback_lines:,}", file=sys.stderr)
res = {
    "lines": lines, "seconds": round(time.time() - t0), "declarations": decl_total, "by_kind": decl_by_kind,
    "marked_expressions": len(mark), "fallback_lines": fallback_lines,
    "oat_name_id": oat_id, "geocl_name_id": geocl_id,
    "present": {k: (fullname(v) if True else None) for k, v in present.items()},
    "extra_names": {k: fullname(v) for k, v in extra_names.items()},
    "classes": {"1": "OAt.geo", "2": "GeoCl eliminator", "4": "anyGeometry", "8": "OAt.lam", "16": "OAt eliminator"},
    "declarations_with_class": {str(b): decl_mask_counts[b] for b in decl_mask_counts},
    "seed_examples": {str(b): [list(map(str, s)) for s in v] for b, v in seed_lines.items()},
    "decl_hits": [],
}
for kind, nm, mm in decl_hits:
    res["decl_hits"].append({"kind": kind, "name": fullname(nm), "mask": mm})
json.dump(res, open(args.out, "w"), indent=1)
print("wrote", args.out, file=sys.stderr)
