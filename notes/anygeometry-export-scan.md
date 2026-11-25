# Scan of the exported proof terms for any use of the geometry stamp

## Pre-registered outcomes (written 25 Nov 2026 before any scan was run)

These come from `prompts/claude-code-prompt-2026-11-25.md` and are copied here unchanged so the result can be judged against them.

- **PASS:** no declaration in the export uses an eliminator of `GeoCl` (`GeoCl.rec`, `GeoCl.casesOn`, `GeoCl.recOn`, `GeoCl.below`, `GeoCl.brecOn`, or any `match`/aux definition built on them), other than the auto-generated declarations of `GeoCl` itself; **and** every use of `OAt.geo` (the projection constant, or a primitive projection `proj` on structure `OAt` with index 0) sits in a declaration that only passes the value into a `GeoCl` constructor or into another `OAt`.
- **FAIL / finding:** any `GeoCl` eliminator use, or any `OAt.geo` use in a declaration that is not pass-through. Report it with the declaration name. That would be a real result, not a failure of the task.

## Result: **PASS**

**READ (scan output).** Over the whole export (1,080,769,508 lines, 1,468,418 declarations):

- **GeoCl eliminators:** one declaration contains a mark, and it is the auto-generated `inductive GlobalTheory.Mem.Top.Bl.GeoCl` itself (its own recursor rules use `GeoCl.rec`). No other declaration uses `GeoCl.rec`, and `GeoCl.casesOn`, `GeoCl.recOn`, `GeoCl.below` and `GeoCl.brecOn` do not occur in the export at all. A `match` or auxiliary definition built on an eliminator would itself be an exported declaration containing the mark, so none exists.
- **`OAt.geo`:** exactly **three** declarations contain a use (the projection constant, or a `proj` on `OAt` with index 0): the auto-generated projection `OAt.geo` itself, `divEx_geoCl`, and `oAt_setDiv`. Both non-generated ones are the pass-throughs that `notes/anygeometry-removal-map.md` §2.3 predicted, and no others.
- **`OAt` eliminators:** none (`OAt.rec` exists as the structure's own recursor; no declaration uses it).

**DERIVED.** The two uses are pass-through by reading their source at `4e8bb36` (below), so every use of `OAt.geo` in the export is accounted for and none is real. This is the kernel-level check the removal map said was missing, with one limit stated in §6.

## 1. Download and verification

**READ.** `https://math.mit.edu/~drew/grh/solution.ndjson.zst`, 7,699,933,588 bytes. The first download stopped early (6,120,986,480 bytes, wrong hash); I resumed it with a range request to the full size. Compressed sha256 `61a8938ad5f5e57397c1c0e3b954916af546d9004ade01c3555744a681b05381` matches the published value. The file was never unpacked to disk: it was streamed through `zstd -dc --long=30` (miniconda's `zstd`) into the script, with `tee` computing the sha256 of the unpacked stream on the fly. That came out as `5ea74b912147c5c93cc2b6d70cc727cf908df2f62ac6a20480a3fa02f6be244e`, **matching the published unpacked hash**, so the scan read the complete, intact export. The downloaded file is outside the repo and is not committed.

**Resources.** Free RAM before the run: 5.0 GB; free disk 51.9 GB (it stayed above the 25 GB limit; the file is 7.7 GB). The peak memory of the scanner was **not measured** (no instrumentation); it finished normally. The run took **153 minutes**, almost all of it waiting on the Windows pipe (CPU time was 1 min 54 s user and 11 min 36 s system), not on Python.

## 2. The format

**READ.** `lean4export` 3.1.0, Lean 4.33.1 (githash `819816b…`). One JSON object per line; keys come in alphabetical order. First lines:

```
{"meta":{"exporter":{"name":"lean4export","version":"3.1.0"},"format":{"version":"3.1.0"},"lean":{"githash":"819816b2e0a3bf405af45ae5c7af2491d8f5bee6","version":"4.33.1"}}}
{"in":1,"str":{"pre":0,"str":"Eq"}}                                  name: id, parent, string
{"in":8,"num":{"i":0,"pre":7}}                                         numeric name component
{"il":1,"param":2}                                                     universe level
{"app":{"arg":2,"fn":7},"ie":8}                                       expression, "ie" is its id
{"forallE":{"binderInfo":"default","body":3,"name":8,"type":2},"ie":4}
{"ie":170,"proj":{"idx":0,"struct":1,"typeName":31}}                  primitive projection
{"const":{"name":1,"us":[1]},"ie":7}
{"thm":{"all":[630],"levelParams":[],"name":630,"type":2696,"value":2702}}   declaration
{"def":{"all":[30],"hints":{"regular":1},"levelParams":[11],"name":30,"safety":"safe","type":116,"value":117}}
{"inductive":{"ctors":[…],"recs":[…],"types":[…]}}
```

**READ.** Ids are emitted **children before parents** (an `app` always refers to smaller ids), which is what lets one pass propagate "contains a marked node" upward. Declaration counts: 1,246,110 theorems, 214,241 definitions, 7,969 inductives, 91 opaque definitions, 3 axioms, 4 quotient entries.

## 3. Which target names are in the export

**READ.** Full names are in the namespace `GlobalTheory.Mem.Top.Bl`.

| Name | In the export |
|---|---|
| `OAt`, `OAt.geo`, `OAt.lam`, `OAt.mk`, `OAt.rec` | yes |
| `OAt.casesOn`, `OAt.recOn` | **no** |
| `GeoCl`, `GeoCl.base`, `GeoCl.step`, `GeoCl.rec` | yes |
| `GeoCl.casesOn`, `GeoCl.recOn`, `GeoCl.below`, `GeoCl.brecOn` | **no** |
| `anyGeometry`, `geoCl`, `geoCl_of` | yes |

An absent name means nothing the five headline theorems depend on uses it.

## 4. How the scan works

`results/anygeometry-check/export_scan.py` (one pass, streaming). It resolves target names as the name records arrive (name table kept in two 4-byte arrays), marks `const` nodes named `OAt.geo`, `OAt.lam`, `OAt` eliminators, `anyGeometry`, and any `GeoCl.x` that is not a constructor, and marks `proj` nodes on `OAt` with index 0 (and index 1 for `lam`). It propagates a bit mask from children to parents in the same pass, and for every declaration ORs the masks of its type and value (for inductives, of every constructor type, recursor type and recursor rule). **27,329** expression lines (kinds other than app, lambda, forall, let, const, projection, sort, bvar) were handled by a generic fallback. A synthetic test (marks, propagation, three expected declarations) passed before the real run.

Rerun: `zstd -dc --long=30 solution.ndjson.zst | python export_scan.py --out export_scan_results.json`. The raw output is `results/anygeometry-check/export_scan_results.json`.

## 5. Every declaration containing a mark

**READ.** 19 declarations contain at least one mark (classes: 1 `OAt.geo`, 2 `GeoCl` eliminator, 4 `anyGeometry`, 8 `OAt.lam`).

| Declaration (`GlobalTheory…`) | Classes | What the marked use is |
|---|---|---|
| `Mem.Top.Bl.OAt.geo` | 1 | **auto-generated** projection; its value is the `proj` on `OAt` index 0 |
| `Mem.Top.Closing.divEx_geoCl` | 1, 4, 8 | **pass-through**: `⟨⟨geoCl_of o.geo, o.lam⟩⟩` ([PublishedInputsImplyConclusion.lean:39-49][pic39]); `o.geo` goes into `geoCl_of` (= `GeoCl.base`) and the result into a new `OAt` |
| `Mem.OxMove.oAt_setDiv` | 1, 8 | **pass-through**: `⟨⟨GeoCl.step N h hp.geo, lamAre_copy … hp.lam⟩⟩` ([DivisionGeometryScalarsTransferSetDivision.lean:105-107][dgs105]) |
| `Mem.Top.Bl.GeoCl` (the `inductive`) | 2 | **auto-generated**: its own recursor rules |
| `T.parameter_of_discrete_series_ray_alt` | 8 | reads `OAt.lam`, not `geo` (the real `lam` reader of removal map §2.3) |
| `Mem.Top.Bl.OAt.lam` | 8 | auto-generated projection |
| the other 13 | 4 only | mention `anyGeometry` (as the `Γ` argument) and nothing else; listed in the table below |

**READ, the other 13 (class 4 only):** `Mem.Top.Bl.parametersOfDependence`, `Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt`, `Mem.Top.DivRec.divEx_prov`, `Mem.Top.DivRec.divEx_of_ox`, `Mem.Top.Closing.memberE_closing_alt_alt`, `Mem.Top.Bl.exists_baseLattice_of_pair_alt`, `Mem.Top.Bl.exists_baseLattice_of_prime_alt`, `T.member_exists_baseLattice_alt`, `Fc.StageOneU.member_bundles_large_unramified_exponents_alt`, `T.large_unramified_exponent_bundles_exist_alt`, `UpperTheory.GalC.final_of_alt`, `Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`, `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`.

**Comparison with `anygeometry-removal-map.md` §2.3.** The map's expected pass-throughs (`divEx_geoCl`, `oAt_setDiv`) are exactly the two non-generated `OAt.geo` users here. Its real reader of `lam` (`ParameterOfDiscreteSeriesRay`) is `parameter_of_discrete_series_ray_alt`. `divEx_prov` (which builds `geo := trivial`) contains `anyGeometry` but no `OAt.geo` mark, as expected for a constructor.

## 6. Counts for context, and a finding

**READ.** Declarations in the export that mention `anyGeometry`: **14** (the 13 above plus `divEx_geoCl`). That mention `OAt.lam`: **4** (`OAt.lam` itself, `divEx_geoCl`, `oAt_setDiv`, `parameter_of_discrete_series_ray_alt`).

**DERIVED, new.** The source has 30 declarations that mention `anyGeometry` (removal map §1), counting the definition itself. Only these 14 appear in the export with the constant in their term; the other 15 do not, so they are not used by the five headline theorems (a declaration in the export would contain the constant). All 14 are the `_alt` routes (names ending in `_alt`, or the shared `divEx_*` and `parametersOfDependence`). The older route (`member_bundles_large_ue`, `open_of_hypothesesUE`, `memberE_exBL_of_pair`, `memberE_closing`, `nonempty_hyps_of_classicalTheoremsUE`, `hypsE₂`, and so on) does not appear in the export. So a build test of removal would only need to succeed on the declarations the proof actually depends on.

## 7. What this does and does not show

- **Shows:** at the level the kernel works at, no declaration the five theorems depend on uses an eliminator of `GeoCl` or `OAt`, and `OAt.geo` is used in exactly two declarations besides its own projection.
- **Limit 1.** "Pass-through" for those two uses rests on reading their source, as the prompt specified, plus the fact that neither declaration contains any other mark. I did not extract and print the exported term around the use. Doing that would need a second full pass (about 2.5 hours) that keeps the 6,108 marked expression lines.
- **Limit 2.** The marks are structural: a declaration that only *references* another by name is not marked by that reference; the referenced declaration is, and appears in the list.
- **Limit 3.** This is the export of the declarations `Main` depends on. It says nothing about the 16 source declarations outside it, and it does not show that the proof would still build if the `geo` field were deleted (the removal map's Tier 1).

*Written by Claude Code (25 Nov 2026) from `prompts/claude-code-prompt-2026-11-25.md`, which Claude in chat wrote.*

[pic39]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/PublishedInputsImplyConclusion.lean#L39-L49
[dgs105]: https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DivisionGeometryScalarsTransferSetDivision.lean#L105-L107
