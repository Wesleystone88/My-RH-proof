# Answers to side questions from Sutherland's export (issues #5 and #2 of leanprover-community/riemann-hypothesis)

## Pre-registered questions (written 26 Nov 2026 before the scan was run)

Copied from `prompts/claude-code-prompt-2026-11-26h-export-questions.md`.

1. **Name list.** Write every declaration name in the export, one per line, sorted, to `results/export-names/names.txt`, then zstd-compress it. Record the count (expected 1,468,418, the figure from our earlier scan) and the sha256 of the compressed file. Commit the compressed file only if it is under 25 MB; otherwise keep it local and report the size.
2. **LinkMu providers.** For every declaration whose last name component is `linkMu_of_sizes`, `linkMu_of_full`, `linkMu` or `linkMu_of_linkDIV`: is it in the export (full name), and which declarations mention it, split into "in the proof/body" and "in the statement only"?
3. **`omTied_retie_of_cube`.** Is it in the export, and which declarations mention it (proof/body vs statement only)?
4. **`GeneralHyps`, `GeneralHypU`, `GeneralHypV`.** Is each in the export as a declaration (match by last component, list full names)? If present, which declarations mention it (proof/body vs statement only)?

**Positive control (the run is VOID if it fails):** `riemannHypothesis` must be found to mention `rhOfAll` in its body (Main.lean:4: `theorem riemannHypothesis : RiemannHypothesis := rhOfAll`), and the name list must contain `riemannHypothesis`.

## Control (passed)

`riemannHypothesis` mentions `rhOfAll` in its body: **yes**. The name list contains `riemannHypothesis`: **yes**. The run is valid.

## The run

**COMPUTED.** One pass over Andrew Sutherland's export, shared with the `GeoTiedP` task. The compressed sha256 `61a8938a…` and the unpacked sha256 `5ea74b91…` both match the published values. 1,080,769,508 lines, 1,468,418 declarations, 10,163 s. Script: `results/export-names/scan_export.py`; raw output: `results/export-names/scan.json` (key `mentions`).

## 1. Name list

`results/export-names/names.txt.zst`: **1,468,418** names (the expected count), one per line, sorted. 7,366,339 bytes compressed (committed; it is under 25 MB), sha256 `daf668890024ecbccb20d13d8ccf076749b411c78bacac8b58ab3a1b3ffd38db`. Uncompressed: 77,248,763 bytes, sha256 `b0b486d79d078a2b85d461e6e7704bc1ecc39e2db0390f98c3ee68592fa2ab11`. To search: `zstd -dc names.txt.zst | grep NAME`.

One line per exported declaration record. Constructors and recursors of inductive types are not listed separately, and a mutual block is listed under its first type.

## 2. LinkMu providers

All four are in the export. All mentions are in bodies; none is statement-only.

| Declaration | In export | Mentioned in the body of |
|---|---|---|
| `Formalism.MainNotions.J.linkMu` | yes | `Formalism.MainNotions.J.linkMu_of_linkDIV`, `Formalism.SlopeId.linkMu_of_sizes` |
| `Formalism.SlopeId.linkMu_of_sizes` | yes | `Formalism.SlopeId.linkMu_of_full` |
| `Formalism.SlopeId.linkMu_of_full` | yes | `Formalism.L2.DIV.RestAll.bRest_all_alt` |
| `Formalism.MainNotions.J.linkMu_of_linkDIV` | yes | `UpperTheory.Top.topDesWin` |

**DERIVED.** The final path uses **two routes**, both ending in `J.linkMu`: `bRest_all_alt → linkMu_of_full → linkMu_of_sizes → J.linkMu`, and `topDesWin → J.linkMu_of_linkDIV → J.linkMu`. (`bRest_all_alt` and `topDesWin` are themselves in the export, so both are on the path of `Main`.)

## 3. `omTied_retie_of_cube`

In the export as `GlobalTheory.Mem.Top.Bl.TrueLocal.omTied_retie_of_cube`. Mentioned in the body of exactly one declaration: **`GlobalTheory.Mem.Top.Bl.TrueLocal.omTied_withTrue`**. No statement-only mentions.

## 4. `GeneralHyps`, `GeneralHypU`, `GeneralHypV`

**None of the three is in the export** under any full name: no name in the list contains any of them, even as a substring. They are defined in the source (`GeneralHyps.lean`, `FinitelyManyWithInfinitesimalCharacter.lean`, `SiegelWeilUnitaryConvergent2.lean`, all under `AbelianVarietyTheory/Definitions/GlobalTwisting/`). So they are **not on the dependency path of `Main`**, and there is no mention list to give.

## Limits

- The export holds what `Main` depends on. It says nothing about declarations outside that closure: "absent" means not used by `Main`, not "unused anywhere".
- "Mentions" means the constant appears in the declaration's type or value, not that a proof uses it in any deeper sense.
- Matching is by last name component, so same-named declarations in other namespaces would have been reported; only those above exist.

## Plain-language summary (facts only, by issue)

For **issue #5** (reader's map):
- The names of all 1,468,418 declarations on the dependency path can be searched as plain text (`results/export-names/names.txt.zst`).
- Both `LinkMu` routes are on the final path: `linkMu_of_full` (through `linkMu_of_sizes`), used by `bRest_all_alt`; and `J.linkMu_of_linkDIV`, used by `topDesWin`. Both end in `J.linkMu`.
- `omTied_retie_of_cube` is used by one declaration, `omTied_withTrue`.

For **issue #2** (import cone):
- `GeneralHyps`, `GeneralHypU` and `GeneralHypV` do not appear in the kernel export of what `Main` depends on, so the headline theorems do not use them. This is a statement about the proof terms, not about imports.

Source of the facts: Andrew Sutherland's export (`math.mit.edu/~drew/grh`, sha256 above), archive `homeowmorphism/riemann-hypothesis-original` at `4e8bb36`.

*Claude Code did the scan and wrote this note (26 Nov 2026) from `prompts/claude-code-prompt-2026-11-26h-export-questions.md`, which Claude in chat wrote.*
