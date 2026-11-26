# Claude Code: meta-codex pull request 1 — standalone ConeAudit + module filter (25 Nov 2026)

Written by Claude in chat. This is for **jackyreaps/meta-codex**, not the RH repos. The owner approved both changes in issue #1 ("Feel free to open a PR from a branch") and added an MIT LICENSE (`cd0bac8`).
Rules: one Lean process at a time; do not run this while the 25c export scan is running; nothing in `C:\rhc`; never push to `main`; no new toolchain downloads without asking Timmy; stop if C: has less than 25 GB free.

## Setup

1. Clone `https://github.com/jackyreaps/meta-codex` into `XPostCode/meta-codex` (a new folder, next to My-RH-proof). Confirm `LICENSE` exists on `main`; if it does not, stop and tell Timmy.
2. Create branch `standalone-cone-audit`.
3. Check that the Lean toolchain `leanprover/lean4:v4.33.1` is already installed (`elan toolchain list`). If it is not, stop and ask Timmy before downloading anything.

## Change 1: make meta-codex depend on nothing but Lean

- Copy the current `riemann-hypothesis/ScaffoldingAudit.lean` from `https://github.com/jackyreaps/X-files` (record the X-files commit you copied from) into meta-codex, either as the body of `Core/ConeAudit.lean` or as `Core/ScaffoldingAudit.lean` imported by it. Keep its header and its author's credit. It imports only `Lean`; confirm that.
- Remove the `[[require]] X-files` block from `lakefile.toml`, and update `lake-manifest.json` so it lists no packages.
- Set `lean-toolchain` to `leanprover/lean4:v4.33.1` (the RH archive's version). If anything fails to compile on 4.33.1, fix only what is needed and list each fix.

## Change 2: filter by module, not by name prefix

`collectActiveCone` in `Core/FieldProjection.lean` (and the cone walk in the copied ScaffoldingAudit, if it has the same filter) skips names starting with `Lean.`, `Init.`, `Std.`, `Mathlib.`. Mathlib and Init declarations are not named that way, so the filter misses them. Replace it with a check on the declaration's **module**: `env.getModuleIdxFor? n`, then the module name from the environment's header. Skip a constant when its module's first component is in a list (default: `Init`, `Lean`, `Std`, `Mathlib`, `Batteries`, `Aesop`, `Qq`, `ProofWidgets`, `Plausible`, `ImportGraph`, `LeanSearchClient`). Constants with no module (defined in the file being audited) are kept. Make the list one easy-to-edit definition. Use whatever API 4.33.1 actually provides; say which.

Keep the change small: no other refactors, no README edits (the owner is doing the README).

## Test (pre-registered: write these expectations in the PR notes before running)

- `lake build` succeeds with no `sorry`, and nothing is downloaded except what the empty manifest needs (nothing).
- Run `Examples/HigherDimDemo.lean` before (on `main`, if it builds there without fetching Mathlib; otherwise skip the "before" and say so) and after. The `#audit_*` outputs should match, except that constants from `Init`/`Lean`/`Std` no longer appear in cone listings.
- Add one check to the demo: an `#audit_theorem` on a theorem that uses a core lemma (for example `Nat.add_comm`) must not list that core lemma after the change.

## Last step

Commit on the branch with a message saying Claude Code made the change at Timmy's request, ending with the usual attribution lines, and push the **branch** (never `main`). Do **not** open the pull request: Timmy writes and opens it himself. Give Timmy a plain list of facts for it: what changed, the X-files commit copied from, the toolchain, each compile fix, and the before/after test results.
