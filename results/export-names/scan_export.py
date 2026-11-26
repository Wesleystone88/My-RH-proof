#!/usr/bin/env python3
"""One streaming pass over Sutherland's lean4export, serving two tasks kept separate in the output:

  [25c] the second geometry slot: who opens the `geo : GeoTiedP …` field of DivT, LinkedFamilyData and
        TiedDataSAlt (accessor constants and raw `proj` nodes), who takes those structures apart, and who
        mentions GeoTiedP and related constants.
  [26h] the open questions of leanprover-community/riemann-hypothesis issues #2 and #5: full name list,
        and for a list of last name components, which declarations mention them (body vs statement only).

Built on tools/export-audit/export_audit.py (imported, not copied).  "Mentions" means the constant occurs
in the declaration's type or value.

    zstd -dc --long=30 solution.ndjson.zst | python scan_export.py --names-out names.txt --out scan.json
    python scan_export.py --self-test
"""
import sys, os, json, argparse, io
from array import array

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "export-audit"))
import export_audit as ea

STRUCTS = ["GlobalTheory.Mem.Top.Bl.DivT", "Formalism.L2.LinkedFamilyData", "Formalism.L2.TiedDataSAlt"]

LASTS_25C = {"GeoTiedP", "GeoTiedPL", "GeoOver", "geoOver_stages", "geoTiedP_divTr", "geoTied", "formsTieX",
             "divXFl", "tiedX_fl", "famFlJ", "geoTiedP", "geoTiedP_satisfiable"}
LASTS_26H = {"linkMu_of_sizes", "linkMu_of_full", "linkMu", "linkMu_of_linkDIV", "omTied_retie_of_cube",
             "GeneralHyps", "GeneralHypU", "GeneralHypV", "rhOfAll", "riemannHypothesis"}


class Scan(ea.Audit):
    def __init__(self, structs, lasts, **kw):
        super().__init__(structs, [], **kw)
        self.lasts = set(lasts)
        self.numvals = {}
        self.name_targets = {}      # name id -> full name
        self.decl_names = array("I")
        self.all_decl_ids = set()   # ids of target names that are declarations (incl. ctors / recursors)

    def fullname(self, n):
        out = []
        while n:
            if self.strid[n] == 0 and n in self.numvals:
                out.append(str(self.numvals[n]))
            else:
                out.append(self.strings[self.strid[n]])
            n = self.parent[n]
        return ".".join(reversed(out))

    def on_name(self, j):
        super().on_name(j)
        n = j["in"]
        if "str" in j:
            if j["str"]["str"] in self.lasts:
                full = self.fullname(n)
                self.name_targets[n] = full
                self.true_pred_id[n] = full      # reuse the base class: marks `const` nodes of this name
        else:
            self.numvals[n] = j["num"]["i"]

    def on_decl(self, d):
        kind = next(iter(d))
        body = d[kind]
        if kind == "inductive":
            types = body.get("types", [])
            if types:
                self.decl_names.append(types[0]["name"])
            for part in ("types", "ctors", "recs"):
                for x in body.get(part, []):
                    if x["name"] in self.name_targets:
                        self.all_decl_ids.add(x["name"])
        else:
            nm = body.get("name", 0)
            self.decl_names.append(nm)
            if nm in self.name_targets:
                self.all_decl_ids.add(nm)
        super().on_decl(d)

    def mentions(self):
        """full target name -> dict(in_export, body=[...], statement_only=[...])"""
        out = {}
        for nid, full in self.name_targets.items():
            b = self.bits.get(("T", full), 0)
            body, stmt = [], []
            if b:
                for (d, kind, tm, vm, own) in self.hits:
                    if d == nid:
                        continue
                    if vm & b:
                        body.append(self.fullname(d))
                    elif tm & b:
                        stmt.append(self.fullname(d))
            out[full] = {"is_declaration_in_export": nid in self.all_decl_ids,
                         "mentioned_in_body": sorted(body), "mentioned_in_statement_only": sorted(stmt)}
        return out


def self_test():
    """The base tool's fixture, plus name mentions: T.f is used in the bodies of T.useA, T.projA, T.wrapD?"""
    ok = ea.self_test(log=io.StringIO())
    sc = Scan(["T.S"], {"f", "Q", "S", "nosuch"}, progress=0).run(ea.build_fixture())
    m = sc.mentions()
    chk = [("T.f used in the bodies of T.useA and T.projA only",
            m["T.f"]["mentioned_in_body"] == ["T.projA", "T.useA"] and m["T.f"]["is_declaration_in_export"]),
           ("T.Q appears only in the statement of T.mentionB",
            m["T.Q"]["mentioned_in_body"] == [] and m["T.Q"]["mentioned_in_statement_only"] == ["T.mentionB"]),
           ("T.S struct audit unchanged under the subclass",
            {k: v["label"] for k, v in sc.report()["structs"]["T.S"]["fields"].items()} == ea.EXPECTED),
           ("a name with no matching component is not listed", "nosuch" not in " ".join(m)),
           ("declaration names collected", "T.useA" in [sc.fullname(i) for i in sc.decl_names])]
    for msg, good in chk:
        print("[%s] %s" % ("PASS" if good else "FAIL", msg))
        ok &= good
    print("SELF-TEST", "PASSED" if ok else "FAILED")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--out", default="scan.json")
    ap.add_argument("--names-out", default="names.txt")
    ap.add_argument("--input")
    ap.add_argument("--no-transport", action="store_true")
    a = ap.parse_args()
    if not self_test():
        sys.exit(1)
    if a.self_test:
        return
    stream = open(a.input, "rb") if a.input else sys.stdin.buffer
    sc = Scan(STRUCTS, LASTS_25C | LASTS_26H, transport=not a.no_transport, progress=50_000_000).run(stream)
    res = sc.report()
    res["mentions"] = sc.mentions()
    names = sorted(sc.fullname(i) for i in sc.decl_names)
    with open(a.names_out, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(names) + "\n")
    res["names_written"] = len(names)
    rh = res["mentions"].get("rhOfAll", {})
    res["control_26h"] = {
        "riemannHypothesis_mentions_rhOfAll_in_body": "riemannHypothesis" in rh.get("mentioned_in_body", []),
        "riemannHypothesis_in_name_list": "riemannHypothesis" in names}
    json.dump(res, open(a.out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("control_26h", res["control_26h"], file=sys.stderr)
    print("wrote", a.out, a.names_out, file=sys.stderr)


if __name__ == "__main__":
    main()
