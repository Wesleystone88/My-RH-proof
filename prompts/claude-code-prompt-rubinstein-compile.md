# Claude Code task: compile the Rubinstein H-files (23 Nov 2026)

Saved verbatim as given.

In My-RH-proof:

1. Compile results\rubinstein-hypotheses\H1.lean, H2.lean, H3.lean, H6.lean and H9.lean the same
   way as CommonPeriodMap2.lean: copy them into C:\rhc, run `lake env lean` on each, and save the
   outputs as H1.out and so on next to the .lean files. Check that nothing else is building first.
   Mark each file that shows only propext, Classical.choice and Quot.sound as COMPILED in
   results\rubinstein-hypotheses\README.md and the main README. If one fails, show me the error
   and don't change its statement.
2. Codex is drafting more files in results\rubinstein-hypotheses\ and notes\ right now, but it will
   not commit. When it finishes, commit its new files too, without editing them. Later I'll ask
   you to compile that batch.
3. Save these two prompts (this one and the Codex one) in prompts\ for transparency.
4. Commit with clear messages and push.
