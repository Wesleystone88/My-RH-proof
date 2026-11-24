# anyGeometry kernel check

`DependsOn.lean` walks the constants a declaration uses, transitively, through the environment's
`ConstantInfo` types and values, and reports whether `anyGeometry` is reached. Output is in
`DependsOn.out`.

**How it was run** (one Lean process at a time, in `C:\rhc`, pinned 705-module closure plus the
104-module H12 supplement, `LEAN_NUM_THREADS=2`):

1. Compile each control file to an `.olean` so it can be imported:
   `lake env lean -o ctrl\X.olean X.lean` for `CommonPeriodMap`, `CommonPeriodMap2`, `H1`, `H2`,
   `H3`, `H4`, `H5`, `H6`, `H7`, `H9`.
2. Run `lake env lean DependsOn.lean` with `C:\rhc\ctrl` added to `LEAN_PATH`.

**What this can and cannot show.** `anyGeometry` is defined in `OverIx.lean`, which is not in the
build. If a module is not loaded, nothing in the environment can mention the constants it defines.
The first lines of `DependsOn.out` report whether `OverIx` and `EveryCharacterE` are loaded, so a
"not reached" result can be read for what it is. This checks the *definitions* of the five premises
(`LinkDIV`, `LinkS`, `ChosenProviso`, `TopG`, `VWin`) and our own theorems. It does **not** check the
declarations that *supply* those premises for the headline family; those live in modules that
import `OverIx`. Checking them needs `OverIx` and its dependents built, which is a large build and
was not started without asking. The positive control at the end shows the walker does report a
dependency when one exists.

See [`../../notes/anygeometry-footprint.md`](../../notes/anygeometry-footprint.md) for the
source-level reading this complements.

## Result (24 Nov 2026)

From [`DependsOn.out`](DependsOn.out):

- `OverIx` loaded: **false**. `EveryCharacterE` loaded: **false**. Constants named `*.anyGeometry` in
  the environment: **0** (11,831 modules loaded).
- The definitions of `LinkDIV`, `LinkS`, `ChosenProviso`, `TopG` and `VWin`: `anyGeometry` **not reached**.
- Controls `RHX.one_map_three_sections`, `RHX.common_period_map`, `RHX.common_period_map_family`,
  `RHX.h1_pairing_size`, `h2`, `h3`, `h4`, `h5`, `h6`, `h7`, `h9`: `anyGeometry` **not reached**.
- Positive control: from `RHX.h1_pairing_size` and `RHX.h6_glued_lattice` the walker does reach
  `LinkDIV`, so it detects a dependency when there is one.

**Read this honestly.** Every "not reached" above is guaranteed by the imports: `anyGeometry` does
not exist in this environment. These results confirm that our theorems and the premise definitions
do not import `OverIx`, which matches the closure-list check in
`notes/anygeometry-footprint.md`. They say nothing about whether the declarations that *supply* the
premises for the headline family use `anyGeometry`; Codex's note reads that the supply for
`LinkDIV` goes through the filter. Checking that kernel-side needs `OverIx` and its dependents built
(a large build). Not done; it needs your go-ahead.
