import Std

/-! A squarefree class is encoded by the parities of its prime exponents.
For a fixed product class, the first parity vector determines the second.
The sums here enumerate all bit vectors of the given length, including
classes with zero mass. The ring identity works for arbitrary weights. -/
namespace RHExtraction
open Lean.Grind

def cubeSum {R : Type} [Add R] : Nat → (List Bool → R) → R
  | 0, f => f []
  | n+1, f => cubeSum n (fun v => f (false :: v)) +
                cubeSum n (fun v => f (true :: v))

def shift (mask v : List Bool) : List Bool := List.zipWith Bool.xor mask v

variable {R : Type} [CommRing R]

theorem sum_shift (mask : List Bool) (f : List Bool → R) :
    cubeSum mask.length (fun v => f (shift mask v)) = cubeSum mask.length f := by
  induction mask generalizing f with
  | nil => rfl
  | cons b s ih =>
    have h₀ := ih (fun v => f (false :: v))
    have h₁ := ih (fun v => f (true :: v))
    unfold shift at h₀ h₁
    cases b <;> simp only [List.length_cons, cubeSum, shift, List.zipWith_cons_cons,
      Bool.false_xor, Bool.true_xor, Bool.not_false, Bool.not_true] <;>
      rw [h₀, h₁]
    exact AddCommMonoid.add_comm _ _

theorem sum_add (n : Nat) (f g : List Bool → R) :
    cubeSum n (fun v => f v + g v) = cubeSum n f + cubeSum n g := by
  induction n generalizing f g with
  | zero => rfl
  | succ n ih =>
    simp only [cubeSum]
    rw [ih (fun v => f (false :: v)) (fun v => g (false :: v)),
        ih (fun v => f (true :: v)) (fun v => g (true :: v))]
    grind

def diagonal (n : Nat) (w : List Bool → R) := cubeSum n (fun v => w v * w v)
def correlation (mask : List Bool) (w : List Bool → R) :=
  cubeSum mask.length (fun v => w v * w (shift mask v))

/-- Twice the slack in the diagonal bound is exactly a sum of squares. -/
theorem parity_energy_identity (mask : List Bool) (w : List Bool → R) :
    cubeSum mask.length (fun v => (w v - w (shift mask v)) ^ 2) +
      (correlation mask w + correlation mask w) =
    diagonal mask.length w + diagonal mask.length w := by
  let shifted := fun v => w (shift mask v)
  have pointwise : (fun v => (w v - shifted v) ^ 2 + (w v * shifted v + w v * shifted v)) =
      (fun v => w v * w v + shifted v * shifted v) := by
    funext v
    grind
  have h := congrArg (cubeSum mask.length) pointwise
  simp only [sum_add] at h
  have hs := sum_shift mask (fun v => w v * w v)
  unfold correlation diagonal
  change cubeSum mask.length (fun v => shifted v * shifted v) = _ at hs
  rw [hs] at h
  exact h

#print axioms parity_energy_identity

variable [LE R] [LT R] [Std.IsLinearOrder R] [Std.LawfulOrderLT R] [OrderedRing R]

omit [Std.LawfulOrderLT R] in
private theorem cube_nonneg (n : Nat) (f : List Bool → R) (hf : ∀ v, 0 ≤ f v) :
    0 ≤ cubeSum n f := by
  induction n generalizing f with
  | zero => exact hf []
  | succ n ih =>
    have h := OrderedAdd.add_le_add (ih (fun v => f (false :: v)) (fun _ => hf _))
      (ih (fun v => f (true :: v)) (fun _ => hf _))
    simpa only [cubeSum, AddCommMonoid.zero_add] using h

theorem parity_correlation_le (mask : List Bool) (w : List Bool → R) :
    correlation mask w ≤ diagonal mask.length w := by
  have h := parity_energy_identity mask w
  have h₀ := cube_nonneg mask.length (fun v => (w v - w (shift mask v))^2)
    (fun _ => OrderedRing.sq_nonneg)
  grind only

#print axioms parity_correlation_le
end RHExtraction
