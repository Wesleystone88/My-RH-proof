# Claude Code: chat notes + JackyReaps binding test (25 Nov 2026)

Written by Claude in chat. Run this **after** `prompts/claude-code-prompt-2026-11-25b.md`.
Rules: one Lean process at a time; never `lake exe cache get` for the project; stop if C: has less than 25 GB free; no new module builds without asking Timmy. Label every claim READ, DERIVED, COMPUTED, COMPILED or GUESS.
Do not run git in `../rh-source`: it is a partial clone (blob:none, sparse), and `git grep HEAD` there tries to download blobs. Search source text in the full pinned tree you build from, with plain grep or ripgrep.

## Tasks

1. **Commit the chat notes.** `notes/nielsen-appendix-check.md` and `notes/jackyreaps-model-check.md` were written in chat and are finished. Commit them now, saying Claude in chat wrote them.

2. **Match his names to the real archive (READ).** JackyReaps' model ([X-files @ 433c7c6](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean)) replaces archive predicates with stand-ins (see the table in `notes/jackyreaps-model-check.md`). For each name below, find the real declaration at our pin and quote its statement with a pinned link (homeowmorphism/riemann-hypothesis-original @ 4e8bb36):
   `ThetaIntegralsAgree`, `LocalMatching`, `CovolumeBoundOfX` (his namespace `GlobalTheory.CovTop`), `BoundAtTwoThreeFamilyFonAlt`, `VWin`, `green_of_regular`, `DefiniteSideCondition`, `theoremK_head2`, `every_character_of_green_v_win`, `nonempty_hyps_definite_side_of_closed_bound`.
   Per name, mark exactly one: **SAME** (his stand-in is equivalent), **WEAKER IN HIS MODEL** (the real one says more than his stand-in), or **NOT FOUND AT OUR PIN** (he used archive commit `40e56bab`; say so, do not guess a match). Write `notes/jackyreaps-binding.md`.

3. **One-line vacuity check (COMPILED).** Write `results/jackyreaps-check/Vacuity.lean`:
   ```lean
   theorem RHX.covolume_model_vacuous (s : ℝ) : ∃ C0 : ℝ, 0 ≤ C0 ∧ s ≤ C0 :=
     ⟨max s 0, le_max_right _ _, le_max_left _ _⟩
   #print axioms RHX.covolume_model_vacuous
   ```
   Import only Mathlib modules already built for our closure (the same Mathlib imports `results/rubinstein-hypotheses/H8.lean` uses are fine). Compile with `lake env lean`; if an import is not built, stop. Save the output as `Vacuity.out`.

**Pre-registered verdict** (write it at the top of `notes/jackyreaps-binding.md` before task 2): his countermodel carries over to the real archive only if every real predicate is no stronger than his stand-in. If any name comes out WEAKER IN HIS MODEL, `challenge_lemma_false` says nothing about the real archive until his witness is shown to satisfy the real predicate.

## Last step

Commit and push `notes/jackyreaps-binding.md`, `results/jackyreaps-check/` and this prompt, saying Claude Code wrote the results and Claude in chat wrote the prompt. Report the per-name table and the axioms line of `Vacuity.out`.
