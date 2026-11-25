# Which hypotheses of the engine are essential? (pre-registered)

## Pre-registered rule (written 25 Nov 2026 before `drop_one.py` was run)

From `prompts/claude-code-prompt-2026-11-25b.md`, task 3:

> A hypothesis is **ESSENTIAL** if numbers are found that satisfy all the other hypotheses but violate the conclusion; otherwise **UNKNOWN** (not shown redundant).

Consequences fixed in advance:

- "Found" means an explicit instance, printed, and re-checked in exact rational arithmetic (or with a stated margin when a real exponent is involved).
- Failing to find a counterexample proves nothing about redundancy. It is reported as UNKNOWN together with what was tried.
- The instance is small (few words, few translates, small finite types). A counterexample on a small instance is a real counterexample to the dropped-hypothesis version of the statement, but only if every other hypothesis is verified on it.
- Guess to be tested, not assumed: the floor (divisibility, (Dv)) and the ceiling (frame / slope inequality, (SI)) are both essential.

*(Results are added below after the run.)*

## What was run  (COMPUTED)

`drop_one.py` (Python 3.10, numpy/scipy HiGHS, mpmath at 60 digits); full output `drop_one.out`, machine-readable `drop_one_results.json` (it contains each counterexample's global constants and every unknown). Runtime about 30 s.

**Model (DERIVED from the source, checked by the sanity test below).** After `ch_top_main_eq` the conclusion is `ASK(u) − Main(u) ≤ B_final := x^{CErr·ε} · errorBracketSizeWindows(…)`; `each_unit_bound_statement` proves the sharper `ASK − Main ≤ ErrX5at` ([QuotientSlopeBoundsWith.lean:45](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L45)). The instance: one translate, 1 or 2 words with weights d = 1, `m = f = |Top| = |H| = 1`, `T2 = ∅`. For fixed global constants and fixed `HH, del, η, e` and `uF` the clauses of `SizeData₂` are linear in the remaining reals, so "all other hypotheses hold and `ASK − Main > B_final`" is a linear program (the word attaining `uF` and the on/off state of the `SlopeIneq` guard are enumerated). The base instance has `x = 800, ε = 1, a = 8000, k = 800, K = 0.2` and satisfies every global conjunct of `ErrWindows`, `BNBoundsU`, `LargeX`.

**Sanity check (passed before anything else was believed).** With all hypotheses the LP maximum of `ASK − Main` is at most `4.6%` of `ErrX5at` in all 12 structural variants (≈ 3.4·10⁵ against 7.4·10⁶); never above, as Lean's theorem requires.

**Certificates.** ESSENTIAL is declared only when the LP finds a point with `ASK − Main ≥ B_final` (or ≥ 2·B_final+1 if unbounded) and that point is **re-checked row by row in mpmath**; the worst row residual is stored in the JSON (all ≤ 0, with margin 10⁻⁶ relative to the row scale). For each hypothesis one clause or conjunct is dropped at a time, the rest stay required; "whole" lines drop the entire hypothesis.

**Two columns matter.** Beating `B_final` is a counterexample to `ch_top`. Beating only `ErrX5at` is a counterexample to the sharper intermediate bound but not to `ch_top` (the final bound has `x^{CErr ε}` slack); those are reported UNKNOWN for `ch_top` with a note.

## Result

Every hypothesis of `ch_top`, as a unit (a unit is ESSENTIAL when dropping it, or one conjunct of it, gives a verified counterexample):

| Hypothesis | Verdict | Which part carried it |
|---|---|---|
| h1 `IdentU` | **UNKNOWN** | not tested: it identifies the abstract record with the arithmetic (needs an `ArithData`) |
| h2.1 `HidaSetting` | **ESSENTIAL (whole only)** | dropping the whole clause: `d = 0` (Lean's `0/0 = 0` makes `s = 0`) together with `muN > muMaxN`. No single conjunct was found essential. This is a junk-value counterexample |
| h2.2 `DIV` = (Dv) | **ESSENTIAL** | unbounded `ASK − Main` |
| h2.3 `EComp5` = (E) | **ESSENTIAL** | the upper side (`Ee ≤ …`); the lower side UNKNOWN |
| h2.4 `HComp` | UNKNOWN | no counterexample with 2 words; sharp-bound ratio 0.046 |
| h2.5 `Count5` = (Ct) | **ESSENTIAL** | the lower bound on `log T` (the paper's (Ct)) and the upper bound `log T ≤ cCount·m·L` (not in the paper's seven); the third conjunct UNKNOWN |
| h2.6 `Slopes` = (Sl) | **ESSENTIAL** | the lower bound `−SL ≤ muM`; the upper bound `muMaxM ≤ SL` UNKNOWN |
| h2.7 `QuotientSlopeBoundsWith` = (G) | **ESSENTIAL** | the lower conjunct `muM + Ga + Fo − Ee − Lo5 ≤ muN`; the upper conjunct UNKNOWN |
| h2.8 `LossBounds` = (L) | **ESSENTIAL** | both `ASK − Ga ≤ LoP` and `IO ≤ LoP` |
| h2.9 `SlopeIneq` = (SI) | **ESSENTIAL** | unbounded |
| h2.10 `HHBound` | **ESSENTIAL** | `s − muMinCC ≤ HH` and `0 < HH` (each makes the guard of `SlopeIneq` false when dropped); the cap `HH ≤ x^{cHH}·b` only breaks the sharp bound |
| h2.11 `FParams` | **ESSENTIAL** | `0 ≤ del`, `0 ≤ η`, `0 ≤ e`, `e ≤ eBar` (each switches off `SlopeIneq`); `del ≤ delBar` UNKNOWN; `η ≤ etaBar` only breaks the sharp bound |
| h3 `ErrWindows` | **ESSENTIAL** | `La ≤ 2x^ε` and `ConstsBound` (`c ≤ K`) each alone; 26 other conjuncts UNKNOWN |
| h4 `BNBoundsU` | **ESSENTIAL** | both `B0 ≤ …` and `Nc ≤ …` (after extending the grid to 10¹⁶) |
| h5 `LargeX` | **ESSENTIAL** | `KBig ≤ x^ε` (`log x ≤ x^ε` UNKNOWN) |

Totals: 31 of the 84 lines are ESSENTIAL (a line is a hypothesis, a clause, or one conjunct); the table above folds them into 15 hypotheses: **13 ESSENTIAL, 2 UNKNOWN** (`IdentU`, `HComp`). The paper's seven bounds (G), (Dv), (Ct), (E), (Sl), (SI), (L) all came out ESSENTIAL. Each ESSENTIAL line has its instance and unknowns in `drop_one_results.json` (key `counterexample`).

Clauses with **no** counterpart in the paper's seven came out UNKNOWN or junk-only: `HComp`, the lower side of `EComp5`, the upper conjuncts of `Slopes` and of `QuotientSlopeBoundsWith`, the third conjunct of `Count5`, and every single conjunct of `HidaSetting`. The one source clause essential beyond the seven is the upper half of `Count5` (and the size windows h3–h5, which the paper folds into "Remark 2.4").

## Drivers: floor and ceiling

The floor, divisibility `DIV` / (Dv), and the ceiling, the slope inequality `SlopeIneq` / (SI), **both came out ESSENTIAL** (unbounded gap when either is dropped), as guessed; but they are not alone: every one of the paper's seven is essential in this model, and so are the loss bounds (L). `DIV` bounds `muCC` from above, `SlopeIneq` from below, and the pair is what caps `Fo` and then `Ga`; (G), (Sl), (Ct), (E) and (L) are the links through which `ASK` reaches `Ga`. The pair is therefore the core of the chain, not the only load-bearing pieces. Two cheap ways to break `SlopeIneq` are worth noting: its guard (`0 ≤ del < 1`, `0 ≤ η`, `e ≤ 1/4`, `s − muMinCC ≤ HH`, `0 < HH`) makes it vacuous outside the range, which is why `FParams` and `HHBound` are essential too.

## Limits (all stated, none hidden)

- **UNKNOWN is not redundant.** The instance is tiny (one translate, ≤ 2 words, `m = f = 1`, `|Top| = |H| = 1`, `T2 = ∅`) and the search is a finite grid of mutations (decade factors from 10⁻⁸ to 10⁸, a few structural variants). A larger instance could expose more. In particular `HComp` needs two words and was tested only with two equal-weight words.
- The two clauses that look essential only through Lean's junk values (`0 < d` with `d = 0`, `0 < f`) are separate cases; `HidaSetting` is reported ESSENTIAL as a whole through `d = 0`, not through any real-valued violation.
- `h1 IdentU` is the identification of the abstract record with `ArithData`; no numeric test was attempted. This is not a claim that it is redundant, it is not tested.
- `nT ≥ 1`, `m ≤ x^{1/2+ε/2}` and the case `|Top| > 1` are outside the model (not tried).
- The counterexamples violate the *abstract* statement with a hypothesis removed. They do not touch the real proof of RH, in which every hypothesis is proved for the concrete data.

*Written by Claude Code (25 Nov 2026) from `prompts/claude-code-prompt-2026-11-25b.md`, which Claude in chat wrote.*
