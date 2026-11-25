import Development.AutomorphicArithmetic.DedekindLFunctions.LandauTheorems.ChTop

/-!
# The engine on a test bench

`RHX.engine_M` restates `Deduction.ch_top` (ChTop.lean:37) with exactly its hypotheses and conclusion and
proves it by calling `ch_top`. Nothing is assumed beyond what `ch_top` takes. The point of the file is to
have the engine as one named theorem about an abstract record, so that it can be examined (see
`ENGINE.md`, `HExcision.lean`, `drop_one.py`) without the surrounding construction.

Every import is in `results/common-period-map/closure-files.txt` or
`results/rubinstein-hypotheses/h12-extra-closure.txt` (`ChTop` is the third line of the latter's
`LandauTheorems` entry).
-/

open Finset

noncomputable section

open Deduction.CH Formalism Formalism.D5 Formalism.RankGapBounds.WeightedMeanData
  Formalism.LFunctionChainParameters.WeightedSlopeBounds Formalism.LFunctionChainParameters.characterSumData
  Formalism.LFunctionChainParameters.ThickSetMeanBounds Formalism.LFunctionChainParameters.LErr
  Formalism.LFunctionChainParameters.LChain

namespace RHX

theorem engine_M {H : Type} [AddCommGroup H] [Fintype H] [DecidableEq H] {U0 : Type} [Fintype U0]
    {W : U0 → Type} [∀ u0, Fintype (W u0)] [∀ u0, Nonempty (W u0)]
    {Top : Type} [Fintype Top] {m f : ℕ}
    (Dd : Data U0 W Top m f) (tr : U0 → H) (C : Consts) (Xpp eK K : ℝ)
    (D : ArithData H) (ell : AddChar (E0 × H) ℂ → ℂ) (N : ℕ) (TT T2 : Finset H) (a : H → ℝ)
    (w : H → Fin m → E0 × H → ℝ) (eT : Top ≃ TT) (eP : Fin f ≃ PhiSet (H := H))
    (h1 : IdentU Dd tr D N ell TT a w eT eP) (h2 : SizeData₂ Dd C Xpp) (h3 : ErrWindows Dd C Xpp eK K)
    (h4 : BNBoundsU Dd T2) (h5 : LargeX Dd.x Dd.ε K C.cHH eK) (u : U0) :
    gapA D N ell TT a w (tr u) ≤
      Dd.x ^ (CErr C * Dd.ε) *
        errorBracketSizeWindows Dd.x Dd.ε (Fintype.card H) TT.card T2.card m Dd.b Dd.k Dd.a :=
  Deduction.ch_top Dd tr C Xpp eK K D ell N TT T2 a w eT eP h1 h2 h3 h4 h5 u

end RHX

end

#print axioms RHX.engine_M
