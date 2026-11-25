# Does the engine reach the formula for h? (pre-registered)

## Pre-registered outcomes (written 25 Nov 2026 before `HExcision.lean` was run)

Copied from `prompts/claude-code-prompt-2026-11-25b.md`, task 2b.

- **PASS** = `hExpl6` is not reached from `ch_top` (the engine works for every h that satisfies its hypotheses; the formula for h enters only where the inequalities `P ≤ h` and `μ + h − Fo ≤ MAIN + error` are proved).
- **FINDING** = reached: print the shortest path and name the hypothesis or definition it goes through. If the path runs only through the type of a hypothesis (for example a field like `h_eq` that the proof never projects), report it as **FINDING (through a type)** and say so; do not reclassify it as PASS.

Setup, also fixed in advance:

- Root: `Deduction.ch_top` (`ChTop.lean:37`). Targets: any constant whose last name component is `hExpl6`; separately, `setDiv`.
- Positive control: starting from `sExpl` (`LocalQuadraticParts.lean:350`) the walker must reach `hExpl6`. If the control fails, the result is void.
- First output line: whether the module defining `hExpl6` is loaded and the full name found. If it is not loaded, the check means nothing and the run stops.

*(Results are added below after the run.)*

## Result: **PASS**

**COMPILED.** `HExcision.lean` compiled from `C:\rhc` with `lake env lean` (Lean 4.33.1, 1 minute); raw output in `HExcision.out`. `Engine.lean` compiled too (6 minutes, cold Mathlib import); its output `Engine.out` is the single line `'RHX.engine_M' depends on axioms: [propext, Classical.choice, Quot.sound]`.

First line of the output (as the prompt required): the module defining `hExpl6`, `Formalism.LocalRingCardinality.KernelPlaceMeanBound`, **is loaded**; the constant found is `Formalism.BasicNotions.DV.hExpl6` (the only constant with that last component). 11,369 modules were loaded.

| Walk | Result | Constants visited |
|---|---|---|
| `Deduction.ch_top` → any `…hExpl6` | **not reached** | 17,403 |
| `Deduction.ch_top` → any `…setDiv` | not reached | 17,403 |
| positive control `sExpl` → `hExpl6` | **reached**, path `LocalQuadraticParts.sExpl → DV.hExpl6` | 17 |

`ch_top` reaches 17,403 constants in total (types and values together); the walk exhausted all of them without meeting `hExpl6`. The positive control passes, so the walker does find `hExpl6` when it is there, and the PASS is not void.

**Verdict: PASS** under the pre-registered definition: `hExpl6` is not reached from `ch_top`.

## What this does and does not say

- **DERIVED, expected by construction.** `hExpl6` is defined on the concrete record `D7` (`KernelPlaceMeanBound.lean:25`), while `ch_top` is stated for the abstract record `Data`, in which `h` is just a field. So a PASS is what the types predict; the walk confirms that nothing in the type or the proof of `ch_top` or anything it uses mentions the formula. The informative part is the positive control: it shows the walker would have caught a dependence.
- **No `setDiv` constant exists** in the loaded environment under that last name (the first line of the output lists none; the exported name is `oAt_setDiv`, which does not end in `setDiv`). So the second target is vacuous, not a second PASS. I did not search for other spellings.
- **Limit (stated in the prompt).** The walk is constant-reachability on types and on values. It says that `hExpl6` is not mentioned anywhere under `ch_top`; for a FINDING it would not have said which fields of a hypothesis the proof projects. It does not say anything about the *rest* of the proof: the formula for h enters where `h` is *proved* to satisfy `DIV` and `SlopeIneq` for the concrete record, which is outside `ch_top`.
