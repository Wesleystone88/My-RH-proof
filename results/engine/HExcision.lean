import Lean
import Std.Data.HashSet
import Std.Data.HashMap
import Development.AutomorphicArithmetic.DedekindLFunctions.LandauTheorems.ChTop
import Formalism.LocalRingCardinality.KernelPlaceMeanBound
import Formalism.SharpRestriction.Divisibility.LocalQuadraticParts

/-!
# Is `hExpl6` (the formula for h) reachable from `ch_top`?

Constant-reachability walk, copied from `results/anygeometry-check/DependsOn.lean` (`constsOf`, `reach`).
It follows every constant used in the type or the value of a declaration, transitively.

* root: `Deduction.ch_top` (ChTop.lean:37)
* targets: any constant whose last name component is `hExpl6`; separately `setDiv`
* positive control: from `sExpl` (LocalQuadraticParts.lean:350) the walk must reach `hExpl6`

LIMIT: this is reachability through types and values. It does not say which fields of a record a proof
projects, and it does not distinguish a use in a proof from a mention in a type.

Pre-registered outcomes are in `H-EXCISION.md`.
-/

open Lean Elab Command

def constsOf (ci : ConstantInfo) : Array Name :=
  let a := ci.type.getUsedConstants
  match ci.value? (allowOpaque := true) with
  | some v => a ++ v.getUsedConstants
  | none => a

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

/-- full walk without stopping: how many constants are reachable from `root` -/
def reachAll (env : Environment) (root : Name) : Nat := Id.run do
  let mut seen : Std.HashSet Name := {}
  let mut stack : Array Name := #[root]
  seen := seen.insert root
  while !stack.isEmpty do
    let n := stack.back!
    stack := stack.pop
    match env.find? n with
    | none => pure ()
    | some ci =>
      for c in constsOf ci do
        if !seen.contains c then
          seen := seen.insert c
          stack := stack.push c
  return seen.size

def lastComp (n : Name) : String :=
  match n with
  | .str _ s => s
  | _ => ""

#eval show CommandElabM Unit from do
  let env ← getEnv
  let mut hs : Array Name := #[]
  let mut ss : Array Name := #[]
  let mut sd : Array Name := #[]
  for (n, _) in env.constants.toList do
    if lastComp n == "hExpl6" then hs := hs.push n
    if lastComp n == "sExpl" then ss := ss.push n
    if lastComp n == "setDiv" then sd := sd.push n
  let defMod := `Formalism.LocalRingCardinality.KernelPlaceMeanBound
  let loaded := env.header.moduleNames.contains defMod
  IO.println s!"FIRST LINE: module defining hExpl6 ({defMod}) loaded: {loaded}; hExpl6 constants found: {hs}"
  IO.println s!"modules loaded: {env.header.moduleNames.size}; sExpl constants: {ss}; setDiv constants: {sd}"
  let root := `Deduction.ch_top
  IO.println s!"root present: {env.contains root}"
  if !loaded || hs.isEmpty then
    IO.println "VOID: the module defining hExpl6 is not loaded; the check means nothing."
  else
    let isH (n : Name) : Bool := lastComp n == "hExpl6"
    let (vis, f, p) := reach env root isH
    match f with
    | none => IO.println s!"ch_top -> hExpl6: NOT reached ({vis} constants visited)"
    | some x =>
      IO.println s!"ch_top -> hExpl6: REACHED at {x} ({vis} constants visited)"
      IO.println s!"  shortest-found path: {p}"
    let total := reachAll env root
    IO.println s!"constants reachable from ch_top in total: {total}"
    let isSD (n : Name) : Bool := lastComp n == "setDiv"
    let (vis2, f2, p2) := reach env root isSD
    match f2 with
    | none => IO.println s!"ch_top -> setDiv: NOT reached ({vis2} constants visited)"
    | some x =>
      IO.println s!"ch_top -> setDiv: REACHED at {x} ({vis2} constants visited)"
      IO.println s!"  path: {p2}"
    IO.println "--- positive control: sExpl -> hExpl6"
    if ss.isEmpty then
      IO.println "CONTROL VOID: no sExpl constant is loaded"
    else
      for s in ss do
        let (v3, f3, p3) := reach env s isH
        match f3 with
        | none => IO.println s!"control FAILED: {s} does not reach hExpl6 ({v3} constants visited)"
        | some x =>
          IO.println s!"control OK: {s} reaches {x} ({v3} constants visited)"
          IO.println s!"  path: {p3}"
