# Nielsen's Appendix A demo, checked against the release

Author: Timothy Wesley Stone, with Claude (Opus, chat), 25 Nov 2026.
Credit: Jacob Gajek (@jgajek on X) pointed this out first, 25 Nov 2026.

Labels: **READ** means quoted from the source. **DERIVED** means our reading.

## What was checked

- Nielsen, "Invalidity of the Alpoge Proposed Proof of the Riemann Hypothesis" (PhilPapers record NIEIOT-2). Our copy: 17 pages, PDF creation date 23 Nov 2026 16:55 EST, sha256 `bbb50919d4269696abad1f5a5dd38cd8fd2bb498beedc9fac8255340e2ea6107`. Later versions may differ.
- The release, pinned at homeowmorphism/riemann-hypothesis-original @ `4e8bb36` (src tree identical to upstream `e50d098`).

## Her demo (READ, Appendix A, pp. 16-17)

Her appendix gives a short Lean file meant to reproduce "the structural pattern analyzed in this paper". Its final theorem is:

```lean
theorem claimed_rh (hRH : RiemannHypothesis) :
    (∃ b : Bundle, anyGeometry 0 ∧ b.model.height = targetFormula) ∧ RiemannHypothesis := by
  let b := buildBundle
  exact ⟨⟨b, valid_bundle_of_manufactured b⟩, hRH⟩
```

## The release's final theorem (READ)

```lean
theorem riemannHypothesis : RiemannHypothesis := rhOfAll
```

[Main.lean:4](https://github.com/homeowmorphism/riemann-hypothesis-original/blob/4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e/src/Main.lean#L4)

## Reading (DERIVED)

1. Her demo takes RH as an input (`hRH : RiemannHypothesis`) and hands that same input back as its RH conclusion. It is circular by construction. Her conclusion calls the release's comparison "Riemann to Riemann", and her demo is exactly that. But the release does not have that shape.
2. The release's theorem takes no inputs. Its statement is the bare type `RiemannHypothesis`, so there is nothing for RH to be passed in through.
3. `#print axioms` lists axioms, not a theorem's own hypotheses. So a clean `#print axioms claimed_rh` does not detect `hRH`. Her demo shows that a clean axiom list alone can hide an assumption sitting in the statement. That check does not apply to the release, whose statement has no assumptions.
4. What her demo does show correctly: a predicate that is always `True`, discharged by `trivial`, carries no information. That matches what we found for `anyGeometry`: the stamp is never read ([anygeometry-export-scan.md](anygeometry-export-scan.md)). It does not show the rest of the proof is circular.

## Limits

- We checked one version of her paper (the copy above), not the current PhilPapers version.
- We did not compile her snippet. The reading above is from its text.
- We did not run `#print axioms riemannHypothesis` ourselves (see [zeta-bridge.md](zeta-bridge.md)). The axiom check on the release is Sutherland's.

Related: [nielsen-rfl-check.md](nielsen-rfl-check.md) (her `rfl` claim), [zeta-bridge.md](zeta-bridge.md) (her zeta claim).
