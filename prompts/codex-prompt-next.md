# Codex task: three follow-ups on the Alpöge–Claude RH proof

**Repo:** `C:\Users\timmy\OneDrive\Desktop\XPostCode\My-RH-proof`. Read `README.md`, `notes/RH-proof-handoff.md` (Addenda 34–40) and `results/common-period-map/COMMON-PERIOD-MAP.md` first.

**Pinned source:** `homeowmorphism/riemann-hypothesis-original` at `4e8bb36` (src tree `24df20b`, same as upstream `e50d098`). A sparse checkout with 705 modules already built from source lives in `C:\rhc`. You may read it.

**Labels.** Mark every claim READ (seen in source or a document, with file:line or page), DERIVED (our reasoning) or COMPILED (Lean ran). Never upgrade a label.

**Builds.**
- Never run two Lean builds at once.
- Never run `lake exe cache get` (the project cache).
- Check that nothing else is building in `C:\rhc` before you start.
- If you must build, use the same settings as the successful 2-thread retry in `logs/build-retry.log`.
- Only build if the new file's import closure is already inside the 705 modules in `results/common-period-map/closure-files.txt`. Otherwise draft the file and stop.

**Do not** change `CommonPeriodMap.lean`, `CommonPeriodMap2.lean` or anything under `src/`.

## Part A (short): how the proof handles the primes 2 and 3

The Lean theorem that certifies the kernel condition, `bHyps_of_beStd` (SatakeParameters/StandardSeriesBConditionsLargePrime.lean:145), assumes `5 ≤ l`. The gain structure `Std` (FormalGroupSystem.lean) has `five_le : 5 ≤ p`. Rubinstein's worked example (v2 §III.12) uses ℓ = 3.

1. On the headline path (`LinkG`, `LinkG_at` in GlobalTheoremInputs.lean:122, `loG`/`flG`, `InertK`), find exactly what happens at inert primes p = 2 and p = 3, and at any p < 5. Are they excluded from the gain, charged to an error term, or covered by a separate theorem? Give file:line for each.
2. What does this cost in the final budget, and is the cost of lower order? Point to where that is shown.
3. Can 2 or 3 actually be inert for the host fields the headline uses?

**Output:** `notes/small-primes-check.md`. One page, picture first: which primes get the "bonus", which don't, and who pays.

## Part B (main): the classical dictionary for the period map

**Background (READ, Addendum 36).** `S.Draft.SData` (CuspSpanNormBounds/DataS.lean) is an abstract slot holding `HH`, `Cu`, `Pu`, `volN`, `volH` and `Term`/`aTerm`. `exists_sStage` (ExistsSStageUnconditional.lean:128) fills it with:
- `HH = ℂ^Dall`;
- `Pu` = a supplied map `P` composed with `colEq`;
- `volN = volH = 1`;
- an empty term expansion (`aTerm = 0`).

Other call sites pass `P = 0`. On the headline path, `LinkS`'s diagonal bound rules out `Pu = 0`. `BesselId` ties `Pu`'s matrix coefficients to the arithmetic numbers `what₂.Bu`.

1. For the family that `topDesWin` actually uses (DesWin.lean:11 → `ExistsFamPOfKits` / design existence), find where each `D7` is built and which construction supplies `D.s`. What is the `P` there: a genuine map, or a placeholder? Where are `LinkS` and `BesselId` proved for that same `P`?
2. Trace `what₂.Bu` to its definition: `BuDef`, `perCol`, `zeC` (DataRows.lean around :35 and :217), and the level identity in ZetaProductPairs.lean:136–147. In classical terms, what are these numbers? Candidates are Bessel or Gan–Gross–Prasad periods of theta lifts and per-column periods of the chain. Say which, with the evidence.
3. With `volN = volH = 1`, `c0 = 1/dimPi`. Is that the Rallis inner-product normalization, or a stand-in? Where does the real Rallis constant enter (if it does): `rallis_inner_product_convergent_of_literature`, EveryCharacterOfLiteratureOfVWin.lean:485?
4. Compare with Adriazola's manuscript (github.com/jimjamzola/RH-Alpoge-Reconstruction, `manuscript/sec14_bessel.tex`, Hypotheses H-dict, H-rat and H-see, all listed as open in his §19). Also compare with Rubinstein v2 O25(e), p. 185. For each, say what the Lean source settles and what stays open.

**Output:** `notes/period-map-classical.md`. Include a dictionary table with three columns: Lean object, classical object, status (READ / DERIVED / open).

## Part C (only if A and B are done): Rubinstein's H1 and H6 as Lean statements

For each of H1 (`DIV`, MeanBoundSecondForm.lean:118, `WordFacts` RecBridge.lean:128) and H6 (`OneMapIntoCC`, `SlopesN_at` QuadraticLogDerivCongr.lean:181):

1. Find the exact statement the headline proof supplies for its family.
2. Draft a bridge file in the style of `CommonPeriodMap2.lean`: from the headline's own premises, every family member eventually satisfies H_i.

Name the files `results/rubinstein-hypotheses/H1.lean` and `H6.lean`, and add a short README. Compile only under the build rules above.

When you are done, commit with clear messages and push. Report what you finished, what you skipped, and why.
