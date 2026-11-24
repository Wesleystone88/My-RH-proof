# One map, three sections: Lean checks on the Alpöge–Claude proof of RH

**Timothy Wesley Stone** (Noesis Lab), working with Claude (Anthropic). Codex and GPT were used as tools.
Everything is here on purpose: the prompts, the handoff notes, the dead ends and the corrections.

**Main write-up:** [`paper/alpoge-claude-rh-reading-notes.md`](paper/alpoge-claude-rh-reading-notes.md).

**Status as of 23 Nov 2026: both lemmas compiled; classical dictionary open.**

## Start here

- **A mathematician:** read [`results/common-period-map/COMMON-PERIOD-MAP.md`](results/common-period-map/COMMON-PERIOD-MAP.md), then the [paper](paper/alpoge-claude-rh-reading-notes.md).
- **A Lean user:** run [`compile-closure.ps1`](results/common-period-map/compile-closure.ps1), or read [`CommonPeriodMap2.lean`](results/common-period-map/CommonPeriodMap2.lean).
- **A curious reader:** read the [paper](paper/alpoge-claude-rh-reading-notes.md) and the [investigation log](notes/RH-proof-handoff.md).

## Results

| File | What it shows | Status |
| --- | --- | --- |
| [`CommonPeriodMap.lean`](results/common-period-map/CommonPeriodMap.lean) | The integral map `Bk` used by the divisibility argument equals, up to a nonzero scalar and two isometries, the matrix coefficients of the period map `Pu` used by the rank argument. On the headline family, the same map satisfies the lattice inclusion and the near-isometry (Gram) bound. | **COMPILED**, 23 Nov 2026. Output in [`common-period-map.out`](results/common-period-map/common-period-map.out) |
| [`CommonPeriodMap2.lean`](results/common-period-map/CommonPeriodMap2.lean) | `one_map_three_sections`: from the headline proof's own premises (`LinkDIV`, `LinkS`, `ChosenProviso`), every member of the family eventually has one map `Bk` carrying (8a) the lattice inclusion, (8b) the height bound and (8c) a Zhang-style block form (`MatK_at`, the shape of Zhang's Prop. 4.3). This holds because the source states all three conditions for the single object `Bk`. It does **not** state Rubinstein's H8 inequality (III.330), and it does not connect his three maps to `Bk`. The source states (III.330) as `Frame_at` (QuadraticLogDerivCongr.lean:188–193) and `FrameF` (:258). Audit: **different** ([batch1-audit](notes/batch1-audit.md)). | **COMPILED**, 23 Nov 2026. Output in [`common-period-map2.out`](results/common-period-map/common-period-map2.out). Earlier build attempts failed on file-read errors in Mathlib's cache files (8 parallel Lean workers); a rerun with 2 workers succeeded. |
| [`gap2_lemniscate_check.py`](results/gap2-test-bench/gap2_lemniscate_check.py) and [`gap2_lemniscate_results.txt`](results/gap2-test-bench/gap2_lemniscate_results.txt) | Independent recomputation of Rubinstein's worked lemniscate example and of his failing naive theta kernel. All of his numbers reproduce exactly. New: for the naive kernel, v_p(r_k) stays within 2 of n/(p²−1) for every n ≤ 300 at p = 3, 7, 11, 19, and far below the needed np/(p²−1). The match is most telling at p = 3; at p = 11 and 19 both values stay small. | **COMPUTED**. The new pattern is numerical, not proved. |
| [`results/rubinstein-hypotheses/`](results/rubinstein-hypotheses/) `H0`–`H12` (H8 is `CommonPeriodMap2.lean`, above) | Family-level Lean statements for twelve of Rubinstein's hypotheses on the headline family, taking premises supplied along the headline proof. Compiled does not mean matching. Across all 13 hypotheses (H8 is `CommonPeriodMap2.lean`), the audits ([batch 1](notes/batch1-audit.md), [batch 2](notes/batch2-audit.md)) find: **same** H1, H2, H3, H4, H5, H6, H9 (7); **weaker** H0, H12 (2); **different** H7, H8, H10, H11 (4). **What "same" means:** in H1, H2, H3, H9, H6(i), (8a) and (8b) the conclusion is one conjunct of the premise `LinkDIV`, so these files show where each hypothesis sits in the code, not a new proof of it. Only H6(ii)(iii) and (8c) go through real source theorems. Details in the [folder README](results/rubinstein-hypotheses/README.md). | **COMPILED**, 23–24 Nov 2026: H1, H2, H3, H6, H9, H0, H4, H5, H7, H10, H11, H12. Outputs `H*.out` (axioms: `propext`, `Classical.choice`, `Quot.sound`). |

