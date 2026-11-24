import Formalism.SharpRestriction.GlobalTheoremInputs

/-!
# Rubinstein H1 on the selected family

READ. The seventh conjunct of `LinkDIV_at` is the wordwise estimate in
`WordFacts` (GlobalTheoremInputs.lean:82 and RecBridge.lean:128).
DERIVED. One pair of constants serves every member and word above the threshold.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h1_pairing_size {eps : ℝ} (Fm : FamP eps) {Cabs CH : ℝ}
    (lD : LinkDIV Fm Cabs CH) :
    ∃ C x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x, ∀ u,
      (Fm.D x i).div.RR.muDual + (Fm.D x i).div.h u - (Fm.L x i).Fo ≤
        (Fm.L x i).MAIN u +
        C * ((Fm.D x i).host.TT.card : ℝ) * (Fm.L x i).sc.a * (Fm.L x i).La +
        C * ((Fm.D x i).R.m : ℝ) * ((Fm.L x i).B0 + (Fm.L x i).Nc) *
          (Fm.L x i).sc.x ^ (Cabs * (Fm.L x i).sc.eps) := by
  obtain ⟨C, x0, hD⟩ := lD
  exact ⟨C, x0, fun x hx i => (hD x hx i).2.2.2.2.2.2.1⟩

end RHX

end

#print axioms RHX.h1_pairing_size
