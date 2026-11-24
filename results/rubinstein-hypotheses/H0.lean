import Formalism.SharpRestriction.GlobalSchurBounds.TieGlobal

/-!
# H0 · sizes at the selected window scales
READ (4e8bb36). LossesSmallShares.lean:38,42,219,249 supplies one tied model per
late window scale. TieGlobal.lean:97 retains its translates, sets and constants.
SChain.lean:17,33,53, MeanBoundSecondForm.lean:111 and ErrorFormsWeakWindowsFalse.lean:28
give positivity, the two budget bounds, densities and ranges. Nonempty words use
TieGlobal.lean:13. ChTop.lean:37 additionally takes a large-scale hypothesis.
DERIVED. The size and density assertions below use the same model. The log bound
requires a threshold depending on eps. BNBounds is an inequality interface. The exact per-member budgets below unfold
DataArith.lean:198 and DataParams₂.lean:228 (also LossesSmallShares.lean:250).
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions
open Formalism.RankGapBounds.WeightedMeanData Formalism.LFunctionChainParameters.LErr
open Formalism.LFunctionChainParameters.LChain

namespace RHX

theorem h0_window_sizes {eps : ℝ} (Fm : FamP eps) (heps : 0 < eps)
    {eD eL K cHH eK CL t : ℝ}
    (hFam : ∀ x ≥ t, x ∈ Fm.Win → ChainTied Fm eD eL K cHH eK CL x) :
    ∃ x0 : ℝ, ∀ x ≥ x0, x ∈ Fm.Win →
      ∃ (i0 : Fm.Ix x) (m f : ℕ) (pt : (Fm.D x i0).R.A → Fm.Ix x)
        (Top : Type) (_ : Fintype Top)
        (Dd : Data (Fm.D x i0).R.A (fun v => (Fm.D x (pt v)).what₂.Word) Top m f)
        (C : Consts) (Xpp η X' : ℝ) (TT T2 : Finset (Fm.D x i0).R.A),
        Dd.x = x ∧ Dd.ε = eps ∧ Real.log x ≤ x ^ eps ∧
        1 ≤ m ∧ 3 ≤ Dd.k ∧ Dd.a = x * Dd.b ∧
        (∀ v, 0 < Fintype.card (Fm.D x (pt v)).what₂.Word) ∧
        TieGlobal Fm x pt Dd Xpp η X' ∧ TieLocal Fm x pt Dd ∧
        (∀ h, h ∈ TT ↔ hval (Fm.D x i0).R.toFrame h ∈ Fm.TTn x) ∧
        (∀ v h, h ∈ T2 ↔ ∃ s ∈ (Fm.D x (pt v)).host.T2, h = (Fm.D x i0).R.toFrame.dig s) ∧
        (∀ v, let D := Fm.D x (pt v)
              Dd.B0 = (2 * (D.R.n : ℝ)) * D.R.m * Dd.b * x ^ eps ∧
              Dd.Nc = (D.host.T2.card : ℝ) * D.R.k * Dd.b * x ^ eps /
                ((D.R.n : ℝ) * ((D.R.n : ℝ) * x ^ (-eps)))) ∧
        Dd.HidaSetting C ∧ ErrWindows0 Dd C Xpp eK K ∧ BNBounds Dd T2 ∧
        RestSize eps x (Fintype.card (Fm.D x i0).R.A) TT.card T2.card m Dd.b Dd.k Dd.a := by
  obtain ⟨tLog, hLog⟩ := Filter.eventually_atTop.1 ((isLittleO_log_rpow_atTop heps).bound one_pos)
  refine ⟨max (max t tLog) (Fm.x1 + 1), fun x hx hw => ?_⟩
  obtain ⟨i0, m, f, pt, av, bv, Top, iT, Dd, C, Xpp, ell, N, TT, T2, a, w, eT, eP,
    η, X', θ, hpt, hg, hl, ha, hX, hε, _, _, _, _, hSize, hErr, hBN, _, _, hRest⟩ :=
    hFam x (le_of_max_le_left (le_of_max_le_left hx)) hw
  have hx1 : 1 ≤ x := by rw [← hX]; exact hErr.1.1
  have hlog : Real.log x ≤ x ^ eps := by
    simpa only [Real.norm_eq_abs, one_mul, abs_of_nonneg (Real.log_nonneg hx1),
      abs_of_nonneg (Real.rpow_nonneg (zero_le_one.trans hx1) eps)] using
      hLog x (le_of_max_le_right (le_of_max_le_left hx))
  have hxFam : Fm.x1 < x := by linarith [le_of_max_le_right hx]
  have hm : 1 ≤ m := by
    rw [← (hpt 0).2.1]
    exact le_trans (by decide : 1 ≤ 2) (Fm.D x (pt 0)).R.two_le_m
  have hk : 3 ≤ Dd.k := by
    rw [(hg 0).2.2.2.1]
    have h := (Fm.D x (pt 0)).R.m_add_three_le_k
    exact_mod_cast (by omega : 3 ≤ (Fm.D x (pt 0)).R.k)
  have hab : Dd.a = x * Dd.b := by
    rw [(hg 0).1, (hg 0).2.1]
    show (Fm.L x (pt 0)).sc.x * (Fm.L x (pt 0)).sc.b = _
    rw [Fm.L_x x (pt 0) hxFam]
  refine ⟨i0, m, f, pt, Top, iT, Dd, C, Xpp, η, X', TT, T2, hX, hε, hlog, hm, hk, hab, fun _ => Fintype.card_pos,
    hg, hl, ha.1, ha.2.1, ?_, hSize.1, hErr.1, hBN, hRest⟩
  intro v
  obtain ⟨_, hb, _, _, _, _, hB, hN, _⟩ := hg v
  constructor <;>
    simp [hB, hN, hb, SizeData₂.B0, SizeData₂.Nc, sizeBudget, budgetNc, rankBudget, bSize,
      Scale.b, Scale.L, Ranks.f, Fm.L_x x (pt v) hxFam, Fm.L_eps x (pt v)]

end RHX

end

#print axioms RHX.h0_window_sizes
