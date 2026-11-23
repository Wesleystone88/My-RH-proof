# One map, three sections: Lean checks on the Alpöge–Claude proof of RH

**Timothy Wesley Stone** (Noesis Lab), working with Claude (Anthropic). Codex and GPT were used as tools.
Everything is here on purpose: the prompts, the handoff notes, the dead ends and the corrections.

**Main write-up:** [paper/](paper/).

## Results

| File | What it shows | Status |
| --- | --- | --- |
| [`CommonPeriodMap.lean`](results/common-period-map/CommonPeriodMap.lean) | The integral map `Bk` used by the divisibility argument equals, up to a nonzero scalar and two isometries, the matrix coefficients of the period map `Pu` used by the rank argument. On the headline family, the same map satisfies the lattice inclusion and the near-isometry (Gram) bound. | **COMPILED**, 23 Nov 2026. Output in [`common-period-map.out`](results/common-period-map/common-period-map.out) |
| [`CommonPeriodMap2.lean`](results/common-period-map/CommonPeriodMap2.lean) | `one_map_three_sections`: from the headline proof's own premises, every member of the family eventually satisfies all three of Rubinstein's H8 conditions for the same map `Bk`: (8a) lattice inclusion, (8b) the height bound, (8c) its archimedean matrix being a block of a near-orthogonal frame (`MatK_at`, the shape of Zhang's Prop. 4.3). | Written; **compile pending**. The first build attempts failed on file-read errors in Mathlib's cache files, not on the proof. |
| [`gap2_lemniscate_check.py`](results/gap2-test-bench/gap2_lemniscate_check.py) and [`gap2_lemniscate_results.txt`](results/gap2-test-bench/gap2_lemniscate_results.txt) | Independent recomputation of Rubinstein's worked lemniscate example and of his failing naive theta kernel. All of his numbers reproduce exactly. New: the naive kernel's p-divisibility grows like n/(p²−1) instead of the needed np/(p²−1), which is exactly one factor of p short (checked for n ≤ 300, p = 3, 7, 11, 19). | **COMPUTED**. The new pattern is numerical, not proved. |

Lean output for the compiled file (verbatim from `common-period-map.out`):

```
'RHX.besS_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.KD_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.common_period_map' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.common_period_map_family' depends on axioms: [propext, Classical.choice, Quot.sound]
```

These are the three standard axioms, and nothing else.

## Scope: what this does and does not claim

- **The proof is not mine.** It belongs to **Levent Alpöge and Claude**, and was certified by the **Lean and Mathlib communities** on 21 November 2026.
- **The two Lean files add no new mathematics.** They package, as single checked statements, facts the source already proves (`matKF_of`, `LinkDIV_at`, `BesselId`). Their value is that they answer a specific question an expert raised (H8 and O25(e)) with a machine-checked statement.
- **The classical dictionary is still open.** Nothing here identifies the abstract period map with the classical theta-lift objects in textbook terms. Adriazola's manuscript (§19, Hypotheses H-dict and H-rat) lists this as open too.
- **The "one factor of p" pattern is numerical, not proved.** It was observed for n ≤ 300 and p = 3, 7, 11, 19.
- **There is no human-readable proof of RH here.** That is the long-term goal; it is not finished.

Pinned source: [`homeowmorphism/riemann-hypothesis-original`](https://github.com/homeowmorphism/riemann-hypothesis-original) at commit `4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e`. Its `src` tree is `24df20b62d9976ccd20da819bc20b16f808f0fdd`, the same tree as upstream `e50d098`. Lean 4.33.1. **The source is not copied into this repo.** The compile script fetches exactly that commit.

## Credit

- The questions come from **Michael O. Rubinstein's** draft. H8 ("one map, three sections"), O25, H12, Estimates B and C, and the worked examples of §III.12 are his: [draft v2](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf).
- Lemma 4.2 and Proposition 4.3 are from **Robin Zhang's** note: [GRH note](https://www.ihes.fr/~rzhang/files/GRH%20note.pdf).
- **Jimmie Adriazola's** reconstruction already gives the window and auxiliary-prime structure in conventional terms (§18): [repository](https://github.com/jimjamzola/RH-Alpoge-Reconstruction).

## How this was done

I directed Claude, Codex and GPT. I am not claiming to have written the Lean by hand. Every claim in the notes is labeled one of:

- **READ**: read directly from the pinned source.
- **DERIVED**: worked out by reasoning from what was read.
- **COMPUTED**: produced by running a script.
- **COMPILED**: checked by Lean.

The prompts I gave are in [`prompts/`](prompts/) and the full investigation log is [`notes/RH-proof-handoff.md`](notes/RH-proof-handoff.md), so the whole process can be audited. Mistakes and corrections are kept on purpose.

## Map of the folders

| Folder | What is in it |
| --- | --- |
| [`paper/`](paper/) | The main write-up. |
| [`results/common-period-map/`](results/common-period-map/) | The two Lean files, the compiled output, `compile-closure.ps1`, `closure-files.txt`, the results summary and the latest compile log. |
| [`results/gap2-test-bench/`](results/gap2-test-bench/) | Python recomputation of Rubinstein's lemniscate example, and its results. |
| [`notes/`](notes/) | The handoff log, the expert map, Codex and GPT reports and checks, and `PATHS.md` (old path to new path). |
| [`notes/RH-proof-handoff.md`](notes/RH-proof-handoff.md) | The full investigation log. Start here to audit. |
| [`prompts/`](prompts/) | Prompts given to Codex (saved as files), and a note on prompts given in the Claude chat app. |
| [`lean-experiments/`](lean-experiments/) | Other Lean experiments (`Squarefree.lean` etc.), with their own `lakefile.toml` and `lean-toolchain`. |
| [`scripts/`](scripts/) | Numerical check scripts (`key_minor_check.py`, `lemma22_check.py`, `zero_map_check.py`). |
| [`data/`](data/) | Generated tables from the source (CSV, JSON, zipped). See [`data/README.md`](data/README.md). |
| [`logs/`](logs/) | Build logs. |
| [`archive/`](archive/) | Superseded material. Nothing is deleted. |

## Reproduce it

On Windows, run [`results/common-period-map/compile-closure.ps1`](results/common-period-map/compile-closure.ps1). You need about 25 GB free on C:, and a few hours. It uses no project cache: it checks out only the 705 source files listed in `closure-files.txt` from the pinned commit into `C:\rhc`, downloads Mathlib's own cache, builds those modules from source, and runs Lean on both files. It checks the axioms and writes `compile-log.txt` next to the script. It needs `git` installed; it installs `elan` (the Lean version manager) if missing.

## Licenses

- **MIT** ([LICENSE](LICENSE)): code and Lean files (`.lean`, `.py`, `.ps1`, `lakefile.toml`).
- **CC BY 4.0** ([LICENSE](LICENSE)): notes, prompts, the paper, and data tables.

The Alpöge–Claude source is not included and keeps its own license.

## Citing

See [CITATION.cff](CITATION.cff).

Mistakes are mine to fix. Open an issue.
