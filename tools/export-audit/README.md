# export-audit: is a structure field ever opened?

Version 2 of the scanner behind [`notes/anygeometry-export-scan.md`](../../notes/anygeometry-export-scan.md). It reads a Lean kernel export (lean4export format 3.1.0) in one pass, **without building anything**, and says for each field of the structures you name whether any proof actually opens it.

Timothy Wesley Stone, with Claude (Opus, chat), 25 Nov 2026. Extends `results/anygeometry-check/export_scan.py`. The ideas are in [`ideas/load-bearing-audit.md`](../../ideas/load-bearing-audit.md). JackyReaps' [`meta-codex`](https://github.com/jackyreaps/meta-codex) (`#audit_fields`) does a related check inside a built Lean project; this one works on an export file instead, so it needs only Python.

## The picture

A field is a drawer in a cabinet. The tool reports one of three things for each drawer:

| Label | Meaning |
|---|---|
| **OPENED IN PROOF** | some proof or definition body pulls the field out |
| **MENTIONED ONLY** | the field appears only in what theorems *state*, never in a proof |
| **UNOPENED** | the field never appears (outside the structure's own auto-generated declarations) |

For every opening it names the declaration and how the field is used there:

- **re-wrapped**: it goes straight into a constructor (packed into another structure). All openings re-wrapped = a transport candidate, still to be checked by hand.
- **passed on**: it is handed to a function or theorem. Follow that one by hand.
- **used directly**: it is returned or bound as it is.

It also lists declarations that take the whole structure apart (`rec`, `casesOn`, …), which unpacks every field at once, and checks that an "always true" predicate such as `anyGeometry` really has the body `fun … => True`.

## Use

```
python export_audit.py --self-test
zstd -dc --long=30 solution.ndjson.zst | python export_audit.py ^
    --struct GlobalTheory.Mem.Top.Bl.OAt ^
    --true-pred GlobalTheory.Mem.Top.Bl.anyGeometry ^
    --expect GlobalTheory.Mem.Top.Bl.OAt.lam=OPENED ^
    --out audit.json --md audit.md
```

(`^` continues a line in Windows `cmd`; use `\` in bash.) Repeat `--struct`, `--true-pred` and `--expect` as needed. `--input FILE` reads a plain `.ndjson` file instead of standard input.

## Controls

A "never opened" means nothing unless the tool is shown to see an opening. So:

1. **Self-test before every run.** The script refuses to run if its self-test fails. The self-test uses a hand-built export (`tests/fixture.ndjson`) with known answers: field `a` opened and passed on (both as `S.a s` and as a raw projection), `b` mentioned only, `c` unopened, `d` re-wrapped only, the structure taken apart in one declaration, one always-true predicate and one decoy.
2. **Positive control.** Adding a use of `c` (`tests/fixture_use_c.ndjson`) must flip `c` to OPENED.
3. **Negative control.** A deliberately wrong `--expect` must make the run VOID (exit code 2).
4. **Real control.** On a real export, pass a field you know is opened with `--expect`. For the RH export, `OAt.lam` is read at ParameterOfDiscreteSeriesRay:107 (removal map). If the tool does not see it, the run is VOID.

## Checked (25 Nov 2026)

- **Self-test:** 14 of 14 checks pass.
- **Deliberate breakage:** six versions of the tool were broken on purpose (accessor uses not tracked, the structure's own declarations counted as openings, projections ignored, statements merged with proofs, constructors not recognised, always-true bodies not tracked). The self-test reported FAIL for every one.
- **End to end:** the command line on the test export writes the expected JSON and Markdown, exits 0 with correct controls and 2 with a wrong one.
- **Speed:** on a 3-million-line synthetic stream it took 4.1 s against 3.1 s for the old scanner (about 30% slower). The old scanner took 2 h 33 min on the RH export, so expect roughly 3½ hours there. Memory: about 1 byte per expression (roughly 1 GB for the RH export); `--no-transport` skips that and the re-wrapped/passed-on split.

## Limits

- **The test export is hand-built**, following lean4export's documented 3.1.0 format and the line shapes the old scanner parsed on the real file. It is not output from lean4export itself. The real-control run below is what confirms the tool on a real export.
- **Taking a structure apart** (`casesOn`, `match`) is reported per declaration; which of the unpacked fields that branch then uses is not determined in export mode.
- **Always-true check** confirms the predicate's body. It does not check that every instance of the structure uses that predicate.
- **Re-wrapped vs passed on** looks only at the field's immediate surroundings. A field passed to a function that itself just re-wraps it shows as "passed on"; that is why those are flagged for a hand check.
- **Whole export only.** It reports on everything in the export. Narrowing to a smaller theorem (like `ch_top`) is not done here; `results/anygeometry-check/DependsOn.lean` does that inside a build.

## First real run (pre-registered, not yet run)

On Sutherland's export, with the command above. Written before running:

- `OAt.lam`: OPENED IN PROOF (the control; otherwise VOID).
- `OAt.geo`: OPENED IN PROOF only in `divEx_geoCl` and `oAt_setDiv`, the two declarations the old scan found. PASS if both are "re-wrapped" or "used directly". If either is "passed on", follow it by hand before saying anything.
- `anyGeometry`: body is `fun … => True`.
