# Task for Codex: map the black boxes in the RH Lean proof and open two of them

You are helping Timmy and Claude understand which parts of Alpöge's Lean proof of the Riemann Hypothesis actually do the work. Claude is attacking a different box at the same time, as described under "Split of work" below.

## Where things are

- Repo: `XPostCode/rh-source`, commit `e50d09817ad81469f737e8f637561e6ccf86c670`. Check it with `git -C rh-source log -1`. Lean files are under `rh-source/src`.
- Shared notes: `XPostCode/RH-proof-handoff.md`. Read Addenda 13–21 first. They hold the current map: the window argument, the √x balance, the lattice "squeeze", Chowla–Selberg, `key_minor_dvd`, Bost's slope inequality, and the multiplicity bookkeeping.
- Black-box map: `XPostCode/rh-extraction/blackbox-map.md`, giving directory sizes and how much of each the handoff has read.
- Outside guide: `proof-guide.pdf`, cross-referenced in Addendum 18.

**Do not edit `RH-proof-handoff.md`.** Claude merges results into it. Write everything to `XPostCode/rh-extraction/codex-blackbox-report.md`, plus any data files you make (JSON/CSV) in `XPostCode/rh-extraction/`.

## Hard facts about this repo

- 175,187 files and 17.4M lines of Lean, with no comments. Every file is in `Main`'s import closure, so import closure is useless for finding what is used.
- It cannot be built locally: the build takes 7–10 h on 48 cores and 503 GB of RAM, and the export is 61 GB. Work from the text.
- Names repeat a lot: at least 15 different `KudlaFamilyStatement`, many `Conclusion1`, three `structure Loc`. Always identify a declaration by namespace plus file path, and quote its actual statement. Never trust a name to describe content.
- `kexactB` and `kcopy` (67 files) skip the elaborator's type check; the kernel still checks them. Treat the stated type as the only reliable description.

## Task 1 (main): an approximate usage graph from `riemannHypothesis`

1. Index every declaration (`theorem`, `lemma`, `def`, `abbrev`, `structure`, `class`, `instance`, `inductive`) with its fully qualified name. Track `namespace` / `section` / `end`, and record each file's `open` lines.
2. For each declaration, collect the identifier tokens in its signature and body. Resolve each token, in this order:
   - (a) the current namespace and its parents;
   - (b) opened namespaces;
   - (c) a globally unique short name;
   - otherwise record it as ambiguous, keeping the candidates.
3. Breadth-first search from `riemannHypothesis` in `src/Main.lean`. Follow resolved edges. For ambiguous ones, follow all candidates but flag them.
4. If declaration level is too slow, fall back to file level: file A uses file B if A references a name declared in B that resolves uniquely.

Report:

- the number of reachable declarations and files, and the lines reachable vs total;
- the top 30 depth-3 and depth-4 directories by **reachable** lines, each marked with how many of its files are cited in the handoff (that is our "unread" measure);
- the 40 "interface" propositions on the path. These are `def … : Prop` that are passed as hypotheses on the headline chain and proved far away, typically named `*Statement`, `*Holds`, `Hyp*`, `*Inputs`, `Closed*`, `Link*`. For each give file:line and the full statement;
- how big the ambiguity problem was: the share of edges that were ambiguous.

Save the graph as `rh-extraction/usage-graph.json` (or CSV) so Claude can query it.

## Task 2: the Iwasawa "price of divisibility" (guide §6)

Start from:

- `VWinAt` (`Development/AutomorphicArithmetic/CharacterBoxes/ExistsPageN.lean:44`) and `IsChiField` (`:19`);
- `window1` (`Development/AutomorphicArithmetic/AutomorphicVarieties/LayeredIsomorphisms/Window1.lean:6`);
- `every_character_of_literature_of_vWin` (`…/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:810`).

Answer:

- the exact statement of the Ш-length (Tate–Shafarevich) bound and of the window, with quantifiers;
- whether Ferrero–Washington (μ = 0) appears as a proved theorem or as a hypothesis, and where;
- how the bound reaches the loss terms of the main inequality. Candidates: `B0`, `DIVinN`/`etaSum` in `Formalism/SharpRestriction/GlobalTheoremInputs.lean`, and `topDesWin` in `Development/AutomorphicArithmetic/CharacterBoxes/DesWin.lean`.

## Task 3: the archimedean size inputs (guide §4(c))

Find the statements, and where they are used on the headline path, of:

- the **Rallis inner product formula**;
- the **Siegel mass formula** (likely under `Formalism/PeriodIntegrals/UnitaryGroupMassFormula`, 430k lines);
- **Weyl's formula**.

Then show how they reach `good_tower_volume_theorem` (`Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheoremStatement.lean:26`) and the degree bound `LinkDIV_at` (`Formalism/SharpRestriction/GlobalTheoremInputs.lean:77–89`).

## Split of work (avoid overlap)

- **Claude** takes the existence of the auxiliary polynomial: `Formalism/SharpRestriction/GrowthBounds/StandardPolynomials` (`restCols`, `restPre`, `restTCore`, `hhDegs`). Claude also takes how `DivisorProofs` (2.85M lines) connects to the main path.
- **Codex** takes Tasks 1–3 above.

## Conventions

- Tag each claim **READ** (you read the source), **DERIVED** (you reasoned it out) or **COMPILED** (you compiled or ran it).
- Give `file:line` relative to `rh-source/src`.
- Say "not read" when that is the case. Do not present a guess as a fact.
- Put a short plain-language summary at the top of the report, with no jargon: Timmy thinks in pictures.
