# Old paths to new paths

The notes (especially `RH-proof-handoff.md`) and prompts cite the author's original working paths. They were **not rewritten**. Use this table to find the file now.

Original working folder: `XPostCode\rh-extraction\`. Everything below that was in the repo's first commit was under `rh-extraction/`, `HP-Spectral-Discovery/` or the root.

| Old path | New path |
| --- | --- |
| `rh-extraction/CommonPeriodMap.lean` | `results/common-period-map/CommonPeriodMap.lean` |
| `rh-extraction/CommonPeriodMap2.lean` | `results/common-period-map/CommonPeriodMap2.lean` |
| `rh-extraction/common-period-map.out` | `results/common-period-map/common-period-map.out` |
| `rh-extraction/compile-closure.ps1` | `results/common-period-map/compile-closure.ps1` |
| `rh-extraction/closure-files.txt` | `results/common-period-map/closure-files.txt` |
| `rh-extraction/COMMON-PERIOD-MAP.md` | `results/common-period-map/COMMON-PERIOD-MAP.md` |
| `rh-extraction/compile-log.txt` | `results/common-period-map/compile-log.txt` |
| `rh-extraction/gap2_lemniscate_check.py` | `results/gap2-test-bench/gap2_lemniscate_check.py` |
| `rh-extraction/gap2_lemniscate_results.txt` | `results/gap2-test-bench/gap2_lemniscate_results.txt` |
| `RH-proof-handoff.md` | `notes/RH-proof-handoff.md` |
| `HP-Spectral-Discovery/HP-Spectral-Discovery.md` | `notes/HP-Spectral-Discovery.md` |
| `rh-extraction/expert-map.md` | `notes/expert-map.md` |
| `rh-extraction/codex-blackbox-report.md`, `codex-core-report.md` | `notes/` (same names) |
| `rh-extraction/common-period-map-check.md` | `notes/common-period-map-check.md` |
| `rh-extraction/amplifier-{audit,equations,sources,variables}.md` | `notes/` (same names) |
| `rh-extraction/blackbox-map.md` | `notes/blackbox-map.md` |
| `rh-extraction/codex-prompt-*.md` | `prompts/` (same names) |
| `rh-extraction/{DivisibleMeansBig,DvCore,GainCheck,ParityEnergy,ScalarBridge,Squarefree,Theorem2Check,TransferSkeleton,WindowAvoid}.lean` | `lean-experiments/` (same names) |
| `rh-extraction/README.md` | `lean-experiments/README.md` |
| `rh-extraction/lakefile.toml`, `lean-toolchain` | `lean-experiments/` (same names) |
| `rh-extraction/{key_minor_check,lemma22_check,zero_map_check}.py` | `scripts/` (same names) |
| `rh-extraction/{build-closure,lake-version,mathlib-cache}.log` | `logs/` (same names) |
| `rh-extraction/core-*`, `blackbox-*.json`, `usage-*`, `handoff-citations.json`, `interface-witnesses.json` | `data/` (same names; the big `usage-*.csv` are zipped or not included, see `data/README.md`) |

## Cited but not in this repo

- `rh-source/...` (for example `rh-source/src/...`): a local checkout of the pinned Alpöge source. Not committed. Fetch `homeowmorphism/riemann-hypothesis-original` at `4e8bb36faa8c9e3f1bda144ccf5a637f8b96066e`; the file is at the same relative path under `src/`.
- `rh-extraction/rank-section-check.md`, `rh-extraction/compile-closure-check.md`, `rh-extraction/period-map-classical.md`: cited in the notes or prompts, but **no copy was found** when this repo was organized. They may have lived elsewhere or never been saved. Nothing was deleted.
- `C:\rhc`: the Lean build folder created by `compile-closure.ps1`. Not committed (it is tens of GB).
- `lean30/`: the author's separate 30-rule spec check; not part of this repo.
