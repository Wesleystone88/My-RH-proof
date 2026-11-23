import Std

/-! Linear skeleton of the zeta "transfer" step in Alpöge's formalization
(commit e50d09817ad81469f737e8f637561e6ccf86c670).

Source: `s_lower5`, `Ga_bound5` and `each_unit_bound_statement` in
src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean
(lines 49-69, 113-161, 175-197).

The quantities are free variables in any ordered commutative ring. The
source lemmas use real numbers and supply each hypothesis from a named
component of `SizeData₂` or from `LossBounds`. The averaging step between
the two levels (`sub_wmean_le`) is not modelled: level one is the pointwise
bound, level two starts from its weighted mean `s`.

The `*_needed` theorems are the load-bearing test: dropping one structural
hypothesis lets the conclusion fail, shown by explicit integer values. -/
namespace RHExtraction
open Lean.Grind

variable {R : Type} [CommRing R] [LE R] [LT R] [Std.IsLinearOrder R]
  [Std.LawfulOrderLT R] [OrderedRing R]

/-- Level one, pointwise in `u` (mirrors `s_lower5`).
* `gain`  : QuotientSlopeBoundsWith, second half (twisting by places raises the slope by Ga).
* `div`   : DIV (degree of the ambient lattice bounded by the explicit archimedean sum).
* `count` : Count5 lower bound, multiplied by `A = sumA ≥ 0`.
* `eUp`   : EComp5 upper half, with `P = m·sumA·lg`.
* `slM`   : Slopes lower half.
* `key`   : `key_identity5` (exact algebra; produces Main). -/
theorem pointwise_lower
    (muN muM muCC h Ga Fo Ee Lo SDiv EDiv A logT Lam P mcEB0 SL Main KC : R)
    (gain : muM + Ga + Fo - Ee - Lo ≤ muN)
    (div : muCC + h - Fo ≤ SDiv - A * logT + EDiv)
    (count : A * Lam ≤ A * logT)
    (eUp : Ee ≤ P + mcEB0)
    (slM : -SL ≤ muM)
    (key : SDiv - A * Lam + P = Main + KC) :
    Ga + muCC - (Main + KC + SL + mcEB0 + EDiv + Lo) ≤ muN - h := by
  grind

/-- Level two, after averaging (mirrors `Ga_bound5` + `each_unit_bound_statement`).
* `lower` : averaged level one (`s` is the weighted mean of `muN - h`).
* `slope` : SlopeIneq (mean slope ≤ ambient slope + log of family size + Phi).
* `loss`  : LossBounds, first half (the prime ramp sum ASK is within LoP of Ga).
Both `muCC` and `Ga` cancel. -/
theorem transfer
    (ASK Ga Main muCC s E logW Phi LoP : R)
    (lower : Ga + muCC - Main - E ≤ s)
    (slope : s - logW - Phi ≤ muCC)
    (loss : ASK - Ga ≤ LoP) :
    ASK - Main ≤ LoP + E + logW + Phi := by
  grind

#print axioms pointwise_lower
#print axioms transfer

/-! Load-bearing test at level two. Each statement says: the other two
hypotheses can hold while the conclusion fails. -/

theorem slope_needed : ∃ ASK Ga Main muCC s E logW Phi LoP : Int,
    Ga + muCC - Main - E ≤ s ∧ ASK - Ga ≤ LoP ∧
    ¬ (ASK - Main ≤ LoP + E + logW + Phi) :=
  ⟨100, 100, 0, 0, 100, 0, 0, 0, 0, by decide⟩

theorem lower_needed : ∃ ASK Ga Main muCC s E logW Phi LoP : Int,
    s - logW - Phi ≤ muCC ∧ ASK - Ga ≤ LoP ∧
    ¬ (ASK - Main ≤ LoP + E + logW + Phi) :=
  ⟨100, 100, 0, 0, 0, 0, 0, 0, 0, by decide⟩

theorem loss_needed : ∃ ASK Ga Main muCC s E logW Phi LoP : Int,
    Ga + muCC - Main - E ≤ s ∧ s - logW - Phi ≤ muCC ∧
    ¬ (ASK - Main ≤ LoP + E + logW + Phi) :=
  ⟨100, 0, 0, 0, 0, 0, 0, 0, 0, by decide⟩

/-! Load-bearing test at level one: without DIV the ambient slope `muCC`
is not tied to the explicit main term. -/
theorem div_needed : ∃ muN muM muCC h Ga Fo Ee Lo SDiv EDiv A logT Lam P mcEB0 SL Main KC : Int,
    muM + Ga + Fo - Ee - Lo ≤ muN ∧ A * Lam ≤ A * logT ∧ Ee ≤ P + mcEB0 ∧
    -SL ≤ muM ∧ SDiv - A * Lam + P = Main + KC ∧
    ¬ (Ga + muCC - (Main + KC + SL + mcEB0 + EDiv + Lo) ≤ muN - h) :=
  ⟨0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, by decide⟩

theorem gain_needed : ∃ muN muM muCC h Ga Fo Ee Lo SDiv EDiv A logT Lam P mcEB0 SL Main KC : Int,
    muCC + h - Fo ≤ SDiv - A * logT + EDiv ∧ A * Lam ≤ A * logT ∧ Ee ≤ P + mcEB0 ∧
    -SL ≤ muM ∧ SDiv - A * Lam + P = Main + KC ∧
    ¬ (Ga + muCC - (Main + KC + SL + mcEB0 + EDiv + Lo) ≤ muN - h) :=
  ⟨0, 0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, by decide⟩

#print axioms slope_needed
#print axioms div_needed
end RHExtraction
