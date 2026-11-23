# Codex task: compile CommonPeriodMap.lean from source on C: (small build, no project cache)

> **Update (23 Nov, later).** `compile-closure.ps1` in this folder now does Part A by itself, with no AI needed. If `compile-log.txt` says ALL PASSED, skip Part A.
> - `closure-files.txt` now lists **705** modules (sha256 `74664cc73f7eec24eeaa32e76d8ba1fbcf8c5c4ba7e25c1f2ab7dcf8e8508484`). This is the union needed by `CommonPeriodMap.lean` and by the new `CommonPeriodMap2.lean`.
> - The build target is `Formalism.SharpRestriction.GlobalSchurBounds.TopDensityNGeSixteen`.
> - Part C was answered by Claude in `CommonPeriodMap2.lean` (`RHX.one_map_three_sections`).


## Why this route works

The last attempt stopped because the project cache needs all 175,187 modules. Our file needs far fewer. It imports only `Formalism.SharpRestriction.GlobalTheoremInputs`. At the pinned source tree (`src` = `24df20b62d9976ccd20da819bc20b16f808f0fdd`), that module's import closure is **307 repo modules** plus Mathlib, about 2.3 MB of source. `closure-files.txt` in this folder lists them; its sha256 is `57c04567041a11dad341a2b0497cf56977a069bf9eb6dc3ecc9d39ddf3355b20`.

So we build those 307 modules **from source**, with Mathlib's own cache, and do not download the project cache at all. This is a stronger check than the cache route. Lean re-checks everything our file stands on, except Mathlib.

Do not use D:. It is exFAT with 1 MiB clusters. Use C:, which is NTFS with 4 KiB clusters.

## Stop conditions

- Stop and report if free space on C: falls below 25 GB at any point.
- Stop and report if one module builds for more than 90 minutes, or the build runs out of memory.
- Never run `lake exe cache get` (the project cache). Use only `lake exe mathlib/cache get`.
- Never edit anything under `src/`. Never change the statements in `CommonPeriodMap.lean`.

## Part A: build and compile

1. **Check prerequisites.** Record free bytes on C:, the CPU core count and RAM. Check that `CommonPeriodMap.lean` here still has sha256 `573cd37bb2621d52be6e4f124eda0b35cb3565db1818d4b57aa2f004d5888410`.

2. **Make a sparse clone at a short path.**
   ```powershell
   git -c core.longpaths=true clone --filter=blob:none --no-checkout --depth 1 https://github.com/homeowmorphism/riemann-hypothesis-original C:\rhc
   cd C:\rhc
   git config core.longpaths true
   git config core.autocrlf false
   git sparse-checkout init --no-cone
   ```
   Write the sparse patterns as `/lakefile.toml`, `/lake-manifest.json`, `/lean-toolchain` and `/scripts/`, followed by one line per entry of `closure-files.txt` with a leading `/`. Load them with `git sparse-checkout set --no-cone --stdin`, then run `git checkout`.
   - Verify that `git rev-parse HEAD` is `4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e`.
   - Verify that `git rev-parse HEAD:src` is `24df20b62d9976ccd20da819bc20b16f808f0fdd`.
   - Verify that the 307 files are present. Report the count of `.lean` files under `src`.

3. **Toolchain.** `lean-toolchain` must say `leanprover/lean4:v4.33.1`. Use the existing pinned binary. Record the output of `lean --version` and `lake --version`.

4. **Get Mathlib.**
   ```powershell
   $env:LEAN_ABORT_ON_PANIC = "1"
   $env:LAKE_ARTIFACT_CACHE = "false"
   $env:MATHLIB_CACHE_GET_URL = "https://cache.mathlib.org/mathlib4"
   lake exe mathlib/cache get
   ```
   This fetches Mathlib at the manifest rev `0df444a360eaa60ab8c11dca51a86af692955474` together with Mathlib's compiled files. Report the bytes used on C: afterwards.
   If Lake first tries to build the repo's `cache` executable from `scripts/` and fails, report the exact error. You may instead run Mathlib's cache tool from inside `.lake/packages/mathlib` with `lake exe cache get`, using the same environment variables.

5. **Build only the closure.**
   ```powershell
   lake build Formalism.SharpRestriction.GlobalTheoremInputs 2>&1 | Tee-Object build-closure.log
   ```
   Report the number of modules built, wall time and peak memory if you can see it. Report the last 40 lines of the log. Mathlib should show as already built. If anything in Mathlib recompiles, report that.

6. **Compile our file.** Copy `CommonPeriodMap.lean` into the project root as `C:\rhc\CommonPeriodMap.lean`, outside `src/`, so that it is not part of the library.
   ```powershell
   lake env lean CommonPeriodMap.lean 2>&1 | Tee-Object common-period-map.out
   ```
   Paste the full output into the report.
   - **Success** means no errors, and the four `#print axioms` lines show only `propext`, `Classical.choice` and `Quot.sound`, in any subset. Both `besS_eq` and `KD_eq` are `rfl` lemmas, so "does not depend on any axioms" is also fine for them.
   - **If there are errors:** fix only proof bodies or elaboration details (implicit arguments, `rw` versus `simp only`, coercions, names) in `CommonPeriodMap.lean`. Log every edit as a diff with the reason, and re-run. If a fix would require changing any statement, stop and report the exact error.

7. **Record the final file.** Report the sha256 of the final `CommonPeriodMap.lean`. If it changed, also commit the edited copy back to `rh-extraction\CommonPeriodMap.lean` and keep the original as `CommonPeriodMap.orig.lean`.

8. **Keep the build.** Leave `C:\rhc` in place, because follow-up lemmas will reuse it. Report its total size.

**Output:** `rh-extraction\compile-closure-check.md`. Include the commit, source tree, toolchain, Mathlib rev, disk before and after, timings, the full Lean output and the final hash. Label each claim READ, DERIVED or COMPILED as before.

## Part B: only if Part A passes

Do Part B of `codex-prompt-common-period-map.md`, the classical identification of `s.HH`, `Cu`, `Pu` and `c0`. Output it to `period-map-classical.md`.

## Part C: only if Part A passes (the next lemma)

Codex's last report found that our lemma covers (8a), lattice inclusion, and the Gram bound. It does not cover H8's third section, (8c): an image-rank bound for the *same* map. Find where the headline proof derives its rank or codimension estimate from the Gram bounds for `Pu`. Candidates are `blockReal_at_of` (TopDensityNGeSixteen.lean:1283), `matKF_of` (:1348), `frame_at_of` (:538) and `FrameReal_at` (:519).

Report:
- the exact statement it proves;
- whether that statement is about `D.s.Pu u` or already about `D.div.Bk u`;
- whether it can be added as a fourth conjunct of `RHX.common_period_map`, using only the premises the headline proof already supplies for the same family member.

If it can be added, draft the extended theorem as `CommonPeriodMap2.lean` in the same style, compile it in `C:\rhc` the same way, and report the result. Do not change the original file.

**Output:** `rh-extraction\rank-section-check.md`.