Lean output for the compiled files (verbatim from `common-period-map.out` and `common-period-map2.out`):

```
'RHX.besS_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.KD_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.common_period_map' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.common_period_map_family' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.one_map_three_sections' depends on axioms: [propext, Classical.choice, Quot.sound]
```

These are the three standard axioms, and nothing else.

## Scope: what this does and does not claim

- **The proof is not mine.** It belongs to **Levent Alpöge and Claude**, and was certified by the **Lean and Mathlib communities** on 21 November 2026.
- **The two Lean files add no new mathematics.** They package, as single checked statements, facts the source already proves (`matKF_of`, `LinkDIV_at`, `BesselId`). Their value is that they put a specific question an expert raised (H8 and O25(e)) into machine-checked form: one map `Bk` carries the three conditions together in the source's own records. They do not answer his question whether his three maps are one map, and `CommonPeriodMap2.lean` does not state his inequality (III.330); see the [batch 1 audit](notes/batch1-audit.md).
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
| [`paper/`](paper/) | The main write-up, [`alpoge-claude-rh-reading-notes.md`](paper/alpoge-claude-rh-reading-notes.md). |
| [`results/common-period-map/`](results/common-period-map/) | The two Lean files, the compiled output, `compile-closure.ps1`, `closure-files.txt`, the results summary and the latest compile log. |
| [`results/gap2-test-bench/`](results/gap2-test-bench/) | Python recomputation of Rubinstein's lemniscate example, and its results. |
| [`notes/`](notes/) | The handoff log, the expert map, Codex and GPT reports and checks, and `PATHS.md` (old path to new path). |
| [`notes/RH-proof-handoff.md`](notes/RH-proof-handoff.md) | The full investigation log. Start here to audit. |
| [`notes/batch1-audit.md`](notes/batch1-audit.md), [`notes/batch2-audit.md`](notes/batch2-audit.md) | The audits of H0–H12 (H8 is `CommonPeriodMap2.lean`) against Rubinstein v2: 7 same, 2 weaker, 4 different. |
| [`notes/zeta-bridge.md`](notes/zeta-bridge.md) | Test of Nielsen's claim that the zeta link is supplied by definition. Not supported for the zeta link; the limits of what was read are in the note. |
| [`prompts/`](prompts/) | Prompts given to Codex (saved as files), and a note on prompts given in the Claude chat app. |
| [`lean-experiments/`](lean-experiments/) | Other Lean experiments (`Squarefree.lean` etc.), with their own `lakefile.toml` and `lean-toolchain`. |
| [`scripts/`](scripts/) | Numerical check scripts (`key_minor_check.py`, `lemma22_check.py`, `zero_map_check.py`). |
| [`data/`](data/) | Generated tables from the source (CSV, JSON, zipped). See [`data/README.md`](data/README.md). |
| [`logs/`](logs/) | Build logs. |
| [`archive/`](archive/) | Superseded material. Nothing is deleted. |

## Reproduce it

On Windows, run [`results/common-period-map/compile-closure.ps1`](results/common-period-map/compile-closure.ps1). You need about 25 GB free on C:, and a few hours. It uses no project cache: it checks out only the 705 source files listed in `closure-files.txt` from the pinned commit into `C:\rhc`, downloads Mathlib's own cache, builds those modules from source, and runs Lean on both files. (If you see "failed to read file" errors on Mathlib `.olean` files, retry with `LEAN_NUM_THREADS=2`; see `logs/build-retry.log`.) It checks the axioms and writes `compile-log.txt` next to the script. It needs `git` installed; it installs `elan` (the Lean version manager) if missing.

## Licenses

- **MIT** ([LICENSE](LICENSE)): code and Lean files (`.lean`, `.py`, `.ps1`, `lakefile.toml`).
- **CC BY 4.0** ([LICENSE](LICENSE)): notes, prompts, the paper, and data tables.

The Alpöge–Claude source is not included and keeps its own license.

## Citing

See [CITATION.cff](CITATION.cff).

Mistakes are mine to fix. Open an issue.
