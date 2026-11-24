import Formalism.SharpRestriction.GlobalSchurBounds.QuadraticLogDerivCongr

/-!
# H7 · losses on the chosen translates
READ (4e8bb36). GlobalTheoremInputs.lean:122 restricts the local gain comparison
to inert primes below the cutoff. LinkMin.lean:720 and LossesSmallShares.lean:86,201
pass the loss bound to the selected translates. SChain.lean:17 packages
LossBounds (QuotientSlopeBoundsWith.lean:34) in ChainTied (TieGlobal.lean:97).
DERIVED. A common threshold gives the local statement for every index and the
two global losses for each selected translate. The global bound has a common
constant and exponent through C.cLoss and C.eLoss; only the latter is bounded
explicitly here and the uniform constant bound comes from ErrWindows0.
TieArith and Ident identify ASK with the chosen prime sum (TieGlobal.lean:84, SChain.lean:26).
-/

noncomputable section

open Formalism.BasicNotions Formalism.MainNotions
open Formalism.RankGapBounds.WeightedMeanData Formalism.LFunctionChainParameters.LErr
open Formalism.D5 Formalism.LFunctionChainParameters.ThickSetMeanBounds
open Formalism.LFunctionChainParameters.LChain

namespace RHX

theorem h7_gain_and_losses {eps : ℝ} (Fm : FamP eps) (lG : LinkG Fm)
    {eD eL K cHH eK CL t : ℝ}
    (hFam : ∀ x ≥ t, x ∈ Fm.Win → ChainTied Fm eD eL K cHH eK CL x) :
    ∃ (Cg x0 : ℝ) (δ : ℝ → ℝ), Filter.Tendsto δ Filter.atTop (nhds 0) ∧
      ∀ x ≥ x0, x ∈ Fm.Win →
        (∀ i : Fm.Ix x, LinkG_at (Fm.Gx x i) Fm.GK Cg ((Fm.L x i).sc.b ^ δ x)) ∧
        ∃ (i0 : Fm.Ix x) (m f : ℕ) (pt : (Fm.D x i0).R.A → Fm.Ix x)
          (Top : Type) (_ : Fintype Top)
          (Dd : Data (Fm.D x i0).R.A (fun v => (Fm.D x (pt v)).what₂.Word) Top m f)
          (C : Consts) (Xpp η X' : ℝ) (av : ℕ → ℤ) (N : ℕ)
          (ell : AddChar (E0 × (Fm.D x i0).R.A) ℂ → ℂ)
          (TT T2 : Finset (Fm.D x i0).R.A) (a : (Fm.D x i0).R.A → ℝ)
          (w : (Fm.D x i0).R.A → Fin m → E0 × (Fm.D x i0).R.A → ℝ)
          (eT : Top ≃ TT) (eP : Fin f ≃ PhiSet (H := (Fm.D x i0).R.A)),
          Dd.x = x ∧ Dd.ε = eps ∧ C.eLoss ≤ eL ∧ ErrWindows0 Dd C Xpp eK K ∧
          TieGlobal Fm x pt Dd Xpp η X' ∧ TieLocal Fm x pt Dd ∧
          TieArith Fm x pt av (arithOf (Fm.D x i0).host.toHostRaw) ell TT T2 a w ∧
          Ident Dd (arithOf (Fm.D x i0).host.toHostRaw) N ell TT a w eT eP ∧
          ∀ v, Dd.ASK v - Dd.Ga v ≤ Dd.LoP C ∧ Dd.IO v ≤ Dd.LoP C := by
  obtain ⟨Cg, tg, δ, hδ, hg⟩ := lG
  refine ⟨Cg, max tg t, δ, hδ, fun x hx hw => ⟨hg x ((le_max_left _ _).trans hx), ?_⟩⟩
  obtain ⟨i0, m, f, pt, av, bv, Top, iT, Dd, C, Xpp, ell, N, TT, T2, a, w, eT, eP,
    η, X', θ, _, hGlobal, hl, hArith, hX, hε, _, heL, _, hIdent, hSize, hErr, _⟩ :=
    hFam x ((le_max_right _ _).trans hx) hw
  obtain ⟨_, _, _, _, _, _, _, hLoss, _⟩ := hSize
  exact ⟨i0, m, f, pt, Top, iT, Dd, C, Xpp, η, X', av, N, ell, TT, T2, a, w,
    eT, eP, hX, hε, heL, hErr.1, hGlobal, hl, hArith, hIdent, hLoss⟩

end RHX

end

#print axioms RHX.h7_gain_and_losses
