# Idea: a load-bearing audit for huge formal proofs

Idea: Timothy Wesley Stone. Written up with Claude (Opus, chat), 25 Nov 2026.
Status: **IDEA, deferred.** Nothing new is built for this note; it collects pieces that already exist in this repo.

## The problem, as a picture

A 17-million-line proof is like a building put up from an enormous delivery of parts. The inspector's stamp (Lean's kernel) says the building is sound. It does not say which parts hold it up and which were delivered, carried around the site, and never unpacked. For an AI-written proof that matters: people writing readable versions need to know which pieces carry the mathematics, and critics need to know whether a suspicious piece (like `anyGeometry := fun _ _ _ => True`) does any work.

## Four labels, three rungs

Given a theorem `T` and a piece `X` (a definition, a hypothesis, a structure field):

| Label | Meaning | Rung that decides it |
|---|---|---|
| **NOT IN CONE** | `T` never mentions `X`, even indirectly | 1. Was it delivered? (dependency-cone walk) |
| **CARRIED ONLY** | `X` is mentioned and passed along, but no proof under `T` ever opens it | 2. Was the crate opened? (field projections and eliminators in the proof terms) |
| **OPENED** | some proof under `T` uses what is inside `X` | 2 |
| **ESSENTIAL** | removing `X` breaks `T` | 3. Pull the beam (rebuild without `X`, or a countermodel to the statement without `X`) |

Rung 1 over-reports: a piece can be in the cone only because some type names it. Rung 2 is the step that separates scaffolding from use. Rung 3 cannot be automatic in general.

## What this repo already has

| Rung | Piece | What it did |
|---|---|---|
| 1 | [`results/anygeometry-check/DependsOn.lean`](../results/anygeometry-check/DependsOn.lean) | In-environment walker over types and values, with a positive control (24 Nov). |
| 1 (as excision) | [`results/engine/HExcision.lean`](../results/engine/HExcision.lean) | Showed the engine `ch_top` never reaches the h formula `hExpl6`; positive control from `sExpl` (25 Nov, PASS). |
| 2 | [`results/anygeometry-check/export_scan.py`](../results/anygeometry-check/export_scan.py) | Streamed the 61.5 GB kernel export and marked projections of `OAt.geo` and eliminators of `GeoCl`; found the stamp carried, never opened ([note](../notes/anygeometry-export-scan.md)). Needs no build. |
| 3 (by model) | [`results/engine/drop_one.py`](../results/engine/drop_one.py) | Dropped each hypothesis of the abstract engine and searched for counterexamples: 13 of 15 ESSENTIAL. |
| 3 (by rebuild) | [`notes/anygeometry-removal-map.md`](../notes/anygeometry-removal-map.md), Tier 1 | The edits to delete the `geo` field; the rebuild (5,690 modules) has not been run. |

## What the tool would add

One command: theorem, list of pieces, source (a built environment or a kernel export). Output: one label per piece, with evidence (the path that reaches it, or the declarations that open it). Rules carried over from the work above:

- A positive control on every run. A "not reached" or "never opened" means nothing unless the same run shows the tool finds a known use.
- The pass/fail rule is written down before the run.
- No ESSENTIAL label without a rebuild or an explicitly scoped model, and the label says which.

**The hard part (open).** Some pieces are opened only to be rebuilt into another copy of the same kind of certificate (for example `GeoTiedP`, carried stage to stage by `geoTiedP_divTr`). Mechanically that is OPENED; in substance it is transport. Today that call is made by reading the source. A rule for "opened, but the contents only flow into another copy of the same certificate" would be the new idea here.

**Smallest first step, if picked up.** Make `export_scan.py` generic: target names and structures from the command line instead of hard-coded, plus a built-in positive control.

## Prior art and credit

- Lean's `#print axioms` already walks the same dependency cone, for axioms only. Cone walking is a standard technique.
- Lean core's unused-variables linter works on syntax, and Batteries' `#lint` has an `unusedArguments` environment linter that works declaration by declaration ([docs](https://florisvandoorn.com/LeanCourse24/docs/Batteries/Tactic/Lint/Frontend.html)). An unused-`have` linter exists in Batteries but was reported in January 2026 not to work, because the elaborated term gives false positives ([Zulip](https://leanprover-community.github.io/archive/stream/287929-mathlib4/topic/unused.20have.20linter.html)).
- AXLE's `simplify_theorems` prunes structure a single proof does not use ([arXiv 2606.26442](https://arxiv.org/pdf/2606.26442)).
- **JackyReaps' `ScaffoldingAudit.lean`** ([X-files](https://github.com/jackyreaps/X-files)) is an independent, public cone walker that flags `True` definitions and pass-through carriers. Credit to him for the "load-bearing vs vestigial transport" framing in the public discussion of this proof. Our walker was written separately, for the `anyGeometry` check, and no code is taken from his.
- **Gap, as far as a quick search on 25 Nov found:** a field-level "is `X` ever opened anywhere under `T`" across a whole development, run from a kernel export without building. Not verified beyond that search.

## Addendum, 25 Nov 2026 (afternoon): four refinements for a field-opening audit

Timothy Wesley Stone, with Claude (Opus, chat). Suggested the same day to JackyReaps for his `meta-codex` toolkit (`#audit_fields`). The positive-control rule, the "opened only to be rebuilt" problem and "output with evidence" were already in the note above (committed `e98343b`, 13:18 EST); items 6, 7 and the True shortcut in 9 are new here.

6. **Statement vs. proof.** A field that appears only in a declaration's statement (its type) is mentioned, not opened. Count only projections inside proof or definition bodies, and do not count the structure's own auto-generated projection function as an opening. Three levels: OPENED IN PROOF, MENTIONED ONLY, UNOPENED.
7. **Per-field `casesOn`.** Unpacking a structure (`casesOn`, `match`, `let ⟨a, b⟩ := x`) binds every field, but the branch may use only some. Check which bound variables the branch body actually uses. Compiled `match` goes through matcher helper declarations (`foo.match_1`), so the branches must be inspected where the matcher is called.
8. **Built-in positive control.** Every run first audits a tiny known case (a structure with fields `a`, `b` and a theorem that uses `.a` only) and must report `a` OPENED, `b` UNOPENED; otherwise the run is reported VOID. Optionally the user names a known opener, as `sExpl → hExpl6` in our h check.
9. **Opened only to be re-wrapped.** Cheap half: if the field's type unfolds to `True` at the use site, opening it carries no information (a proof of `True` has nothing to extract). For the headline instance `geo : anyGeometry … ` unfolds to `True`, so every opening of `geo` is information-free. Hard half: follow an opened value; if it goes straight into a constructor, call it TRANSPORT; if it reaches a proof of a different kind of statement, REAL USE; if the trail is too long, UNDETERMINED. In general this cannot be decided, so UNDETERMINED is a required output.
