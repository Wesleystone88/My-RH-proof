# Codex: "follow the zeta" (24 Nov 2026, task 4)

Rules: read and write only. No git, no builds, nothing in `C:\rhc`.
Source: pinned at `4e8bb36`. Label every claim **READ**, **DERIVED** or **GUESS**.
Either answer is fine. Report what the source says, even if it supports Nielsen.

## The claim being tested (pre-registered)

Nielsen (X, 23 Nov): the code "assigns a bundle to hold zeta, and that bundle holds content that matches the Riemann hypothesis. That isn't proving anything."

- **If she is right,** the link between Mathlib's `riemannZeta` / `RiemannHypothesis` and the proof's own objects is supplied by definition: `rfl`, `HEq.rfl`, a copied structure field, or a hypothesis that is never proved.
- **If she is wrong,** that link is a theorem with a real proof term.

## Tasks

1. **The statement.** Quote the statement of `riemannHypothesis` in `src/Main.lean`. Confirm it is Mathlib's `RiemannHypothesis` with no extra hypotheses.

2. **The bridge.** Follow `riemannHypothesis → rhOfAll → allChi → everyCharacter`. Find the exact declaration(s) where a statement about the project's characters or L-functions turns into a statement about Mathlib's `riemannZeta`.
   - Quote each one and say whether it comes from Mathlib or the project.
   - For each step, say whether it is proved by a real proof term or by `rfl`, a definition, or a copied field.

3. **The bundle.** Find the structure(s) that best fit "a bundle assigned to hold zeta". These are fields mentioning `riemannZeta`, `LSeries`, zero-freeness, or a zero-free region. For each RH-relevant field, say how the headline proof fills it: a real proof, or by construction.

4. **The inventory.** List every declaration on the route from `riemannHypothesis` (as traced in `notes/h-rat-verify.md`) that mentions `riemannZeta` or `RiemannHypothesis`.

5. **The verdict.** End with one paragraph: does any step match the "if she is right" pattern above? Name it with file:line, or say none was found and how far you looked.

Write to `notes/zeta-bridge.md`.
