# data/

Generated tables describing the pinned Lean source (`homeowmorphism/riemann-hypothesis-original` @ `4e8bb36`, src tree `24df20b`). They are inputs to the notes in [`../notes/`](../notes/), not results in themselves.

## Provenance

**No generator script was saved.** These tables came from Codex runs driven by prompts:

- the `core-*` tables and `handoff-citations.json`, `interface-witnesses.json`: [`../prompts/codex-prompt-core.md`](../prompts/codex-prompt-core.md); results described in [`../notes/codex-core-report.md`](../notes/codex-core-report.md)
- the `blackbox-*` tables: [`../prompts/codex-prompt-blackbox.md`](../prompts/codex-prompt-blackbox.md); results described in [`../notes/codex-blackbox-report.md`](../notes/codex-blackbox-report.md)
- the `usage-*` tables are the declaration-reference graph over the whole source, from the same runs; see those two reports.

To regenerate, re-run those prompts against the pinned commit. You will not get a byte-identical file unless the runs do the same thing.

## Known limitation

The reach tables miss **dot-notation calls** (for example `P.wordFacts`), so some links between declarations are missing from them. Where it mattered, those links were **confirmed by reading the source**, and the notes say so. Do not treat the reach tables as complete.

## Large files

GitHub rejects files over 100 MB and warns over 50 MB. These were zipped separately:

| File | Rows | Status |
| --- | --- | --- |
| `usage-nodes.csv` | 1,061,435 lines | zipped: `usage-nodes.csv.zip` (16.5 MB) |
| `usage-files.csv` | 175,189 lines | zipped: `usage-files.csv.zip` (6.1 MB) |
| `usage-refs.csv` | 14,253,295 lines (~302 MB) | **not in this repo** (zip is still 70.9 MB). Listed in `.gitignore`. |

`usage-refs.csv` columns: `from_id,token,target_or_group`. Its SHA-256 on the author's machine is
`0b230d0ab0e6f6f2dfa13fa28082a6ff8bdb8f2f084896846edcf92e6de22eba`. To get it, regenerate it as above, or ask the author.

To unzip: `unzip usage-nodes.csv.zip` (or any zip tool), in this folder.
