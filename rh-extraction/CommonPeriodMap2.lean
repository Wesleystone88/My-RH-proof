import Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen

/-!
# One map, three sections

Author: Timothy Wesley Stone, with Claude.
Pinned source: homeowmorphism/riemann-hypothesis-original @ 4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e
(src tree 24df20b62d9976ccd20da819bc20b16f808f0fdd, the same tree as upstream e50d098).

Rubinstein's H8 ("One map, three sections") and O25(e), and Zhang's Proposition 4.3, ask
whether a single map β_w satisfies three conditions at once:
(8a) it sends the integral lattice into the target lattice;
(8b) its height is bounded;
(8c) at one archimedean place its matrix is a block of a larger complex map whose Gram
operators satisfy the near-orthogonality bounds of Zhang's Lemma 4.2.

In the formal proof the map is `D.div.Bk u`, and the conditions are:
* (8a) `D.div.OneMapIntoCC`;
* (8b) `htMap … (D.div.Bk u) ≤ D.div.h u`;
* (8c) `Lnk.MatK_at D η0 e0`. This says that the matrix of the same `D.div.Bk u` at the place `v`,
  written as `Y'⁻¹ · M(Bk u) · Y u`, is the top block of `Bf u * Vr u`. Here `Vr u` is an isometry,
  and `Bf` satisfies the off-diagonal (`KpG`) and diagonal (`KdG`) Hilbert–Schmidt bounds.

The theorem below shows that the headline proof's own premises (`LinkDIV`, `LinkS` and
`ChosenProviso`, all on one family `Fm`) give all three for every member of the family,
eventually. It adds no new mathematics. It packages, as one statement, what the source
proves in `matKF_of` (TopDensityNGeSixteen.lean:1348) and in `LinkDIV_at`
(GlobalTheoremInputs.lean:77).

Downstream, `frameReal_at_of` (:679) bundles the same three facts into `LatGeom`, in which a
single `B` carries the inclusion, the height and the block identity. `frame_at_of` (:538) then
applies `joint_a_ramified_holds`, which turns them into the mean-slope bound `Frame_at`.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions

namespace RHX

theorem one_map_three_sections {eps : ℝ} (Fm : FamP eps) {Cabs CH C0 : ℝ} (hC0 : 0 < C0)
    (lD : LinkDIV Fm Cabs CH) (lS : LinkS Fm C0) (cPr : ChosenProviso Fm C0) :
    ∃ x0 : ℝ, ∀ x ≥ x0, ∀ i : Fm.Ix x, ∃ η0 e0 : ℝ,
      -1 ≤ η0 ∧ η0 ≤ Real.exp (-(x ^ (eps / 8))) ∧ 0 ≤ e0 ∧
      Real.sqrt e0 ≤ Real.exp (-(x ^ (eps / 8))) ∧
      (Fm.D x i).div.OneMapIntoCC ∧
      (∀ u, (Fm.D x i).div.Bk u ≠ 0 →
        Formalism.HN.htMap ((Fm.D x i).div.Nu u).b ((Fm.D x i).div.Nu u).X (Fm.D x i).div.RR.dualB
          (Fm.D x i).div.RR.dualX ((Fm.D x i).div.Bk u) ≤ (Fm.D x i).div.h u) ∧
      Formalism.MainNotions.Lnk.MatK_at (Fm.D x i) η0 e0 := by
  obtain ⟨a0, hK⟩ := Formalism.MainNotions.Lnk.matKF_of Fm Cabs CH C0 hC0 lS cPr lD
  obtain ⟨C, a1, hD⟩ := lD
  refine ⟨max a0 a1, fun x hx i => ?_⟩
  obtain ⟨η0, e0, h1, h2, h3, h4, hM⟩ := hK x (le_trans (le_max_left _ _) hx) i
  have hDi := hD x (le_trans (le_max_right _ _) hx) i
  exact ⟨η0, e0, h1, h2, h3, h4, hDi.1, hDi.2.2.2.2.2.1, hM⟩

end RHX

end

#print axioms RHX.one_map_three_sections
