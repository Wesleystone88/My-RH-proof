# Task for Codex: cut away the textbook math and measure the new argument

The previous report (`rh-extraction/codex-blackbox-report.md`) was excellent. It showed that following names from `riemannHypothesis` reaches about 10–11 million lines. Most of that is formalized **published** mathematics. We now want only the part of the proof that is new.

## Key fact (Claude, verified at commit e50d098)

`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean` is the authors' own split. It contains **194 theorems named `UpperTheory.LiteratureTheorems.*`** (lines ~219–800). Each has the form `X_of_literature (O) : <Published proposition> := <proof in repo>`. They cover Deligne–Ribet, Siegel–Klingen, Hecke L-functions, local Langlands for GL_n, Jacquet–Shalika, Bernstein–Zelevinsky, Howe duality, Siegel–Weil, Rallis, Kawamata–Viehweg, arithmetic Hilbert–Samuel, Bhatt–Scholze, Fontaine B_cris, Grothendieck–Messing, Linnik, Chebotarev, Poitou–Tate, Greenberg–Wiles, and more. `OpenLiteratureStatements` (line 215) has only three fields: `caraianiLocalGlobalDual`, `localLanglandsExists` and `galoisRepOfPolarizedPairLit`.

The top join (line 810) is:

```
every_character_of_literature_of_vWin (O : OpenLiteratureStatements) (hV : VWin) : EveryCharacter :=
  every_character_of_theta_integrals_local_matching
    (published_results_eigen O) (published_results_first O)
    (theta_integrals_agree_and_local_matching_of_literature O).1 (…).2
    (topCovolSlim2_use_alt_alt <~15 literature results>)
    (local_langlands_gl_recT_exists_of_literature O) hV
```

So the new argument is built from three non-literature pieces:

- **(i)** `UpperTheory.Lit.every_character_of_theta_integrals_local_matching`, the main argument;
- **(ii)** `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt`, the covolume / arithmetic volume bound;
- **(iii)** the window `VWin`, through `UpperTheory.One.vwin_of_row` → … → `UpperTheory.V.HV.Core.of_four_alt` (Ferrero–Washington, plus the counts `CountI`, `CountII`, `CountIII`, `CountV` and `LemmaK`).

## Do this

1. **Build the stop set:**
   - the 194 `UpperTheory.LiteratureTheorems.*` declarations;
   - every proposition they conclude: all `GlobalTheory.Published.*`, plus the other target props listed in that file;
   - the declarations that prove them, i.e. the right-hand sides of those theorems such as `PositivityTheory.PfDR.deligneRibet_holds`;
   - the remaining `*.Published.*` namespaces anywhere in the repo, for example `UpperTheory.V.Published.FerreroWashington` and its proof `UpperTheory.V.FW.ferreroWashington`.

   Record the stop set in `rh-extraction/core-stopset.csv`, one row per declaration: name, file:line, and which rule put it there.
2. **Run a stopped breadth-first search** from `riemannHypothesis` (`Main.lean:4`), reusing your usage-graph data. Do **not** enter stop-set declarations. Run it twice: once on single-target edges only, and once on all candidates. Report reachable declarations, files and lines, and the top 30 directories (depths 3 and 4). **This number is the size of the new argument.**
3. **Repeat step 2 separately** from each of (i), (ii) and (iii). For each, list which stop-set (literature) results it consumes.
4. **Find the hubs.** List the 40 non-literature declarations with the largest stopped reach below them, ordered from the headline down. For each give the fully qualified name, file:line and the full statement (type). This is the outline of the new argument.
5. **Check soundness of the split.**
   - Show where `O : OpenLiteratureStatements` is actually constructed on the headline path (`Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7–11` and `everyCharacter_of_row`), and confirm its three fields are proved and not assumed.
   - Flag any literature proposition that is passed as a hypothesis all the way to `Main` without being proved.
6. **Write the plain-language summary first.** For example: "The new argument is about N lines; it uses these K famous theorems as tools; its three branches are …". Timmy thinks in pictures, so keep the summary free of jargon.

## Output

Write the report to `XPostCode/rh-extraction/codex-core-report.md`, and data files to `rh-extraction/core-*.csv` / `core-*.json`. **Do not edit `RH-proof-handoff.md`.** Claude merges results into it.

## Conventions (as before)

- Tag each claim **READ**, **DERIVED** or **COMPILED**.
- Give `file:line` relative to `rh-source/src`, at commit e50d098.
- Identify every declaration by fully qualified name plus file, because names repeat.
- Say "not established" where it applies.

Claude is meanwhile reading branch (i) at the place where the lattice-degree inequality is actually proved: `wordFacts_of_face` (`Formalism/LocalToGlobal/Divisibility/RecBridge.lean:204`) and `linkDIV_L2R_face` (`Formalism/LocalToGlobal/Divisibility/LinkDIVL2R3Col.lean:19`).
