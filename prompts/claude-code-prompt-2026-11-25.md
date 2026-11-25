# Claude Code: check the actual proof terms for any use of the geometry stamp (25 Nov 2026)

Written by Claude in chat. **No Lean, no builds, no `lake`, nothing written in `C:\rhc`.** This is a download plus a streaming scan.
Standing rules still apply: stop if C: would drop below 25 GB free; one heavy process at a time.

## Why

`notes/anygeometry-removal-map.md` found, by reading the source text, zero real readers of the `geo` field of `OAt` (the "stamp" filled by `anyGeometry`), and no case analysis on `GeoCl`. Text search can miss things. The kernel did not check source text; it checked the exported proof terms. Andrew Sutherland publishes that exact export:

- https://math.mit.edu/~drew/grh/solution.ndjson.zst (7,699,933,588 bytes; compressed sha256 `61a8938ad5f5e57397c1c0e3b954916af546d9004ade01c3555744a681b05381`; unpacked sha256 `5ea74b912147c5c93cc2b6d70cc727cf908df2f62ac6a20480a3fa02f6be244e`, 61,570,595,788 bytes). It is the lean4export (tag v4.33.0) output for module `Main`: only the declarations the five headline theorems depend on.
- Decompression needs `--long=30` (zstd) or an equivalent window setting.

Scanning it answers the question at the level the kernel works at, with no rebuild.

## Pre-registered outcomes (write these at the top of the note before scanning)

- **PASS:** no declaration in the export uses an eliminator of `GeoCl` (`GeoCl.rec`, `GeoCl.casesOn`, `GeoCl.recOn`, `GeoCl.below`, `GeoCl.brecOn`, or any `match`/aux definition built on them), other than the auto-generated declarations of `GeoCl` itself; **and** every use of `OAt.geo` (the projection constant, or a primitive projection `proj` on structure `OAt` with index 0) sits in a declaration that only passes the value into a `GeoCl` constructor or into another `OAt`.
- **FAIL / finding:** any `GeoCl` eliminator use, or any `OAt.geo` use in a declaration that is not pass-through. Report it with the declaration name. That would be a real result, not a failure of the task.

## Tasks

1. **Download and verify** the compressed file's sha256. Do not unpack it to disk (61.5 GB would not fit); decompress as a stream. Check free RAM first and say how much the scan used.
2. **Learn the format** from the first few thousand lines: how names, expressions (`const`, `proj`, `app`, `lam`, …) and declarations are encoded, and whether expression ids are emitted children-before-parents. Quote a few example lines.
3. **Find the target names**: the full names of `OAt`, `OAt.geo`, `OAt.lam`, `OAt.mk`, `OAt.rec`, `OAt.casesOn`, `GeoCl`, `GeoCl.base`, `GeoCl.step`, `GeoCl.rec`, `GeoCl.casesOn`, `GeoCl.recOn`, `anyGeometry`, `geoCl`, `geoCl_of`. Say which are present in the export at all (absence means nothing the five theorems depend on uses them).
4. **Scan once, streaming.** Mark every expression node that is (a) a `const` of `OAt.geo` or of any `GeoCl` eliminator, or (b) a `proj` on `OAt` with index 0. If ids are emitted bottom-up, propagate "contains a marked node" to parents in the same pass (a bitset over expression ids), so that each declaration whose type or value contains a mark can be listed. If the format makes that impractical, say so and list what you can.
5. **For every declaration containing a mark**: its name, whether it is auto-generated for `OAt`/`GeoCl`, and (by reading its source at `4e8bb36`) whether the marked use is pass-through or real. Compare with the list in `notes/anygeometry-removal-map.md` §2.3 (expected pass-throughs: `divEx_geoCl`, `oAt_setDiv`).
6. Also count, for context, how many declarations in the export mention `anyGeometry` and `OAt.lam`.

Write to `notes/anygeometry-export-scan.md`, with the scanning script saved as `results/anygeometry-check/export_scan.py` (or similar) so anyone can rerun it. Keep the downloaded file outside the repo and do not commit it.

## Last step

Commit and push the note, the script and this prompt file, saying Claude Code wrote the note and script and Claude in chat wrote the prompt. Report PASS or FAIL against the pre-registered outcomes, with the declaration list.
