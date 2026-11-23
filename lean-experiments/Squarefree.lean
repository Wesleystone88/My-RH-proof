import Mathlib.Data.Nat.Squarefree
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Linarith

namespace RHExtraction
open Finset
noncomputable section

def outside (m n : ℕ) := n.primeFactors.filter (fun p => Odd (n.factorization p) ∧ ¬ p ∣ m)
def representative (m n : ℕ) := ∏ p ∈ outside m n, p

private theorem mem_outside {m n p : ℕ} :
    p ∈ outside m n ↔ Odd (n.factorization p) ∧ ¬ p ∣ m := by
  simp only [outside, mem_filter]
  constructor
  · exact And.right
  · intro h
    refine ⟨?_, h⟩
    rw [← Nat.support_factorization, Finsupp.mem_support_iff]
    obtain ⟨k, hk⟩ := h.1
    omega

theorem factors_representative (m n : ℕ) :
    (representative m n).primeFactors = outside m n :=
  Nat.primeFactors_prod fun _ hp => Nat.prime_of_mem_primeFactors (mem_filter.mp hp).1

def label (N m n : ℕ) : Fin (N+1) → Bool := fun p => decide (p.val ∈ outside m n)

def flip {ι : Type} (mask : ι → Bool) : (ι → Bool) ≃ (ι → Bool) where
  toFun v i := mask i ^^ v i
  invFun v i := mask i ^^ v i
  left_inv v := by
    funext i
    change (mask i ^^ (mask i ^^ v i)) = v i
    cases mask i <;> cases v i <;> rfl
  right_inv v := by
    funext i
    change (mask i ^^ (mask i ^^ v i)) = v i
    cases mask i <;> cases v i <;> rfl

/-- Each positive pair in a given arithmetic class has a prescribed partner label. -/
theorem partner_label {N m a b r : ℕ} (ha : a ≠ 0) (hb : b ≠ 0)
    (h : representative m (a*b) = r) :
    label N m b = flip (fun p : Fin (N+1) => decide (p.val ∈ r.primeFactors)) (label N m a) := by
  subst r
  funext p
  simp only [flip, Equiv.coe_fn_mk, label, factors_representative, mem_outside,
    Nat.factorization_mul ha hb, Finsupp.add_apply]
  by_cases hm : p.val ∣ m
  · simp [hm]
  · simp only [hm, not_false_eq_true, and_true]
    generalize a.factorization p.val = i
    generalize b.factorization p.val = j
    by_cases hi : Odd i <;> by_cases hj : Odd j <;>
      simp_all [Nat.odd_add, ← Nat.not_odd_iff_even]

variable {I G : Type} [Fintype I] [Fintype G] [DecidableEq G]

def bucket (key : I → G) (w : I → ℝ) (g : G) := ∑ i, if key i = g then w i else 0

theorem regroup (key : I → G) (w : I → ℝ) (f : G → ℝ) :
    ∑ i, w i * f (key i) = ∑ g, bucket key w g * f g := by
  classical
  simp only [bucket, sum_mul, ite_mul, zero_mul]
  rw [sum_comm]
  simp

/-- Works for any class whose ordered pairs force the second bucket from the first
by a permutation. A common upper bound for the individual weights is unnecessary. -/
theorem pair_mass_le_diagonal (key : I → G) (w : I → ℝ) (hw : ∀ i, 0 ≤ w i)
    (e : G ≃ G) (rel : I → I → Prop) [DecidableRel rel]
    (hrel : ∀ i j, rel i j → key j = e (key i)) :
    ∑ i, ∑ j, (if rel i j then w i * w j else 0) ≤ ∑ g, (bucket key w g)^2 := by
  classical
  let W := bucket key w
  calc
    _ ≤ ∑ i, w i * W (e (key i)) := by
      apply sum_le_sum
      intro i _
      simp only [W, bucket, mul_sum, mul_ite, mul_zero]
      apply sum_le_sum
      intro j _
      by_cases h : rel i j
      · simp [h, hrel i j h]
      · simp only [h, if_false]
        split <;> simp [mul_nonneg (hw i) (hw j)]
    _ = ∑ g, W g * W (e g) := regroup key w (fun g => W (e g))
    _ ≤ _ := by
      have h := sum_le_sum (s := (univ : Finset G)) (fun g _ =>
        show 2 * (W g * W (e g)) ≤ (W g)^2 + (W (e g))^2 by nlinarith [sq_nonneg (W g - W (e g))])
      rw [← mul_sum, sum_add_distrib, e.sum_comp (fun g => (W g)^2)] at h
      change _ ≤ ∑ g, (W g)^2
      linarith

