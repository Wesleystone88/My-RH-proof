# One map, three sections: Lean checks on the Alpöge–Claude proof of RH

**Timothy Wesley Stone** (Noesis Lab), working with Claude (Anthropic). Codex and GPT were used as tools.
Everything is in this folder on purpose: the prompts, the handoff notes, the dead ends and the corrections. You can see how every claim here was checked.

## What this is

On 20 November 2026 Levent Alpöge released a Lean proof of the Riemann Hypothesis, and the Lean community certified it on 21 November. The proof is 17 million lines that nobody has read end to end. The experts writing human accounts (Rubinstein, Zhang, Adriazola) each flag points they could not yet check.

This folder works on those points by reading the Lean source at a pinned commit and proving small statements in Lean about what it actually does.

## Results

| File | What it shows | Status |
| --- | --- | --- |
| `CommonPeriodMap.lean` | The integral map `Bk` used by the divisibility argument equals, up to a nonzero scalar and two isometries, the matrix coefficients of the period map `Pu` used by the rank argument. On the headline family, the same map satisfies the lattice inclusion and the near-isometry (Gram) bound. | **COMPILED**, 23 Nov 2026. Output in `common-period-map.out` |
| `CommonPeriodMap2.lean` | `one_map_three_sections`: from the headline proof's own premises, every member of the family eventually satisfies all three of Rubinstein's H8 conditions for the same map `Bk`. These are (8a) lattice inclusion, (8b) the height bound, and (8c) its archimedean matrix being a block of a near-orthogonal frame (`MatK_at`, the shape of Zhang's Prop. 4.3). | **COMPILED**, 23 Nov 2026. Output in `common-period-map2.out`. Earlier builds failed on file-read errors in Mathlib cache files, not on the proof. |
| `gap2_lemniscate_check.py` and `gap2_lemniscate_results.txt` | Independent recomputation of Rubinstein's worked lemniscate example and of his failing naive theta kernel. All of his numbers reproduce exactly. New: the naive kernel's p-divisibility grows like n/(p²−1) instead of the needed np/(p²−1), which is exactly one factor of p short (checked for n ≤ 300, p = 3, 7, 11, 19). | COMPUTED. The new pattern is numerical, not proved. |

Lean output for the compiled file:

```
'RHX.besS_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.KD_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.common_period_map' depends on axioms: [propext, Classical.choice, Quot.sound]
'RHX.common_period_map_family' depends on axioms: [propext, Classical.choice, Quot.sound]
```

These are the three standard axioms, and nothing else.

## What this does not claim

- **The two Lean files add no new mathematics.** They package, as single checked statements, facts that the source already proves (`matKF_of`, `LinkDIV_at`, `BesselId`). Their value is that they answer a specific question an expert raised, H8 and O25(e), with a machine-checked statement.
- **The classical dictionary is still open.** Nothing here identifies the abstract period map with the classical theta-lift objects in textbook terms. Adriazola's manuscript (§19, Hypotheses H-dict and H-rat) lists this as open too.
- **We do not give a human-readable proof of RH.** The end goal is a short readable account of how the proof works. It is not finished.

## Reproduce it

Pinned source: `homeowmorphism/riemann-hypothesis-original` at `4e8bb36`. Its `src` tree is `24df20b`, the same tree as upstream `e50d098`. Lean 4.33.1.

On Windows, run `compile-closure.ps1`. It needs no project cache. It builds from source only the 705 modules these files import (listed in `closure-files.txt`), using Mathlib's own cache, then runs Lean on both files and checks the axioms. It needs about 25 GB free on C:.

## Credit

- The proof belongs to **Levent Alpöge and Claude**. It was certified by the **Lean and Mathlib communities** on 21 November 2026.
- The questions come from **Michael O. Rubinstein's** draft. H8 ("one map, three sections"), O25, H12, Estimates B and C, and the worked examples of §III.12 are his: [draft v2](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf).
- Lemma 4.2 and Proposition 4.3 are from **Robin Zhang's** note: [GRH note](https://www.ihes.fr/~rzhang/files/GRH%20note.pdf).
- **Jimmie Adriazola's** reconstruction already gives the window and auxiliary-prime structure in conventional terms (§18): [repository](https://github.com/jimjamzola/RH-Alpoge-Reconstruction).

Mistakes are mine to fix. Open an issue.
