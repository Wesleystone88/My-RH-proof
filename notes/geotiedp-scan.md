# The second geometry slot, `GeoTiedP`: is anything inside it ever used?

## Pre-registered outcomes (written 26 Nov 2026 before the scan was run)

Copied from `prompts/claude-code-prompt-2026-11-25c.md`.

- **PASS:** every use of a `GeoTiedP`-typed field (`DivT.geo`, `ClassS.geo`, `LinkedFamiliesFixedValues.geo`, or any other field whose type is `GeoTiedP …`) sits in a declaration that only passes it on, or rebuilds another `GeoTiedP` from it (transport), and no declaration takes a component out of it to prove a statement that is not itself a `GeoTiedP`.
- **FINDING:** a declaration that extracts a component (an equivalence, `TiedX`, `CuspTieX`, `IsoInv`, `LevInTie`, the family) and uses it for something else. Report it with its name; that is a real result.

## Result: **PASS**

No declaration on the dependency path of `Main` takes a component out of a `GeoTiedP` to prove anything that is not itself a `GeoTiedP`. The only declaration that takes it apart is the transport `geoTiedP_divTr`. Every other use passes the whole value along or states an equality about the whole field.

## The run

**COMPUTED.** One pass over Sutherland's export (10,163 s), shared with the side-questions task. The compressed sha256 `61a8938a…` was re-verified before the run and the unpacked sha256 `5ea74b91…` computed during it; both match the published values. 1,080,769,508 lines, 1,468,418 declarations. Script: `results/export-names/scan_export.py` (entry point `results/anygeometry-check/export_scan_geotiedp.py`), which imports `tools/export-audit/export_audit.py`; its self-test passed first. Raw output: `results/export-names/scan.json`. I ran it with `--no-transport` (2.4 GB of free RAM), so the tool's "passed on" labels do not distinguish re-wrapping; every opening below was classified by reading the source.

## 1. Text map (READ)

