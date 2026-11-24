# Codex: independent check of the new H8 file (24 Nov 2026, evening)

Written by Claude in chat. Rules: read and write only. No git, no builds, no `lake`, nothing in `C:\rhc`.
Source: pinned at `4e8bb36` of homeowmorphism/riemann-hypothesis-original (src tree = upstream `e50d098`).
Rubinstein v2: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf (H8 on p. 206; (III.315) and (III.330)).
Label every claim **READ**, **DERIVED** or **GUESS**. Either answer is fine. If the verdict should be "different", say so plainly.

## Why

Claude Code wrote `results/rubinstein-hypotheses/H8.lean` (theorem `RHX.h8_frame`, conclusion `Lnk.FrameF Fm CH`) and also judged it "same" as Rubinstein's H8 in the last section of `notes/batch1-audit.md`. The same model drafted and graded it. You are the second opinion. Do not read that audit section until you have written your own verdict.

## Tasks

1. **Statement vs (III.330).** Quote Rubinstein's H8 and compare it with what `FrameF` and `Frame_at` (QuadraticLogDerivCongr.lean:188–193, 258–260) state, clause by clause: the quantifiers (per translate vs per scale), the bound `(η + 4√e)·x^{C_H} ≤ 6`, the condition on R, the extra `eB ≤ 1/4`, and the inequality itself. Verdict: same, weaker or different.
2. **The two open GUESS items.** (a) Does `uFrame` in the source match his `sp_u`? Check against (III.315). (b) Does `sFrame` match his `s_u`, and `muDual`/`muMinDual` his `μ_CC`/`μ_CC^min`?
3. **No picking out.** Read the bodies of `frameF_of` (TopDensityNGeSixteen.lean:606), `frameRealF_of''` (:988), `latF` (QuadraticLogDerivCongr.lean:1338) and `matKF_of` (TopDensityNGeSixteen.lean:1348). Confirm that none of them obtains `Frame_at`, `FrameReal_at`, `FrameF` or `FrameRealF` by projecting it out of a hypothesis. Say where the actual inequality work happens (file:line).
4. **Premises.** For the four premises taken from `LinkMin.lean` (`NuFullF`, `J.MuRank`, `TuSize`, `RamRankF`), confirm the file's claim of where the headline route builds them (LinkMin.lean:701–719), and say whether those builders are real proofs.

Then, and only then, read the "H8 (new file)" section of `notes/batch1-audit.md` and say where you agree or disagree with it.

Write to `notes/h8-frame-check.md`. Do not edit any other file.
