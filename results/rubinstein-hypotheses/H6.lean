import Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen

/-!
# Rubinstein H6 on the selected family

READ. The integral inclusion is the first conjunct of `LinkDIV_at`.
`Lnk.slopesNF_of` derives the two slope bounds from `PlacesF`
(GlobalTheoremInputs.lean:77 and TopDensityNGeSixteen.lean:1544).
DERIVED. Taking the larger threshold gives all three clauses at the same member.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem h6_glued_lattice {eps : ℝ} (Fm : FamP eps) {Cabs CH : ℝ}
    (lD : LinkDIV Fm Cabs CH) (hPlaces : Lnk.PlacesF Fm) :
    ∃ C x0 : ℝ, 0 ≤ C ∧ ∀ x ≥ x0, ∀ i : Fm.Ix x,
      (Fm.D x i).div.OneMapIntoCC ∧ Lnk.SlopesN_at (Fm.L x i) C := by
  obtain ⟨_, xd, hD⟩ := lD
  obtain ⟨C, xs, hC, hS⟩ := Lnk.slopesNF_of Fm hPlaces
  refine ⟨C, max xd xs, hC, fun x hx i => ?_⟩
  exact ⟨(hD x (le_trans (le_max_left _ _) hx) i).1,
    hS x (le_trans (le_max_right _ _) hx) i⟩

end RHX

end

#print axioms RHX.h6_glued_lattice