/-- Specialization to the finite squarefree sum in meanSq_abs. -/
theorem exceptional_class_bound (N m r : ℕ) (c : ℕ → ℝ) (hc : ∀ n, 0 ≤ c n) :
    ∑ a : Fin N, ∑ b : Fin N,
      (if representative m ((a.val+1)*(b.val+1)) = r then c (a.val+1)*c (b.val+1) else 0)
      ≤ ∑ g, (bucket (fun a : Fin N => label N m (a.val+1)) (fun a => c (a.val+1)) g)^2 := by
  apply pair_mass_le_diagonal _ _ (fun i => hc _) (flip (fun p : Fin (N+1) => decide (p.val ∈ r.primeFactors)))
  intro i j h
  exact partner_label (Nat.succ_ne_zero _) (Nat.succ_ne_zero _) h

def pairMass (N m r : ℕ) (c : ℕ → ℝ) :=
  ∑ a : Fin N, ∑ b : Fin N,
    if representative m ((a.val+1)*(b.val+1)) = r then c (a.val+1)*c (b.val+1) else 0

private theorem same_label {N m a b : ℕ} (ha : 0 < a) (hb : 0 < b)
    (haN : a ≤ N) (hbN : b ≤ N) (h : label N m a = label N m b) :
    representative m (a*b) = 1 := by
  have empty : outside m (a*b) = ∅ := by
    apply eq_empty_iff_forall_notMem.mpr
    intro p hp
    obtain ⟨hodd, hpm⟩ := mem_outside.mp hp
    rw [Nat.factorization_mul ha.ne' hb.ne', Finsupp.add_apply] at hodd
    by_cases hpN : p ≤ N
    · have he := congrFun h (⟨p, by omega⟩ : Fin (N+1))
      simp only [label, mem_outside, hpm, not_false_eq_true, and_true, decide_eq_decide] at he
      grind [Nat.odd_add]
    · have fa := Nat.factorization_eq_zero_of_not_dvd (Nat.not_dvd_of_pos_of_lt ha (by omega : a < p))
      have fb := Nat.factorization_eq_zero_of_not_dvd (Nat.not_dvd_of_pos_of_lt hb (by omega : b < p))
      simp [fa, fb] at hodd
  simp [representative, empty]

/-- For all nonnegative coefficient sequences, the mass of any product class
is at most the mass of class one. This includes arbitrary positive integer
supports and needs neither prime-power support nor individual bucket caps. -/
theorem class_le_trivial (N m r : ℕ) (c : ℕ → ℝ) (hc : ∀ n, 0 ≤ c n) :
    pairMass N m r c ≤ pairMass N m 1 c := by
  classical
  let key := fun i : Fin N => label N m (i.val+1)
  let w := fun i : Fin N => c (i.val+1)
  refine (exceptional_class_bound N m r c hc).trans ?_
  change ∑ g, (bucket key w g)^2 ≤ _
  simp only [pow_two]
  rw [← regroup key w (bucket key w)]
  unfold pairMass
  apply sum_le_sum
  intro i _
  simp only [bucket, mul_sum, mul_ite, mul_zero]
  apply sum_le_sum
  intro j _
  by_cases he : key j = key i
  · have h := same_label (a := i.val+1) (b := j.val+1) (by omega) (by omega)
        (Nat.succ_le_of_lt i.isLt) (Nat.succ_le_of_lt j.isLt) he.symm
    simp [he, h, w]
  · simp only [he, if_false]
    split <;> simp [mul_nonneg (hc _) (hc _)]

#print axioms class_le_trivial

private theorem sum_positive_range (N : ℕ) (f : ℕ → ℝ) :
    (∑ i : Fin N, f (i.val+1)) = ∑ n ∈ Icc 1 N, f n := by
  apply sum_bij (fun (i : Fin N) _ => i.val+1)
  · intro i _
    exact mem_Icc.mpr ⟨by omega, i.isLt⟩
  · intro i _ j _ h
    exact Fin.ext (by omega)
  · intro n hn
    obtain ⟨h₁, h₂⟩ := mem_Icc.mp hn
    exact ⟨⟨n-1, by omega⟩, mem_univ _, by simp; omega⟩
  · intros
    rfl

theorem pairMass_eq (N m r : ℕ) (c : ℕ → ℝ) : pairMass N m r c =
    ∑ a ∈ Icc 1 N, ∑ b ∈ Icc 1 N,
      if representative m (a*b) = r then c a*c b else 0 := by
  unfold pairMass
  rw [sum_positive_range N (fun a => ∑ i : Fin N,
    if representative m (a*(i.val+1)) = r then c a * c (i.val+1) else 0)]
  refine sum_congr rfl fun a _ => ?_
  exact sum_positive_range N (fun b => if representative m (a*b) = r then c a * c b else 0)

theorem interval_class_le_trivial (N m r : ℕ) (c : ℕ → ℝ) (hc : ∀ n, 0 ≤ c n) :
    (∑ a ∈ Icc 1 N, ∑ b ∈ Icc 1 N, if representative m (a*b) = r then c a*c b else 0)
      ≤ ∑ a ∈ Icc 1 N, ∑ b ∈ Icc 1 N, if representative m (a*b) = 1 then c a*c b else 0 := by
  simpa only [pairMass_eq] using class_le_trivial N m r c hc

#print axioms interval_class_le_trivial
end
end RHExtraction
