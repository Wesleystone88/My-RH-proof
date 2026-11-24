-- Outside the 705-module closure: both CharacterBoxes imports below.
-- WinPairs supplies the auxiliary data; ZeroFreeAllOfTopG supplies the selected family interface.
import Development.AutomorphicArithmetic.CharacterBoxes.WinPairs
import Development.AutomorphicArithmetic.CharacterBoxes.ZeroFreeAllOfTopG

/-!
# H12 · compatible data throughout arbitrarily late windows

READ (4e8bb36). WinPairs.lean:5 gives the supply quantifiers. TwistForm.lean:19
puts the scale comparison, PairGood, dyadic size and cohomology bound in one
WinDatum. supplyOfAdmOf.lean:56,110 uses its very same q,d for the host.
Supply.lean:42 defines the host requirements. ZeroFreeAllOfTopG.lean:12,26
combines them with a single family and uniform chain constants.
DERIVED. The second theorem raises the left endpoint past the family's threshold.
Every scale throughout that interval then has tied data and the host estimates
at its actual indices. The two theorems display the supply and its family use.
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions Formalism.HC GlobalTheory.EX UpperTheory.Top

namespace RHX

theorem h12_pair_supply (ψ : PChar) (eps c : ℝ) (he : 0 < eps) (he' : eps < 1 / 52)
    (hc : 1 ≤ c) (hV : VWinAt ψ 401) (hP : PairEx) :
    ∃ J : ℝ, 1 ≤ J ∧ ∀ y : ℝ, ∃ Z : ℝ, y ≤ Z ∧
      ∀ x : ℝ, Z ≤ x → x ≤ Z ^ ((3 : ℝ) / 2) →
        ∃ (Y : ℝ) (q d e : ℕ), WinDatum ψ eps J c x Y q d e :=
  UpperTheory.Top.winPairs ψ eps c he he' hc hV hP

theorem h12_family_windows (ψ : PChar) (hTop : TopG)
    (hSupply : HostExW (3 / 2) (GChi ψ).req) :
    ∃ eD eL ε₁ : ℝ, 0 < ε₁ ∧ ∀ eps : ℝ, 0 < eps → eps < ε₁ →
      ∃ (Fm : FamP eps) (K cHH eK CL : ℝ), ∀ y : ℝ, ∃ Z : ℝ, y ≤ Z ∧
        ∀ x : ℝ, Z ≤ x → x ≤ Z ^ ((3 : ℝ) / 2) →
          x ∈ Fm.Win ∧ Nonempty (Fm.Ix x) ∧ ChainTied Fm eD eL K cHH eK CL x ∧
          ∀ i : Fm.Ix x, EAt (Level.cyc ψ) (Fm.D x i) x eps 4 ∧
            VVle (Fm.D x i).host.E (Fm.D x i).R.t (Real.sqrt (Fm.L x i).sc.b) := by
  obtain ⟨eD, eL, ε₁, hε, hf⟩ :=
    hTop (3 / 2) (GChi ψ) (by norm_num) hSupply (hypV_of_cls ψ (3 / 2))
  refine ⟨eD, eL, ε₁, hε, fun eps he he' => ?_⟩
  obtain ⟨Fm, hc, K, cHH, eK, CL, t, ht⟩ := hf eps he he'
  refine ⟨Fm, K, cHH, eK, CL, fun y => ?_⟩
  obtain ⟨Z, hz, hw⟩ := hc.1 (max y (max t (Fm.x1 + 1)))
  refine ⟨Z, (le_max_left _ _).trans hz, fun x hx hxr => ?_⟩
  have hLate := (le_max_right _ _).trans (hz.trans hx)
  have hx1 : Fm.x1 < x := by linarith [le_of_max_le_right hLate]
  have hwin := hw x hx hxr
  refine ⟨hwin, Fm.Ix_win x hwin, ht x (le_of_max_le_left hLate) hwin, fun i => ?_⟩
  obtain ⟨hHost, hCoh⟩ := hc.2 x hx1 i
  rw [Fm.L_x x i hx1, Fm.L_eps x i] at hHost
  exact ⟨hHost, hCoh⟩

end RHX

end

#print axioms RHX.h12_pair_supply
#print axioms RHX.h12_family_windows
