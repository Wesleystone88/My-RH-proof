# Claude Code: next tasks (24 Nov 2026, afternoon)

Written by Claude in chat. Do the tasks in order. Report after each one.

Standing rules: one Lean process at a time, never two. Never run `lake exe cache get` for the project. Stop if C: has less than 25 GB free. No new module builds without asking Timmy first. Do not commit unfinished Codex files.

## 1. Make the READMEs match the audits (no Lean)

Rubinstein and Adriazola now have issues pointing at this repo, so the READMEs must say exactly what the audits say.

Sources of truth: `notes/batch1-audit.md`, `notes/batch2-audit.md`, `notes/zeta-bridge.md`.

- Totals across all 13: **same** H1, H2, H3, H4, H5, H6, H9 (7); **weaker** H0, H12 (2); **different** H7, H8, H10, H11 (4). Nothing anywhere should say 8 match, or imply H1, H2, H3, H6, H9 were unaudited.
- Add the "picking out" caveat in plain words: in H1, H2, H3, H9, H6(i), (8a) and (8b) the conclusion is one conjunct of the premise `LinkDIV`, so these files show where each hypothesis sits in the code, not a new proof of it. Only H6(ii)(iii) and (8c) go through real source theorems.
- H8: `CommonPeriodMap2.lean` shows one map `Bk` carries all three conditions, because the source states all three for that object. It does not state Rubinstein's inequality (III.330), and it does not connect his three maps to `Bk`. The source states (III.330) as `Frame_at` (QuadraticLogDerivCongr.lean:188–193) and `FrameF` (:258).
- Fix any line that says the files "answer" Rubinstein's H8 question, or that the family satisfies "all three of Rubinstein's H8 conditions" without that qualification. Check at least: `README.md` (lines ~21, ~23, ~40), `results/rubinstein-hypotheses/README.md`, `results/common-period-map/COMMON-PERIOD-MAP.md`.
- Add one row or line for `notes/zeta-bridge.md` (the test of Nielsen's zeta claim) and `notes/batch1-audit.md`.
- Keep the edits minimal. Do not rewrite sections that are already correct.

Commit and push with this prompt file. Message: "READMEs: match the batch 1 and 2 audits (7 same, 2 weaker, 4 different); H8 qualified". Say in the commit body that Claude Code edited the READMEs and Claude in chat wrote the prompt.

## 2. A new H8 file that states Rubinstein's inequality (Lean)

Goal: a theorem whose conclusion is `Frame_at` (Rubinstein's III.330) for the headline family, with his constants η_u = 5x^{−C_H} + 3√α_ram and e_u = 2e_0 as far as the source gives them.

- Read `notes/batch1-audit.md` lines ~78–90 first. The source route is `frameReal_at_of` (TopDensityNGeSixteen.lean:679) then `frame_at_of` (:538), and `FrameF` (QuadraticLogDerivCongr.lean:258).
- **No picking out.** Do not take a premise that already contains `Frame_at`, `FrameReal_at` or `FrameF` as one of its conjuncts. The conclusion must come through `frame_at_of` (or the source's own family-level theorem that calls it). If that is impossible with premises the headline route supplies, stop and report why instead of writing a picked-out version.
- List every premise and say where the headline route supplies it (file:line), as in the other H files.
- Write to `results/rubinstein-hypotheses/H8.lean`, theorem `RHX.h8_frame`, ending with `#print axioms RHX.h8_frame`.
- Compile only with `lake env lean` in the existing pinned closure, and only if every import is already in `results/common-period-map/closure-files.txt` (or `h12-extra-closure.txt`). If something is missing, stop and list the missing modules. Do not build them without asking.
- Save the output as `results/rubinstein-hypotheses/H8.out`.
- Then compare the conclusion with (III.330) the same way `notes/batch1-audit.md` does, and give a verdict: same, weaker or different. Put it in a short section at the end of `notes/batch1-audit.md`, headed "H8 (new file)".
- If it compiles with only `propext`, `Classical.choice`, `Quot.sound`: add it to the folder README table, then commit and push with the message "H8.lean: Rubinstein's inequality (III.330) via frame_at_of". If not: commit nothing and report.

## 3. Report

A short table: task, result, commit hash (or "not committed" and why).
