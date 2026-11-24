# Batch 1 audit (24 Nov 2026, afternoon) — for Codex or Claude Code

Rules: read and write only. No builds, no `lake`, nothing in `C:\rhc`. This is a reading task; no Lean needs to run.
If you are Codex: no git. If you are Claude Code: no git until the last step below.
Source: Alpöge's Lean proof pinned at `4e8bb36` of homeowmorphism/riemann-hypothesis-original (src tree = upstream `e50d098`).
Rubinstein: version 2 of the exposition, https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf (hypotheses on pp. 203–214).
Label every claim **READ** (quoted from a file), **DERIVED** (our reasoning) or **GUESS**.
Either answer is fine for every hypothesis. If a statement does not match, say so plainly.

## Why

`notes/batch2-audit.md` compared H0, H4, H5, H7, H10, H11, H12 with Rubinstein's wording and found only H4 and H5 match. The batch 1 files were never audited that way. Our public posts said "8 match"; that count is unchecked for the files below.

## Task

Do the same audit, in the same format as `notes/batch2-audit.md`, for:

- `results/rubinstein-hypotheses/H1.lean`
- `results/rubinstein-hypotheses/H2.lean`
- `results/rubinstein-hypotheses/H3.lean`
- `results/rubinstein-hypotheses/H6.lean`
- `results/rubinstein-hypotheses/H9.lean`
- `results/common-period-map/CommonPeriodMap2.lean` (our H8)

For each one:

1. Quote Rubinstein's statement (page and equation number).
2. Say what the Lean conclusion gives, clause by clause, with file:line.
3. Verdict: **same**, **weaker** or **different**, using the batch 2 definitions. Say which clauses are missing, changed or extra.
4. Note any premise that does the work of the conclusion (a premise that already states it).

End with a one-line summary table: hypothesis, verdict, one-sentence reason.

Write to `notes/batch1-audit.md`. Do not edit any other file.

## Last step (Claude Code only)

Commit and push `notes/batch1-audit.md` and this prompt file, with the message "Batch 1 audit: H1, H2, H3, H6, H8, H9 against Rubinstein v2" and a line saying who wrote the audit. Then report the summary table.
