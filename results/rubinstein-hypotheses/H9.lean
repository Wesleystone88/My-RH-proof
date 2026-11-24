import Formalism.SharpRestriction.GlobalTheoremInputs

/-!
# Rubinstein H9 on the selected family

Rubinstein v2, H9 (p. 206): the mean height-adjusted slope sits within x^{C_H} b of the target slope.
READ. This is the second conjunct of `LinkDIV_at` (GlobalTheoremInputs.lean:77): the frame mean plus the
maximal slope of the target is at most x^{C_H} b. With `Lat_at`, `muMinDual = -muMax`, this is H9's form.
DERIVED. One threshold serves every member.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h9_target_slope {eps : ℝ} (Fm : FamP eps) {Cabs CH : ℝ}
    (lD : LinkDIV Fm Cabs CH) :
    ∃ x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x,
      sFrame (Fm.D x i).div.Nu (Fm.D x i).div.h + (Fm.D x i).div.RR.muMax ≤
        (Fm.L x i).sc.x ^ CH * (Fm.L x i).sc.b := by
  obtain ⟨_, x0, hD⟩ := lD
  exact ⟨x0, fun x hx i => (hD x hx i).2.1⟩

end RHX

end

#print axioms RHX.h9_target_slope
