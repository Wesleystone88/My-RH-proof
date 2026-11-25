# Codex: next two tasks (24 Nov 2026, evening)

Written by Claude in chat. Rules: read and write only. No git, no builds, no `lake`, nothing in `C:\rhc`.
Source: pinned at `4e8bb36` of homeowmorphism/riemann-hypothesis-original (src tree = upstream `e50d098`).
Rubinstein v2: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf (hypotheses on pp. 203–214).
Label every claim **READ**, **DERIVED** or **GUESS**. Either answer is fine for every item. "Not found" is a valid result.
Do the tasks in order. Each writes one new file; do not edit any other file.

## 1. Hunt for the source's own statement of the five non-matching hypotheses

Background: our H8 file was "different" until we found that the source itself states Rubinstein's inequality (III.330), as `Frame_at` (QuadraticLogDerivCongr.lean:188) and `FrameF` (:258), proved via `frame_at_of`. See `notes/batch1-audit.md` and `notes/h8-frame-check.md`.

Do the same search for the five that still do not match: **H0, H7, H10, H11, H12**. Their current files and the reasons they do not match are in `results/rubinstein-hypotheses/` and `notes/batch2-audit.md`.

For each one:
1. Quote Rubinstein's statement (page, equation).
2. Search the pinned source for a definition or theorem whose statement has his form (not ours). Give every serious candidate with file:line, and quote it.
3. Grade the best candidate against his statement: same, weaker or different, clause by clause, using the same standard as `notes/h8-frame-check.md` (whole statement, including scope: fixed scale vs family, eventual thresholds, parameter ranges).
4. Say how the source proves it: which theorem, and whether that theorem is reached on the headline route (give the chain or say where you lose it). Say whether the conclusion would be picked out of a premise or derived.
5. Feasibility for a new file: list the imports it would need, and whether each module appears in `results/common-period-map/closure-files.txt` or `results/rubinstein-hypotheses/h12-extra-closure.txt`.

End with a table: hypothesis, best source candidate, grade, picked out or derived, feasible in current closure (yes/no).

Write to `notes/source-statements-hunt.md`.

## 2. Where the real proof of the picked-out hypotheses lives

Background: `notes/batch1-audit.md` found that H1, H2, H3, H9, H6(i), (8a) and (8b) are each one conjunct of the premise `LinkDIV`, so our files only locate them. `notes/divinputs-trace.md` traced how the headline route builds `LinkDIV` down to `divClausesR_of` (ConstantGeTwentyEight.lean:184) and its input `DivInputsR`.

For each of those seven items:
1. Name the conjunct of `LinkDIV_at` (GlobalTheoremInputs.lean:77) that states it.
2. Find the exact place in `divClausesR_of` (or whatever the headline route actually calls) where that conjunct is proved. Give file:line and the lemmas it calls.
3. List which `DivInputsR` fields and which estimates that proof depends on, and say for each whether it is a real estimate or holds by construction (`rfl`, `HEq.rfl`, a copied field), consistent with `notes/divinputs-trace.md` and `notes/nielsen-rfl-check.md`. If you disagree with either note, say so.
4. One plain sentence: "Rubinstein's Hn is proved in the code by …".

End with a table: hypothesis, `LinkDIV` conjunct, proving lemma (file:line), main estimates, any by-construction step.

Write to `notes/linkdiv-proofs.md`.
