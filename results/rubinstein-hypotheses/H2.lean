import Formalism.SharpRestriction.GlobalTheoremInputs

/-!
# Rubinstein H2 on the selected family

Rubinstein v2, H2 (p. 204): each level correction differs from its prescribed main term by O(B_0).
READ. This is the eighth conjunct of `LinkDIV_at` (GlobalTheoremInputs.lean:77, the `lifts` clause).
DERIVED. One constant and one threshold serve every member, word and lift.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h2_level_corrections {eps : ℝ} (Fm : FamP eps) {Cabs CH : ℝ}
    (lD : LinkDIV Fm Cabs CH) :
    ∃ C x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x, ∀ u, ∀ j ∈ SizeData₂.lifts (Fm.D x i),
      |(∑ w ∈ (Fm.L x i).supp, SizeData₂.sz w ((Fm.L x i).E u j w)) -
        (∑ t : (Fm.D x i).host.TT, ((Fm.L x i).aT t : ℝ)) *
          Real.log (((Fm.D x i).host.g 0 : ℝ) * ((Fm.D x i).host.g 1 : ℝ))| ≤ C * (Fm.L x i).B0 := by
  obtain ⟨C, x0, hD⟩ := lD
  exact ⟨C, x0, fun x hx i => (hD x hx i).2.2.2.2.2.2.2.1⟩

end RHX

end

#print axioms RHX.h2_level_corrections
