# JackyReaps' "Continuum Gap" countermodel, read against its own model

Author: Timothy Wesley Stone, with Claude (Opus, chat), 25 Nov 2026.
Source checked: [jackyreaps/X-files @ `433c7c6`](https://github.com/jackyreaps/X-files/tree/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis) (commit of 25 Nov 2026, 09:40 CST), folder `riemann-hypothesis/`.

Labels: **READ** means quoted from the source. **DERIVED** means our reading.

## What he now claims (READ, README.md:6-8)

- A `sorry`-free Lean theorem, `Disproof.challenge_lemma_false`, showing that the interfaces he extracted from archive commit `40e56bab` "do not logically imply the claimed theta-lift multiplicity bound".
- He does **not** claim Mathlib's `RiemannHypothesis` is false, and does **not** dispute that Lean's kernel accepted a term of that type. His claim is about "the extracted/modeled live-path boundary interface".
- He lists "direct `.olean` binding" as open: his file models the archive's predicates "without importing" the archive.

## What his model puts in place of the archive (READ, ThetaConstraints.lean)

| Archive part (his label) | His stand-in | Line |
|---|---|---|
| `ThetaIntegralsAgree` | `def … : Prop := True` | [89](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L89) |
| `LocalMatching` | `def … : Prop := True` | [91](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L91) |
| `CovolumeBoundOfX` | `∃ C0 : ℝ, 0 ≤ C0 ∧ surviving ≤ C0` | [98-99](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L98-L99) |
| `BoundAtTwoThreeFamilyFonAlt` | `def … : Prop := True` | [107](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L107) |
| `VWin` | `def … : Prop := True` | [109](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L109) |
| `GreenOfRegular` | `def … : Prop := True` | [111](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L111) |
| `DefiniteSideCondition` | `def … : Prop := True` | [113](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L113) |
| the two literature results | `def … : Prop := True` | [116-117](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L116-L117) |
| slope, relative-trace, character-average constraints | record fields of type `Prop` (a statement slot, not a proof) | [147-153](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/ThetaConstraints.lean#L147-L153) |

His witness `fakeMultiplicity` ([Disproof.lean:42-62](https://github.com/jackyreaps/X-files/blob/433c7c64691f9c2457bbe4cfe2e8d860baef3a60/riemann-hypothesis/Disproof.lean#L42-L62)) fills these with `trivial`, `⟨100, by norm_num, le_rfl⟩`, and `True`.

## Reading (DERIVED)

1. Every archive constraint in his model is either `True`, a statement slot that asks for no proof, or the covolume bound.
2. The covolume bound as he wrote it holds for every real number: take `C0 = max(surviving, 0)`. So it rules nothing out.
3. So his model has no constraint that could bound the surviving mass, and a countermodel is guaranteed. `challenge_lemma_false` shows that his model is empty, not that the archive's interfaces are.
4. This is the same move he criticizes in `anyGeometry` (a requirement replaced by `True`), applied to the parts of the archive that do the work.
5. Whether the countermodel says anything about the real archive depends on his open item: binding to the real definitions. Until his witness is checked against the real predicates, it says nothing about them.

## Where he and we agree

His "pass-through transport" finding (the `geo` field is filled by `anyGeometry` and carried along without being opened; `lam` carries the content) matches our kernel-level result in [anygeometry-export-scan.md](anygeometry-export-scan.md).

## Limits

- We read his files. We did not build his repo.
- He extracted from archive commit `40e56bab`; our pin is `4e8bb36` (src = upstream `e50d098`). We have not yet matched his names (`CovolumeBoundOfX`, `GlobalTheory.CovTop`, `BoundAtTwoThreeFamilyFonAlt`, `VWin`, …) to declarations at our pin. Our local `rh-source` clone is partial, so a search there that finds nothing is not evidence those names are missing.
- Point 2 is DERIVED; a one-line Lean check is queued (`prompts/claude-code-prompt-2026-11-25e.md`).
