# Claude Code: map everything `anyGeometry` touches, and what could replace it (24 Nov 2026, evening)

Written by Claude in chat. **Reading only.** No builds, no `lake`, no edits to the source, no git until the last step. Reading the pinned source in `C:\rhc` or from GitHub at `4e8bb36` is fine; write nothing there.
Source: `4e8bb36` of homeowmorphism/riemann-hypothesis-original (src tree = upstream `e50d098`).
Label every claim **READ**, **DERIVED** or **GUESS**. Either answer is fine everywhere. If something *does* read the geometry, that is a result, not a failure.

## Why

`anyGeometry : GeoP := fun _ _ _ => True` (OverIx.lean:19) is the line critics point at. Simply deleting it or setting it to `False` breaks the build and proves nothing. The informative question is whether the proof ever **reads** the geometry certificate. If nothing reads it, the whole slot could be removed (not replaced by another geometry) and the proof should still go through. This task maps that, so the claim is checked rather than guessed. Start from `notes/anygeometry-footprint.md` (Codex) and do not redo what it already establishes; extend it.

## Tasks

1. **Every occurrence.** List every occurrence of `anyGeometry` in the source (critics count about 118 in 24 files). For each: file:line, enclosing declaration, and kind: (a) definition, (b) passed as a `GeoP` argument (e.g. to `geoCl`), (c) appears in a type or statement, (d) other.
2. **Who builds the certificate, who reads it.** For `GeoCl`, `geoCl`, `GeoOver`, `GeoTiedP` and every structure field whose type is one of these (e.g. the `geo` field in `DivEx`/`DivX`/`HypsAlt`/`OAt`, `.div.geo`):
   - **Constructors:** where values are built (e.g. `GeoCl.base trivial`, `geo := geo`).
   - **Readers:** any place that eliminates or uses such a value: `cases`, `induction`, `match`, `rcases`/`obtain` followed by a later use of the bound name, `.rec`/`casesOn`, projections like `.geo` or `.1` that are then passed into another proof. For each reader, say whether the use is real (the proof needs a property from it) or pass-through (stored again or ignored).
   - Check Nielsen's claims directly: that no proof does case analysis or induction on `GeoCl`; that `GeoTiedP.geoTied`, `GeoTiedP.formsTieX`, `geoOf_surf` are never called.
3. **The replacement, per use.** For each occurrence and each reader: "delete (never read)", or "needs property P" with P stated. If every use is delete, say so plainly: the slot is removable in principle.
4. **How big a rebuild would be.** Parse `import` lines to compute the set of modules that transitively import `OverIx.lean` (and separately `EveryCharacterE.lean`). Report the counts, and how many of them are in the import closure of `src/Main.lean`. This is the number of modules someone would have to recompile to test the removal.
5. **A patch sketch, not applied.** If removal looks possible, describe the minimal set of edits (which structures lose a field, which constructors drop an argument), as text in the note. Do not edit any `.lean` file.

Write everything to `notes/anygeometry-removal-map.md`.

## Last step

Commit and push `notes/anygeometry-removal-map.md` and this prompt file, saying Claude Code wrote the note and Claude in chat wrote the prompt. Report: the count of occurrences, the count of real readers, the removable-or-not verdict, and the rebuild size.
