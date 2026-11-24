import Lean
import Std.Data.HashSet
import Std.Data.HashMap
import Formalism.SharpRestriction.GlobalTheoremInputs
import Development.AutomorphicArithmetic.CharacterBoxes.ExistsPageN
import Development.AutomorphicArithmetic.CharacterBoxes.ZeroFreeAllOfTopG
-- Control theorems of ours, compiled to .olean files first (see README.md in this folder).
import CommonPeriodMap
import CommonPeriodMap2
import H1
import H2
import H3
import H4
import H5
import H6
import H7
import H9

/-!
# Does `anyGeometry` appear in the transitive constants of a declaration?

For each root declaration this walks every constant it uses, transitively, through the
environment's `ConstantInfo` types and values, and reports whether a constant whose last name
component is `anyGeometry` is reached. A positive control shows the walker does detect a
dependency when there is one.

LIMIT (stated up front): `anyGeometry` is defined in `OverIx.lean`, which is not in the 705-module
build or the 104-module H12 supplement. If that module is not loaded, no constant in this
environment can mention `anyGeometry`, so a "not reached" answer here follows from the import
closure and is not a fresh finding about the proofs. The first output line reports whether
`OverIx` and `EveryCharacterE` are loaded. This file checks the DEFINITIONS of the premises and
our own theorems. It does not check the suppliers of those premises for the headline family;
that needs `OverIx` and its dependents built, which is a large build.
-/

open Lean Elab Command

def constsOf (ci : ConstantInfo) : Array Name :=
  let a := ci.type.getUsedConstants
  match ci.value? (allowOpaque := true) with
  | some v => a ++ v.getUsedConstants
  | none => a

/-- Walk constants reachable from `root`. Returns (visited count, first reached name satisfying
`hit`, path from root to it). -/
def reach (env : Environment) (root : Name) (hit : Name → Bool) :
    Nat × Option Name × List Name := Id.run do
  let mut seen : Std.HashSet Name := {}
  let mut parent : Std.HashMap Name Name := {}
  let mut stack : Array Name := #[root]
  seen := seen.insert root
  let mut found : Option Name := none
  if hit root then found := some root
  while found.isNone && !stack.isEmpty do
    let n := stack.back!
    stack := stack.pop
    match env.find? n with
    | none => pure ()
    | some ci =>
      for c in constsOf ci do
        if found.isNone && !seen.contains c then
          seen := seen.insert c
          parent := parent.insert c n
          if hit c then found := some c
          stack := stack.push c
  let mut path : List Name := []
  match found with
  | some f =>
    let mut cur := f
    path := [cur]
    while cur != root do
      match parent.get? cur with
      | some p => path := p :: path; cur := p
      | none => break
  | none => pure ()
  return (seen.size, found, path)

def isAnyGeometry (n : Name) : Bool :=
  match n with
  | .str _ s => s == "anyGeometry"
  | _ => false

def report (env : Environment) (label : String) (root : Name) (hit : Name → Bool) (what : String) :
    IO Unit := do
  if !env.contains root then
    IO.println s!"{label}: {root}  NOT IN ENVIRONMENT (name not found)"
  else
    let (n, f, p) := reach env root hit
    match f with
    | none => IO.println s!"{label}: {root}  -> {what} NOT reached  ({n} constants visited)"
    | some x =>
      IO.println s!"{label}: {root}  -> {what} REACHED at {x}  ({n} constants visited)"
      IO.println s!"    path: {p}"

#eval show CommandElabM Unit from do
  let env ← getEnv
  let mods := env.header.moduleNames.map toString
  let hasOverIx := mods.any (·.endsWith "OverIx")
  let hasEveryE := mods.any (·.endsWith "EveryCharacterE")
  IO.println s!"modules loaded: {mods.size}; OverIx loaded: {hasOverIx}; EveryCharacterE loaded: {hasEveryE}"
  let mut nAny := 0
  for (n, _) in env.constants.toList do
    if isAnyGeometry n then nAny := nAny + 1
  IO.println s!"constants named *.anyGeometry in this environment: {nAny}"
  IO.println "--- premises (definitions)"
  for r in [`Formalism.MainNotions.LinkDIV, `Formalism.MainNotions.LinkS,
            `Formalism.MainNotions.ChosenProviso, `UpperTheory.Top.TopG, `UpperTheory.Top.VWin] do
    report env "premise" r isAnyGeometry "anyGeometry"
  IO.println "--- controls (our theorems)"
  for r in [`RHX.one_map_three_sections, `RHX.common_period_map, `RHX.common_period_map_family,
            `RHX.h1_pairing_size, `RHX.h2_level_corrections, `RHX.h3_height_comparison,
            `RHX.h4_word_counts, `RHX.h5_bottom_lattice, `RHX.h6_glued_lattice,
            `RHX.h7_gain_and_losses, `RHX.h9_target_slope] do
    report env "control" r isAnyGeometry "anyGeometry"
  IO.println "--- positive control: the walker does detect a real dependency"
  report env "positive" `RHX.h1_pairing_size (fun n => n == `Formalism.MainNotions.LinkDIV) "LinkDIV"
  report env "positive" `RHX.h6_glued_lattice (fun n => n == `Formalism.MainNotions.LinkDIV) "LinkDIV"