**The type.** [`GeoTiedP`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/LatticeGeometry/GeoTiedP.lean#L124-L128) is an existential: a Shimura family `F`, place and component equivalences, `TiedX`, `ComplexEmbeddingsCompatible`, `CuspTieX`, `IsoInv`, `LevInTie`.

**Fields of that type:**

| Field | Structure | In the export |
|---|---|---|
| `DivT.geo` (field 4) | [`GlobalTheory.Mem.Top.Bl.DivT`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/TiedColumnData.lean#L127-L133) | yes |
| `TiedDataSAlt.geo` (field 19) | [`Formalism.L2.TiedDataSAlt`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkedFamiliesFixedValues.lean#L15) (the structure in LinkedFamiliesFixedValues.lean) | yes |
| `LinkedFamilyData.geo` | [`Formalism.L2.LinkedFamilyData`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/ClassS.lean#L26) (the structure in ClassS.lean) | **no**: no name in the export has `LinkedFamilyData` in it, so it is not on the path |

[`SpectralDataCompatible`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreAltAltBis.lean#L27) also has fields called `inK` and `geo`, but they are **equations** between the fields above (`geo : HEq S.geo q.x.div.geo`), not values of type `GeoTiedP`.

**Constructors:** [`geoOver_stages`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L155-L167) (the one that makes it from nothing) and [`geoTiedP_divTr`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DivisionLocalDataPreservedDivisionLatticeChange.lean#L122-L141) (from another one). `GeoTiedPL.geoTiedP` and `geoTiedP_satisfiable` exist in the source but are not in the export.

**What `geoTiedP_divTr` takes out:** `obtain ⟨F, ePl, eC, hT, hJ, hC, hI, hL⟩`. `F` becomes `famT N h F`; `ePl`, `eC`, `hJ`, `hC` are reused; the fields of `hT` (`shv`, `pl`, `geo`, `lev_κg`) rebuild the new `TiedX`; `hI` and `hL` give the new `IsoInv` and `LevInTie`. Every component goes only into the rebuilt `GeoTiedP (divTr N h X) inK`. The auxiliary goal it proves along the way is one field of the new `TiedX`, so it is part of that rebuilt value.

## 2. Kernel check (COMPUTED): every declaration containing a mark

**Openings of the two exported `geo` fields** (accessor constant or raw `proj`), outside the structures' own declarations. Neither structure is taken apart by `casesOn`/`rec` anywhere.

| Declaration | Opens | Classification (READ from source) |
|---|---|---|
| [`WitTr.divT_setDiv`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/DivisionLocalDataPreservedDivisionLatticeChange.lean#L148-L153) | `DivT.geo` | **transport**: `geo := geoTiedP_divTr … d.geo` into a new `DivT` |
| [`WPt.exists_pinned_spectral_data_compatible`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TiedDataSAssemble.lean#L55-L95) | `DivT.geo`, `TiedDataSAlt.geo` | **pass-on**: hands `q.x.div.geo` whole to `tiedDataS_assemble_alt`; the `TiedDataSAlt.geo` use is the `HEq` equation it gets back |
| [`tiedDataS_assemble_alt`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TiedDataSAssemble.lean#L20-L53) | `TiedDataSAlt.geo` | **pass-on**: puts its argument `geo` into the new record and states `HEq S.geo geo` |
| [`SpectralDataCompatible`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CoreAltAltBis.lean#L27-L48) | both | an equation only: the structure whose field says `HEq S.geo q.x.div.geo` |

**Mentions of the constant `GeoTiedP`** (9 in bodies, 3 in statements only).
- Bodies: `TiedDataSAlt` and `Mem.Top.Bl.DivT` (the structure declarations), `GeoGraft.GeoOver` (a definition), `SpectralDataCompatible`, `exists_pinned_spectral_data_compatible`, `tiedDataS_assemble_alt`, `geoTiedP_divTr`, `DivRec.exists_divT`, `DivRec.geoOver_stages`.
- Statements only: the projections `DivT.geo`, `TiedDataSAlt.geo`, `SpectralDataCompatible.geo`.

`GeoOver` is used in one body, [`exists_divT`](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/TupPinsOfMuIsW.lean#L175-L195), which does `obtain ⟨X, inK, …, hG, -⟩ := geoOver_stages …` and writes `geo := hG` into a `DivT`: pass-on. `geoOver_stages` is consumed only by `exists_divT`, and `geoTiedP_divTr` only by `divT_setDiv`.

**DERIVED, why this is complete.** To take a `GeoTiedP` apart a declaration needs a term of that type: from a field (all openings are listed above), from `geoOver_stages` (only `exists_divT`), or from a hypothesis or result whose type mentions `GeoTiedP` (listed). None of them extracts a component except `geoTiedP_divTr`.

## 3. Nielsen's claims

- **`GeoTiedP.geoTied` and `GeoTiedP.formsTieX` are never called: confirmed.** READ: a search of the whole pinned source for those calls finds only their definitions ([GeoTiedP.lean:136-144](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/LocalToGlobal/LatticeGeometry/GeoTiedP.lean#L136-L144)). COMPUTED: neither is in the export, so nothing on the path of `Main` calls them.
- **The family behind the built `GeoTiedP` is the degenerate one: confirmed.** READ: `geoOver_stages` uses `divXFl D jc X₀`, `famFlJ … : ShimFam D (geoDegenerate …) PUnit` and `tiedX_fl`, with `inK := fun _ _ => True` and the `Q` of `GeoOver` equal to `fun _ => True`. COMPUTED: `geoOver_stages` mentions `divXFl`, `famFlJ` and `tiedX_fl` in its body, and is the only user of `tiedX_fl`.

## Limits

- The export covers what `Main` depends on; it says nothing about code outside that closure (including `LinkedFamilyData`).
- "Pass-on" and "transport" rest on reading the source of the listed declarations at `4e8bb36`; the exported terms were not printed.
- A PASS says nothing on the path *reads* the content of this slot. It does not say the slot could be deleted without breaking the build.

*Claude Code wrote this note and the script (26 Nov 2026) from `prompts/claude-code-prompt-2026-11-25c.md`, which Claude in chat wrote.*
