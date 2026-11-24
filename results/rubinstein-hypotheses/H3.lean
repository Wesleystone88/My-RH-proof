import Formalism.SharpRestriction.GlobalTheoremInputs

/-!
# Rubinstein H3 on the selected family

Rubinstein v2, H3 (p. 204): the level-adjusted heights of two words differ by a bounded amount.
READ. This is the ninth (last) conjunct of `LinkDIV_at` (GlobalTheoremInputs.lean:77).
DERIVED. One constant and one threshold serve every member and every pair of words.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h3_height_comparison {eps : ℝ} (Fm : FamP eps) {Cabs CH : ℝ}
    (lD : LinkDIV Fm Cabs CH) :
    ∃ C x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x, ∀ u u',
      |((Fm.D x i).div.h u + (∑ t : (Fm.D x i).host.TT, ((Fm.L x i).aT t : ℝ)) *
          Real.log (((Fm.D x i).mem u).A.T : ℝ)) -
        ((Fm.D x i).div.h u' + (∑ t : (Fm.D x i).host.TT, ((Fm.L x i).aT t : ℝ)) *
          Real.log (((Fm.D x i).mem u').A.T : ℝ))| ≤
        C * (((Fm.D x i).host.TT.card : ℝ) * (Fm.L x i).sc.a * (Fm.L x i).La +
          ((Fm.D x i).R.m : ℝ) * (Fm.L x i).B0) := by
  obtain ⟨C, x0, hD⟩ := lD
  exact ⟨C, x0, fun x hx i => (hD x hx i).2.2.2.2.2.2.2.2⟩

end RHX

end

#print axioms RHX.h3_height_comparison
