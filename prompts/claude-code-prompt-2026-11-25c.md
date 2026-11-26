# Claude Code: the second geometry slot, `GeoTiedP` (25 Nov 2026)

Written by Claude in chat. Run after the engine test bench (`claude-code-prompt-2026-11-25b.md`).
Rules: no builds, no `lake`, nothing written in `C:\rhc`, no git until the last step; stop if C: would drop below 25 GB free. Labels READ / DERIVED / GUESS.

## Why

`notes/anygeometry-export-scan.md` showed the always-true stamp (`OAt.geo`) is never read. The removal map (§2.5) found a **second** geometry slot that is not `True`: `DivT.geo : GeoTiedP Y inK` (TiedColumnData.lean:126–133), also a field of `ClassS` and `LinkedFamiliesFixedValues`. `GeoTiedP X inK` is an existential over a Shimura family, place and component equivalences, `TiedX`, `CuspTieX`, `IsoInv`, `LevInTie` (GeoTiedP.lean:124–128). It is built by `geoOver_stages` (TupPinsOfMuIsW.lean:155–167) with `inK := fun _ _ => True` and `Q := fun _ => True`, on the degenerate model Nielsen describes, and carried across stages by `geoTiedP_divTr` (DivisionLocalDataPreservedDivisionLatticeChange.lean:122, used at :148–150), which destructures it and rebuilds it. Question: does anything ever **use** what is inside it, beyond carrying it?

## Pre-registered outcomes (copy to the top of the note before scanning)

- **PASS:** every use of a `GeoTiedP`-typed field (`DivT.geo`, `ClassS.geo`, `LinkedFamiliesFixedValues.geo`, or any other field whose type is `GeoTiedP …`) sits in a declaration that only passes it on, or rebuilds another `GeoTiedP` from it (transport), and no declaration takes a component out of it to prove a statement that is not itself a `GeoTiedP`.
- **FINDING:** a declaration that extracts a component (an equivalence, `TiedX`, `CuspTieX`, `IsoInv`, `LevInTie`, the family) and uses it for something else. Report it with its name; that is a real result.

## Tasks

1. **Text map** (like `notes/anygeometry-removal-map.md`): every field whose type is `GeoTiedP …`; its constructors; its readers (projections, `obtain`/`rcases`/`cases` on it followed by a use). For `geoTiedP_divTr`, say exactly which components it takes out and whether each goes only into the rebuilt `GeoTiedP`.
2. **Kernel check**: rerun the streaming scan on Sutherland's export (reuse `results/anygeometry-check/export_scan.py`, extended with these targets; reuse the downloaded file if it is still on disk, verifying its sha256 again). Mark `const` uses of the `geo` projections above and `proj` nodes on those structures at the `geo` index, and the constant `GeoTiedP`. List every declaration containing a mark and classify each by reading its source at `4e8bb36`.
3. **Check Nielsen's claims directly**: that `GeoTiedP.geoTied` and `GeoTiedP.formsTieX` are never called (in the source and in the export), and that the family behind the built `GeoTiedP` is the degenerate one (`divXFl`, `tiedX_fl`).

Write to `notes/geotiedp-scan.md`; save the extended script as `results/anygeometry-check/export_scan_geotiedp.py`.

## Last step

Commit and push the note, the script and this prompt, saying Claude Code wrote the note and script and Claude in chat wrote the prompt. Report PASS or FINDING with the declaration list.
