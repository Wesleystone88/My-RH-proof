# How much remains after stopping at the literature?

**COMPILED** Starting at the final claim and stopping whenever the source points to a marked result leaves **8,672,900 lines**. Following every possible meaning of a repeated name leaves **10,006,103 lines**. The final join names 17 literature entries directly. Opening those bundles reveals all **194** entries in the authors’ list.

**READ / DERIVED** Three pieces work together. One assembles the argument for every character. Another controls how much space a lattice occupies. The third finds a stretch of numbers where arithmetic costs stay small. All three reuse some of the same work. These counts measure the code reached under the requested rule. How many lines contain historically new mathematics is **not established**.

[Stop rules](#1-what-counts-as-literature) · [Headline and branch counts](#2-size-of-the-stopped-graph) · [What the branches use](#3-what-the-three-branches-consume) · [Forty hubs](#4-the-largest-hubs) · [Check of the three inputs](#5-are-the-literature-inputs-supplied) · [Directory tables](#appendix-a-top-directories) · [Full hub statements](#appendix-b-hub-statements)

## 1. What counts as literature

**READ** Revision `e50d09817ad81469f737e8f637561e6ccf86c670`. Lean paths in this report are relative to `rh-source/src/`. The split file is `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean`. It contains one input structure at line 215, **194** theorem declarations starting at lines 219 through 781 (the last body continues through 809), and the **195th theorem**, the application at line 810. Stopping the application would discard the very argument the split asks us to follow. The 194 rule applies to these 194 theorems in this file. The join, the input structure, and same-prefix declarations in other files receive no automatic stop from this rule.

**COMPILED** [The stop set](core-stopset.csv) contains **2,785 distinct declaration IDs**. A row records every applicable rule. Membership counts overlap.

| Stop rule | Members | What was matched |
|---|---|---|
| Literature wrapper | 194 | The explicitly named 194 in the split file. |
| Wrapper result | 193 | The result propositions and proposition records. Both components of the theta-integrals/local-matching conjunction are included. |
| Wrapper proof expression | 372 | Project proof declarations explicitly named on the right of the 194 equations, including subproofs and record-field values. Field labels and local projections are excluded. |
| Published namespace | 1,671 | Every declaration with an exact namespace component named `Published`, including nested namespaces and helper declarations. |
| Proof of a Published result | 1,160 | A written proof or definition whose result head is an identified Published proposition, including results after binders or arrows. The target source must be import-visible. Conditional suppliers are included. |

**READ / COMPILED** For example, `UpperTheory.LiteratureTheorems.deligne_ribet_of_literature` at `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:229` has result `GlobalTheory.Published.DeligneRibet` and right side `PositivityTheory.PfDR.deligneRibet_holds`. The [wrapper ledger](core-wrappers.csv) identifies both by full path and line. The same rules stop `UpperTheory.V.Published.FerreroWashington` at `Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/FerreroWashington.lean:7` and `UpperTheory.V.FW.ferreroWashington` at `Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:104`.

**COMPILED / READ** The supplier check used the result type, rather than the mere presence of a proposition anywhere in a signature. Import visibility ruled out 81 single-target matches. Of 240 ambiguous result heads, 239 had no import-visible Published candidate. The remaining theorem opens `GlobalTheory.Published.GrothendieckMessing` on lines 13–14 and concludes `LiftObj` on line 244, so it is included: `GlobalTheory.NoethLiftObj.liftObj_of_noetherian` at `Development/AbelianVarietyTheory/Proofs/DivisorProofs/GrothendieckMessingLiftOfNoetherianCase.lean:240`. The [ambiguous cases](core-uncertain-providers.csv) and [rule audit](core-rules.json) record the decisions. Imported library operations such as `And.left` are outside the source index. Definitional equality, typeclass synthesis, and arbitrary equivalent reformulations have not been elaborated.

## 2. Size of the stopped graph

**COMPILED** Breadth-first search includes the root, counts each retained declaration once, and counts each file containing one. Lines are the source spans of retained declarations. A marked declaration seen from a retained one is a *boundary hit*: its ID is recorded and its own lines and outgoing edges are excluded. The single-target search discards every multiple-candidate reference. The all-candidates search follows every candidate. No stop is bypassed in either measurement.

| Root | References | Declarations | Files | Source lines | Distinct boundary hits |
|---|---|---|---|---|---|
| Headline | single | 660,273 | 121,229 | 8,672,900 | 800 |
| Headline | all | 785,884 | 138,350 | 10,006,103 | 1,037 |
| Main argument | single | 568,601 | 100,037 | 7,222,849 | 711 |
| Main argument | all | 736,884 | 127,684 | 9,158,550 | 990 |
| Covolume | single | 314,452 | 61,428 | 4,019,276 | 573 |
| Covolume | all | 619,749 | 106,979 | 7,519,769 | 922 |
| Window | single | 255,029 | 48,487 | 3,197,398 | 544 |
| Window | all | 607,931 | 102,787 | 7,345,264 | 920 |

**READ** The four starting points are:

- Headline — `riemannHypothesis` (from `Main.lean:4`).
- Main argument — `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` (from `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69`).
- Covolume — `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` (from `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolSlim2Use.lean:16`).
- Window — `UpperTheory.One.vwin_of_row` (from `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean:4`).

**DERIVED** For the window I used the proof producer `UpperTheory.One.vwin_of_row`. Starting at the proposition `UpperTheory.Top.VWin` would trace the definition of a window and omit the construction. For each branch the search begins inside that branch’s declaration, so values supplied by the enclosing application are shown separately in section 3.

**COMPILED** Against the previous graph on the same pin:

| References | Before stops | After stops | Lines removed | Reduction |
|---|---|---|---|---|
| single | 10,058,743 | 8,672,900 | 1,385,843 | 13.78% |
| all | 11,020,207 | 10,006,103 | 1,014,104 | 9.20% |

**COMPILED** The three branch counts cannot be added. Their shared and distinct coverage is:

| References | Lines shared by all three | Lines in their union | Other lines reached from the headline |
|---|---|---|---|
| single | 2,623,359 | 8,618,539 | 54,361 |
| all | 6,985,099 | 9,985,457 | 20,646 |

**DERIVED / READ** Two effects explain why millions of lines survive. First, an unmarked caller can reach a classical result by a different route. At `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:812` the join explicitly supplies `PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsUse_outright` and `PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright`. Both survive the stated stop rules. Their proof terms are at `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean:9–15`. Second, the reused graph can confuse a bound variable with a declaration even in single-target mode. In `Development/AbelianVarietyTheory/Definitions/Foundations/MemPuncturedRingIffPowerSeriesPart.lean:101`, `GlobalTheory.Conv.X_mem_discSeries` uses `fun u _ => (hasSum_X u).summable`. The graph points from that local `u` to `GlobalTheory.Conv.u` at line 262, whose definition really does use `X_mem_discSeries`. That creates a spurious cycle. The counts are exact for the saved lexical graph. A kernel dependency count and a historical novelty count are both **not established**.

## 3. What the three branches consume

**COMPILED** [All distinct boundary results by branch](core-literature-frontiers.csv) are listed for both modes, with declaration ID, qualified name, file and line, minimum depth, a witnessing source, matched token and source line, and whether the token appears in the witness’s type, body, or both. A shortest textual witness that occurs in a type can describe an input without applying its proof. The [caller-side inventory](core-supplied-wrappers.json) separately follows explicit references between the 194 wrapper bodies from the arguments on lines 811–813.

**READ / COMPILED** The main argument receives four named literature wrappers from the join: the eigen and first published-result records, both projections of one theta-integrals/local-matching result, and local Langlands. Those four lead to **154** wrappers when their bundles are opened. The covolume argument receives thirteen named wrappers and the two outright results identified above. Its thirteen wrappers lead to **43**. Three wrapper declarations occur in both expanded lists, giving 194 in their union. Window construction takes place at the caller of the join. These are source references in constructed records; the count of fields indispensable after projection is **not established**.

**READ** Main argument — wrappers supplied by the enclosing application:

- `UpperTheory.LiteratureTheorems.published_results_eigen` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:666`.
- `UpperTheory.LiteratureTheorems.published_results_first` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:727`.
- `UpperTheory.LiteratureTheorems.theta_integrals_agree_and_local_matching_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:565`.
- `UpperTheory.LiteratureTheorems.local_langlands_gl_recT_exists_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:313`.

**READ** Covolume — wrappers supplied by the enclosing application:

- `UpperTheory.LiteratureTheorems.resolution_char_zero_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:557`.
- `UpperTheory.LiteratureTheorems.principalisation_char_zero_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:555`.
- `UpperTheory.LiteratureTheorems.poincare_lelong_inv_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:553`.
- `UpperTheory.LiteratureTheorems.fargues_exact_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:549`.
- `UpperTheory.LiteratureTheorems.zarhin_statement` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:547`.
- `UpperTheory.LiteratureTheorems.nef_rr_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:551`.
- `UpperTheory.LiteratureTheorems.siegel_toroidal_integral_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:509`.
- `UpperTheory.LiteratureTheorems.toroidal_for_fan_ks_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:523`.
- `UpperTheory.LiteratureTheorems.semi_abelian_lie_seminegative_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:499`.
- `UpperTheory.LiteratureTheorems.point_separation_pair_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:471`.
- `UpperTheory.LiteratureTheorems.ar_degree_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:251`.
- `UpperTheory.LiteratureTheorems.published_results_arithmetic` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:781`.
- `UpperTheory.LiteratureTheorems.grothendieck_deformation_of_literature` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:405`.

**READ** The window’s first single-target boundary result is the base-change proof supplied at `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean:5`. Deeper in this branch `UpperTheory.V.HV.Core.of_four_alt` takes the rank hypothesis, LemmaK and Counts I, II, III and V. Its body passes the proved Ferrero–Washington result to `Win.thmBab_of_lemmaK` and uses the resulting bound at 401. In the single-target graph the proof and proposition first occur at depths seven and eight. This is a concrete use of the theorem inside the branch.

**READ** `UpperTheory.V.HV.Core.of_four_alt` · `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/HVCore.lean:18`

```lean
theorem of_four_alt (hN : _root_.GlobalTheory.Mem.LiteralAutomorphy.LiteratureRankNHypothesis) (hK : ∃ CK : ℝ, LemmaK CK) (h1 : CountI) (h2 : CountII) (h3 : CountIII) (h5 : CountV) : VWin := by
  obtain ⟨B, hB⟩ := Win.thmBab_of_lemmaK (_root_.UpperTheory.V.HV.U.pt_s hN) hN.coh.lfK hN.coh.ltK FW.ferreroWashington hK
  obtain ⟨CK, hL⟩ := hK
  exact vwin_of_counts (_root_.UpperTheory.V.HV.U.pt_s hN) hN.coh.lfK hN.coh.ltK hL (hB 401 (by norm_num))
    (Odd.thmBcFree_of (ML.iv (_root_.UpperTheory.V.HV.U.pt_s hN) hN.coh.uo)) h1 h2 h3 h5 (countZ X.propZ)
```

**COMPILED** Main argument — immediate boundary inside the declaration (5).

| Marked declaration | Definition site | Witness occurrence |
|---|---|---|
| `GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses` | `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:22` | type |
| `GlobalTheory.FunPr.ThetaLocalInputs` | `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:6` | type |
| `GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching` | `Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilTensorModels.lean:581` | type |
| `GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree` | `Development/AbelianVarietyTheory/BlockTheory/DivisorBase/WeilTensorModels.lean:585` | type |
| `UpperTheory.Zero.LLC.RecTExists` | `Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean:78` | type |

**COMPILED** Covolume — immediate boundary inside the declaration (19).

| Marked declaration | Definition site | Witness occurrence |
|---|---|---|
| `ChowFormCompatibility.chow_form_hyperplane_section` | `Development/WeilBound/CoreStatements/NefModelVolumes/ChowFormHyperplaneSection.lean:12` | body |
| `FubiniStudyChowHeightFormula₂.fubiniStudy_chowHeight_formula` | `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/FubiniStudyChowHeightFormula.lean:17` | body |
| `GlobalTheory.CompanionTheory.Ar.GR.ZarhinStatement` | `Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/ZarhinStatement.lean:21` | type |
| `GlobalTheory.CompanionTheory.Ar.HT.FarguesExact` | `Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/FarguesExact.lean:10` | type |
| `GlobalTheory.CompanionTheory.Ar.Pub.NefRR` | `Development/AutomorphicSpectrum/PublishedTheorems/Geometry₂/NefRR.lean:8` | type |
| `GlobalTheory.CompanionTheory.Hypotheses₂.PoincareLelongInv` | `Development/AutomorphicSpectrum/PublishedTheorems/Metrics₂/PoincareLelongInv.lean:9` | type |
| `GlobalTheory.CompanionTheory.Hypotheses₂.PrincipalisationCharZero` | `Development/AutomorphicSpectrum/PublishedTheorems/Geometry₂/NotSubsetOfDenseCompl.lean:57` | type |
| `GlobalTheory.CompanionTheory.Hypotheses₂.ResolutionCharZero` | `Development/AutomorphicSpectrum/PublishedTheorems/Geometry₂/ConclusionOfSmooth.lean:53` | type |
| `GlobalTheory.CovTop.PublishedHodgeBundleTheorems` | `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean:7` | type |
| `GlobalTheory.Published.ArDegree` | `Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ArBirational.lean:25` | type |
| `GlobalTheory.Published.GrothendieckDeformation` | `Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/GrothendieckDeformation.lean:12` | type |
| `GlobalTheory.Published.PointSeparationPair` | `Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/PointSeparationPair.lean:15` | type |
| `GlobalTheory.Published.SemiAbelianLieSeminegative` | `Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/InterNumDetNonposSplitTorus.lean:23` | type |
| `GlobalTheory.Published.SiegelToroidalIntegral` | `Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/SiegelToroidalIntegral.lean:145` | type |
| `GlobalTheory.Published.ToroidalForFanKS` | `Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/ToroidalCompactificationBis.lean:45` | type |
| `GlobalTheory.Published.chowFormIntExists_holds` | `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ChowFormIntExistsAndChowFormExists.lean:246` | body |
| `GlobalTheory.Published.toroidalCharts_of_siegel_of_forFan` | `Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToroidalChartsOfSiegelOfForFan.lean:8` | body |
| `GlobalTheory.greenRegularCharacters_holds` | `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/GreenCuspidalCharsByRegularCharsProof.lean:137` | body |
| `PositivityTheory.Prw.toroidalChartsForFan_of` | `Development/WeilBound/CoreStatements/AbelianHeightsDuality/PublishedTheoremStatements/BridgesMore.lean:54` | body |

**COMPILED** Window — immediate boundary inside the declaration (1).

| Marked declaration | Definition site | Witness occurrence |
|---|---|---|
| `UpperTheory.BaseChangeIdentities.baseChangeN` | `Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/DefiniteNHolds.lean:5` | body |

## 4. The largest hubs

**COMPILED** The main ranking selects the 40 declarations with the most **distinct retained lines strictly below them** in the headline single-target graph. The outline is displayed from the headline down by minimum reference depth, with size rank alongside. Within a score tie, nearer declarations come first, followed by stable ID. [All hub rankings and full types](core-hubs.csv) include both reference modes and both ranking measures (descendant lines or descendant declarations). The expanded-mode line leaders also have their full statements in Appendix B.

**DERIVED** The score is transitive coverage. A forwarder a line long can inherit nearly all the reach of what it calls. In single-target mode the largest mutually reachable group contains 152,457 declarations; in all-candidates mode it contains 580,158. For exact ranking the calculation condensed such groups, counted each reachable declaration once, and excluded the scored declaration’s own span. A group with 40 real declarations strictly upstream on a single path cannot contain a top-40 entry: each of those 40 scores strictly higher. This pruning argument applies to both metrics. Ambiguity-group vertices carry zero declarations and zero lines. The [ranking diagnostics](core-hub-method.json) include cutoff ties.

| Depth | Size rank | Declaration and source line | Descendant lines |
|---|---|---|---|
| 0 | 1 | `riemannHypothesis` · `Main.lean:4` | 8,672,899 |
| 1 | 2 | `rhOfAll` · `Supplements/Kernels/MainTheorems.lean:9` | 8,672,898 |
| 2 | 3 | `allChi` · `Supplements/Kernels/MainTheorems.lean:7` | 8,672,835 |
| 3 | 4 | `UpperTheory.FinalTheorems.everyCharacter` · `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:10` | 8,672,833 |
| 4 | 5 | `UpperTheory.FinalTheorems.everyCharacter_of_row` · `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7` | 8,672,831 |
| 5 | 6 | `UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:810` | 8,169,367 |
| 6 | 7 | `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69` | 7,222,844 |
| 6 | 15 | `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolSlim2Use.lean:16` | 4,019,269 |
| 7 | 8 | `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:44` | 7,057,327 |
| 7 | 28 | `PositivityTheory.HtPt.Ah.deep_slim_use` · `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/AhSlimU.lean:9` | 3,509,957 |
| 7 | 32 | `SelfIntersectionVolumeEstimates.topCovolG_alt_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolG.lean:39` | 3,380,775 |
| 8 | 9 | `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean:41` | 6,681,312 |
| 8 | 13 | `GlobalTheory.T.open0_of_unitary_group_hypotheses` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:75` | 4,178,221 |
| 8 | 24 | `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SurjectiveAndLowWeightOfUnramifiedExponents.lean:16` | 3,578,398 |
| 8 | 29 | `GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` · `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/DeepStROfUse.lean:12` | 3,475,771 |
| 9 | 10 | `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean:50` | 4,466,281 |
| 9 | 11 | `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean:69` | 4,216,001 |
| 9 | 14 | `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:39` | 4,178,190 |
| 9 | 27 | `GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean:28` | 3,515,416 |
| 9 | 30 | `UpperTheory.GalC.final_alt_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean:19` | 3,449,212 |
| 9 | 31 | `GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis` · `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/GoodTowerVolumeTheoremBis.lean:9` | 3,419,886 |
| 9 | 36 | `GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean:51` | 3,320,162 |
| 10 | 12 | `GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean:34` | 4,215,971 |
| 10 | 18 | `GlobalTheory.T.main_theorem_published_inputs_third_alt_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean:34` | 3,942,665 |
| 10 | 20 | `GlobalTheory.LocalRows.lg1_sLp_sO_hTF` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean:27` | 3,710,107 |
| 10 | 34 | `GlobalTheory.T.final_theorem_of_inputs_right` · `Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRightStatement.lean:19` | 3,345,501 |
| 10 | 37 | `GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean:24` | 3,320,139 |
| 10 | 38 | `GlobalTheory.BigOn.ontoX_of_twist_shares_exp_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfTwistSharesExp.lean:21` | 3,309,554 |
| 11 | 16 | `GlobalTheory.T.member_exists_baseLattice_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean:80` | 4,011,029 |
| 11 | 19 | `GlobalTheory.miStarRow_alt_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean:22` | 3,942,658 |
| 11 | 21 | `GlobalTheory.LocalRows.sLp_sO_hTF_of_siegelWeil` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean:24` | 3,710,079 |
| 11 | 35 | `GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced` · `Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRight.lean:28` | 3,345,489 |
| 12 | 17 | `GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean:57` | 4,011,013 |
| 12 | 22 | `GlobalTheory.LocalRows.at_choice_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean:16` | 3,708,549 |
| 12 | 25 | `GlobalTheory.T.diagonalRow_of_siegelWeil_unitary` · `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DiagonalRowOfSiegelWeilUnitaryStatement.lean:45` | 3,532,891 |
| 13 | 23 | `GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean:36` | 3,588,605 |
| 13 | 26 | `GlobalTheory.Core.Rk.rowDiag_of_siegelWeilUnitary` · `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DiagonalRowOfSiegelWeilUnitary.lean:50` | 3,532,885 |
| 13 | 33 | `GlobalTheory.CarrierGap.offDiag` · `Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean:673` | 3,347,368 |
| 14 | 39 | `GlobalTheory.T.corankOnePairsFamilyBounds_of_siegelWeil` · `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/CorankOnePairsFamilyBoundsOfSiegelWeilStatement.lean:45` | 3,304,528 |
| 15 | 40 | `GlobalTheory.Core.Diag.oneOn_singleton_of_siegelWeil` · `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/CorankOnePairsFamilyBoundsOfSiegelWeil.lean:10` | 3,304,520 |

## 5. Are the literature inputs supplied?

**READ** The input record really has three fields. The first and third have the **same Lean type**. `UpperTheory.One.M.Row` unfolds to the exact row predicate used in `everyCharacter_of_row`, so one witnessed row fills both positions. The middle field has its own witness.

**READ** `UpperTheory.LiteratureTheorems.OpenLiteratureStatements` · `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:215`

```lean
structure UpperTheory.LiteratureTheorems.OpenLiteratureStatements : Prop where
  caraianiLocalGlobalDual : _root_.UpperTheory.One.M.Row
  localLanglandsExists : _root_.UpperTheory.Zero.LLC.RecTExists
  galoisRepOfPolarizedPairLit : _root_.UpperTheory.One.M.Row
```

**READ** `UpperTheory.One.M.recT` and `UpperTheory.One.M.Row` · `Development/AutomorphicArithmetic/Foundations/UnitarySphericalFixing/SatakeParameters/RecT.lean:4`

```lean
def UpperTheory.One.M.recT : UpperTheory.GalStar.RecNotion := fun h rc => UpperTheory.Zero.LLC.IsRecT h rc

def UpperTheory.One.M.Row : Prop := UpperTheory.GalStar.Row0b fun h rc => UpperTheory.Zero.LLC.IsRecT h rc
```

**READ** `UpperTheory.FinalTheorems.everyCharacter_of_row` constructs the record; `UpperTheory.FinalTheorems.everyCharacter` supplies the row · `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7`

```lean
theorem UpperTheory.FinalTheorems.everyCharacter_of_row (h : UpperTheory.GalStar.Row0b fun h rc => UpperTheory.Zero.LLC.IsRecT h rc) : UpperTheory.EveryCharacter :=
  UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin ⟨h, UpperTheory.Zero.LLC.recTExists, h⟩ (UpperTheory.One.vwin_of_row h)

theorem UpperTheory.FinalTheorems.everyCharacter : UpperTheory.EveryCharacter :=
  UpperTheory.FinalTheorems.everyCharacter_of_row UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter
```

**READ** `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter` · `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean:4`

```lean
namespace UpperTheory.Gal.Int

theorem galoisLocalGlobalStrong_recParameter : UpperTheory.GalStar.Row0b recT := galoisRepresentations_of_thetaLift UpperTheory.TP.K.tLiftK
```

**READ** `UpperTheory.Gal.Int.recT` unfolds to the same predicate · `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean:18`

```lean
def recT : UpperTheory.GalStar.RecNotion := fun h rc => UpperTheory.Zero.LLC.IsRecT h rc
```

**READ** `UpperTheory.Gal.Int.galoisRepresentations_of_thetaLift` · `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GaloisRepresentationsOfThetaLift.lean:6`

```lean
theorem galoisRepresentations_of_thetaLift (up : UpperTheory.TP.TLiftK) : UpperTheory.GalStar.Row0b recT := galoisLocalGlobalStrong_of_geometry_lift UpperTheory.Gal.Int.Geo.geoOne_holds up
```

**READ** `UpperTheory.Zero.LLC.recTExists`, statement and opening proof steps · `Development/AutomorphicArithmetic/Foundations/LocalLanglands/LocalCentralUnits/RecTExists.lean:20`

```lean
theorem UpperTheory.Zero.LLC.recTExists :
    UpperTheory.Zero.LLC.RecTExists := by
  intro E Ω _ _ _ _ _ A w h
  obtain ⟨a, ha, -⟩ := UpperTheory.Zero.LLC.artEx E Ω A w h
  obtain ⟨r, hr⟩ := UpperTheory.Zero.LLC.cuspEx E Ω A w h a ha
  obtain ⟨⟨rc, hrc⟩, hcu⟩ :=
    GlobalTheory.LocLanglands.exists_isLExt UpperTheory.Zero.LLC.Pr.exh UpperTheory.Zero.LLC.Pr.multi E Ω A w h r
  have hcusp : ∀ x : IrrGL (HeightOneSpectrum.adicCompletion E w), x.IsCusp → rc x = r x :=
    hcu rc hrc
```

**READ** Field 1 (`caraianiLocalGlobalDual`) and field 3 (`galoisRepOfPolarizedPairLit`) both receive `h` at line 8. At line 11 `h` is supplied by `UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter`, whose body applies the theta-lift result. Field 2 (`localLanglandsExists`) receives `UpperTheory.Zero.LLC.recTExists` directly. Its proof constructs local data using `artEx`, `cuspEx` and `exists_isLExt`. Within the literature wrappers, the middle input is explicitly projected at line 284. A field projected from the record is supplied at this call site even when the wrapper treats it as an assumption.

**READ** Root declarations `allChi` and `rhOfAll` · `Supplements/Kernels/MainTheorems.lean:7`

```lean
theorem allChi : UpperTheory.EveryCharacter := UpperTheory.FinalTheorems.everyCharacter

theorem rhOfAll : RiemannHypothesis := Formalism.VW.rh_of_every allChi
```

**READ** `riemannHypothesis` · `Main.lean:4`

```lean
theorem riemannHypothesis : RiemannHypothesis := rhOfAll
```

**READ / DERIVED** Unproved literature premise passed all the way to this `Main` declaration: **none identified**. The visible headline has no argument for a row, a literature record, a window, or any other literature proposition. The supplied terms above close the three-field question at source level. The pinned upstream `verification/static-scan.txt:1–9` reports zero `axiom` declarations, `sorry`, and `admit` in the submitted sources. Its `verification/NOTES.md` distinguishes that scan from kernel replay. No kernel replay or transitive `#print axioms` was performed for this report, so an independent kernel-level axiom audit is **not established**.

**READ** One illustration of why names cannot count famous theorems: `UpperTheory.LiteratureTheorems.siegel_eisenstein_simple_pole` at `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:505–506` concludes `GlobalTheory.Published.UnusedSlot72`, with proof `trivial`. That abbreviation is exactly `True` at `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/DiscreteSpectrumResidualClassification.lean:7`. This field is supplied. Its written type provides no simple-pole statement. The 194 figure counts source declarations.

## Appendix A. Top directories

**COMPILED** Each pair of columns is independently ranked by retained lines. Depth means the number of directory components below `src/`. [Directory data](core-directories.csv) also gives declaration and file counts for each row. [Counts and overlap](core-counts.json) and [declaration membership with distances](core-reach.csv) support further queries. All declaration IDs join to the previous `usage-nodes.csv`.

### Headline — depth 3

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs | 3,767,971 | Development/AbelianVarietyTheory/Proofs | 4,199,417 |
| 2 | Development/AutomorphicSpectrum/Proofs | 594,816 | Development/AutomorphicSpectrum/Proofs | 667,177 |
| 3 | Development/AutomorphicArithmetic/AutomorphicVarieties | 412,132 | Development/AutomorphicArithmetic/AutomorphicVarieties | 614,407 |
| 4 | Formalism/HermitianCurvature/HermitianCurvatureProofs | 291,057 | GroundTheory/HeightsAndTheta/Heights | 349,209 |
| 5 | GroundTheory/HeightsAndTheta/Heights | 278,524 | Development/AutomorphicArithmetic/Foundations | 301,791 |
| 6 | Development/AutomorphicArithmetic/Foundations | 271,474 | Formalism/HermitianCurvature/HermitianCurvatureProofs | 298,155 |
| 7 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 251,614 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 267,108 |
| 8 | Development/WeilBound/CoreStatements | 235,429 | Development/WeilBound/CoreStatements | 261,620 |
| 9 | Formalism/LocalToGlobal/SiegelLatticeTheory | 233,054 | Formalism/LocalToGlobal/SiegelLatticeTheory | 236,029 |
| 10 | Formalism/SharpRestriction/GrowthBounds | 174,544 | Development/AbelianVarietyTheory/Definitions | 198,837 |
| 11 | Development/WeilBound/RepresentationTheoryGL | 158,122 | Formalism/SharpRestriction/GrowthBounds | 178,596 |
| 12 | Development/AbelianVarietyTheory/Definitions | 143,870 | Development/WeilBound/RepresentationTheoryGL | 177,116 |
| 13 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 141,918 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 149,424 |
| 14 | Formalism/SharpRestriction/LevelLetterCocycles | 118,028 | Formalism/SharpRestriction/LevelLetterCocycles | 121,989 |
| 15 | ReciprocityTheory/ReductiveGroups/DiscreteSeries | 91,591 | Development/ResolutionOfSingularities/EmbeddedResolution | 104,021 |
| 16 | Development/AutomorphicArithmetic/ThetaCorrespondence | 89,992 | Development/AutomorphicArithmetic/IntegralCasts | 97,762 |
| 17 | Development/AutomorphicArithmetic/IntegralCasts | 72,898 | ReciprocityTheory/ReductiveGroups/DiscreteSeries | 95,731 |
| 18 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 48,261 | Development/AutomorphicArithmetic/ThetaCorrespondence | 94,285 |
| 19 | Formalism/SharpRestriction/CuspSpanNormBounds | 47,895 | Formalism/SharpRestriction/CuspSpanNormBounds | 54,646 |
| 20 | Formalism/LocalToGlobal/TorsionIntegrality | 42,867 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 53,991 |
| 21 | Formalism/GL3MeanSquares/GenusMeanAsymptotics | 39,301 | Formalism/LocalToGlobal/Columns | 46,041 |
| 22 | Formalism/LocalToGlobal/Columns | 39,246 | Development/WeilBound/ThetaLifts | 44,388 |
| 23 | Development/EtaleCohomology/EtaleSheaves | 34,651 | Formalism/LocalToGlobal/TorsionIntegrality | 43,927 |
| 24 | Formalism/LocalToGlobal/GlobalTheory | 31,284 | Formalism/GL3MeanSquares/GenusMeanAsymptotics | 39,612 |
| 25 | Development/AutomorphicArithmetic/CommutativeAlgebra | 30,448 | Development/EtaleCohomology/EtaleSheaves | 37,447 |
| 26 | Formalism/SharpRestriction/Divisibility | 27,792 | Development/AutomorphicArithmetic/CommutativeAlgebra | 36,410 |
| 27 | Formalism/LocalToGlobal/IndefiniteReal | 27,017 | Formalism/SharpRestriction/Divisibility | 33,352 |
| 28 | Formalism/LocalToGlobal/ProjectiveLattices | 23,690 | Formalism/LocalToGlobal/IndefiniteReal | 32,992 |
| 29 | Formalism/LocalToGlobal/KernelLattices | 22,351 | Formalism/LocalToGlobal/GlobalTheory | 32,799 |
| 30 | PositivityTheory/AutomorphicForms/PublishedInputs | 22,201 | Development/AbelianVarietyTheory/BlockTheory | 31,910 |

### Headline — depth 4

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 870,192 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 1,160,403 |
| 2 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 406,826 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 440,273 |
| 3 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 337,973 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 359,926 |
| 4 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 314,509 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 357,820 |
| 5 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 298,036 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 347,786 |
| 6 | Development/AbelianVarietyTheory/Proofs/FlagMeasures | 297,076 | Development/AbelianVarietyTheory/Proofs/FlagMeasures | 299,834 |
| 7 | Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs | 215,626 | Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs | 221,587 |
| 8 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 203,718 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 214,460 |
| 9 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 166,328 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 210,125 |
| 10 | Development/AutomorphicSpectrum/Proofs/GeometryProofs | 152,914 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 182,139 |
| 11 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 148,353 | Development/AutomorphicSpectrum/Proofs/GeometryProofs | 154,828 |
| 12 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 140,665 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 153,441 |
| 13 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 111,834 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 115,169 |
| 14 | Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts | 105,000 | Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts | 105,764 |
| 15 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 91,041 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 95,451 |
| 16 | Development/AbelianVarietyTheory/Proofs/GlobalInterpolation | 85,078 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 93,470 |
| 17 | Development/AbelianVarietyTheory/Proofs/JetHarmonics | 84,297 | Development/AbelianVarietyTheory/Proofs/GlobalInterpolation | 87,777 |
| 18 | Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts | 82,632 | Development/AbelianVarietyTheory/Proofs/JetHarmonics | 86,217 |
| 19 | Development/AutomorphicSpectrum/Proofs/MetricProofs | 81,945 | Development/AutomorphicArithmetic/Foundations/Convolution | 84,499 |
| 20 | Development/AutomorphicArithmetic/Foundations/Convolution | 72,258 | Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts | 83,369 |
| 21 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 71,215 | Development/AutomorphicSpectrum/Proofs/MetricProofs | 82,607 |
| 22 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 65,428 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 67,540 |
| 23 | GroundTheory/HeightsAndTheta/Heights/HilbertSamuel | 54,593 | GroundTheory/HeightsAndTheta/Heights/HilbertSamuel | 60,049 |
| 24 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 54,266 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 56,405 |
| 25 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 52,849 | Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization | 54,013 |
| 26 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 50,739 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 53,091 |
| 27 | Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations | 48,662 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 52,234 |
| 28 | Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors | 46,964 | Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations | 49,443 |
| 29 | Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits | 44,543 | Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors | 48,013 |
| 30 | Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs | 44,349 | Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs | 45,834 |

### Main argument — depth 3

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs | 3,498,307 | Development/AbelianVarietyTheory/Proofs | 4,093,074 |
| 2 | Development/AutomorphicSpectrum/Proofs | 316,894 | Development/AutomorphicSpectrum/Proofs | 455,724 |
| 3 | Formalism/HermitianCurvature/HermitianCurvatureProofs | 291,055 | Development/AutomorphicArithmetic/AutomorphicVarieties | 392,740 |
| 4 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 250,993 | Formalism/HermitianCurvature/HermitianCurvatureProofs | 298,120 |
| 5 | Development/AutomorphicArithmetic/Foundations | 238,117 | Development/AutomorphicArithmetic/Foundations | 282,637 |
| 6 | Formalism/LocalToGlobal/SiegelLatticeTheory | 233,054 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 267,074 |
| 7 | Formalism/SharpRestriction/GrowthBounds | 174,544 | GroundTheory/HeightsAndTheta/Heights | 261,461 |
| 8 | Development/WeilBound/RepresentationTheoryGL | 156,702 | Formalism/LocalToGlobal/SiegelLatticeTheory | 236,027 |
| 9 | Development/AbelianVarietyTheory/Definitions | 130,573 | Development/AbelianVarietyTheory/Definitions | 195,330 |
| 10 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 122,039 | Formalism/SharpRestriction/GrowthBounds | 178,553 |
| 11 | Formalism/SharpRestriction/LevelLetterCocycles | 117,694 | Development/WeilBound/RepresentationTheoryGL | 176,820 |
| 12 | Development/AutomorphicArithmetic/AutomorphicVarieties | 96,126 | Development/WeilBound/CoreStatements | 152,734 |
| 13 | ReciprocityTheory/ReductiveGroups/DiscreteSeries | 91,591 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 142,935 |
| 14 | Development/WeilBound/CoreStatements | 90,519 | Formalism/SharpRestriction/LevelLetterCocycles | 121,942 |
| 15 | Development/AutomorphicArithmetic/ThetaCorrespondence | 80,957 | Development/ResolutionOfSingularities/EmbeddedResolution | 104,019 |
| 16 | Development/AutomorphicArithmetic/IntegralCasts | 48,351 | ReciprocityTheory/ReductiveGroups/DiscreteSeries | 95,731 |
| 17 | Formalism/SharpRestriction/CuspSpanNormBounds | 47,895 | Development/AutomorphicArithmetic/ThetaCorrespondence | 85,257 |
| 18 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 47,709 | Development/AutomorphicArithmetic/IntegralCasts | 83,300 |
| 19 | Formalism/LocalToGlobal/TorsionIntegrality | 42,865 | Formalism/SharpRestriction/CuspSpanNormBounds | 54,627 |
| 20 | Formalism/GL3MeanSquares/GenusMeanAsymptotics | 39,300 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 53,984 |
| 21 | Formalism/LocalToGlobal/Columns | 39,230 | Formalism/LocalToGlobal/Columns | 46,041 |
| 22 | GroundTheory/HeightsAndTheta/Heights | 39,064 | Development/WeilBound/ThetaLifts | 44,237 |
| 23 | Development/EtaleCohomology/EtaleSheaves | 34,651 | Formalism/LocalToGlobal/TorsionIntegrality | 43,927 |
| 24 | Formalism/LocalToGlobal/GlobalTheory | 31,284 | Formalism/GL3MeanSquares/GenusMeanAsymptotics | 39,611 |
| 25 | Development/AutomorphicArithmetic/CommutativeAlgebra | 30,440 | Development/EtaleCohomology/EtaleSheaves | 37,445 |
| 26 | Formalism/LocalToGlobal/IndefiniteReal | 26,992 | Development/AutomorphicArithmetic/CommutativeAlgebra | 36,409 |
| 27 | Formalism/SharpRestriction/Divisibility | 26,264 | Formalism/LocalToGlobal/IndefiniteReal | 32,973 |
| 28 | Formalism/LocalToGlobal/ProjectiveLattices | 22,660 | Formalism/LocalToGlobal/GlobalTheory | 32,799 |
| 29 | Formalism/LocalToGlobal/KernelLattices | 22,351 | Formalism/SharpRestriction/Divisibility | 32,471 |
| 30 | Formalism/LocalToGlobal/CharacterGerms | 21,450 | Development/AbelianVarietyTheory/BlockTheory | 31,497 |

### Main argument — depth 4

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 718,355 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 1,105,307 |
| 2 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 405,479 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 439,763 |
| 3 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 337,742 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 359,790 |
| 4 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 297,374 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 356,786 |
| 5 | Development/AbelianVarietyTheory/Proofs/FlagMeasures | 297,076 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 347,004 |
| 6 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 281,517 | Development/AbelianVarietyTheory/Proofs/FlagMeasures | 299,834 |
| 7 | Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs | 215,559 | Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs | 221,562 |
| 8 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 159,486 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 177,281 |
| 9 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 148,043 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 164,553 |
| 10 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 133,334 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 153,233 |
| 11 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 111,397 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 129,597 |
| 12 | Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts | 105,000 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 115,052 |
| 13 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 90,894 | Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts | 105,764 |
| 14 | Development/AbelianVarietyTheory/Proofs/GlobalInterpolation | 84,998 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 93,460 |
| 15 | Development/AbelianVarietyTheory/Proofs/JetHarmonics | 83,045 | Development/AbelianVarietyTheory/Proofs/GlobalInterpolation | 87,684 |
| 16 | Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts | 74,063 | Development/AbelianVarietyTheory/Proofs/JetHarmonics | 85,996 |
| 17 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 65,218 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 80,989 |
| 18 | Development/AutomorphicArithmetic/Foundations/Convolution | 54,542 | Development/AutomorphicArithmetic/Foundations/Convolution | 75,601 |
| 19 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 54,266 | Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts | 74,817 |
| 20 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 52,515 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 67,535 |
| 21 | Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations | 48,612 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 56,403 |
| 22 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 48,225 | Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization | 54,011 |
| 23 | Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors | 46,964 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 53,091 |
| 24 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 46,668 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 52,143 |
| 25 | Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits | 44,543 | Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations | 49,420 |
| 26 | Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs | 44,011 | Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors | 48,013 |
| 27 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 41,449 | Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs | 45,823 |
| 28 | Development/AbelianVarietyTheory/Proofs/UnramifiedDepth | 38,537 | Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits | 45,169 |
| 29 | CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis | 37,046 | Development/WeilBound/CoreStatements/AutomorphicKernels | 44,131 |
| 30 | Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof | 35,549 | Development/AbelianVarietyTheory/Definitions/Divisors | 43,374 |

### Covolume — depth 3

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs | 1,679,342 | Development/AbelianVarietyTheory/Proofs | 2,895,457 |
| 2 | Development/AutomorphicSpectrum/Proofs | 525,682 | Development/AutomorphicSpectrum/Proofs | 628,176 |
| 3 | Development/AutomorphicArithmetic/Foundations | 232,074 | Development/AutomorphicArithmetic/AutomorphicVarieties | 385,215 |
| 4 | GroundTheory/HeightsAndTheta/Heights | 231,754 | GroundTheory/HeightsAndTheta/Heights | 330,985 |
| 5 | Development/WeilBound/CoreStatements | 226,717 | Formalism/HermitianCurvature/HermitianCurvatureProofs | 297,948 |
| 6 | Development/WeilBound/RepresentationTheoryGL | 122,306 | Development/AutomorphicArithmetic/Foundations | 274,935 |
| 7 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 108,990 | Development/WeilBound/CoreStatements | 258,772 |
| 8 | Development/AutomorphicArithmetic/AutomorphicVarieties | 80,069 | Formalism/LocalToGlobal/SiegelLatticeTheory | 222,989 |
| 9 | Development/AbelianVarietyTheory/Definitions | 80,038 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 210,971 |
| 10 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 40,213 | Development/AbelianVarietyTheory/Definitions | 167,111 |
| 11 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 34,825 | Development/WeilBound/RepresentationTheoryGL | 167,036 |
| 12 | Development/EtaleCohomology/EtaleSheaves | 34,651 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 126,353 |
| 13 | Formalism/LocalToGlobal/SiegelLatticeTheory | 32,710 | Development/ResolutionOfSingularities/EmbeddedResolution | 104,021 |
| 14 | Development/AutomorphicArithmetic/CommutativeAlgebra | 30,386 | ReciprocityTheory/ReductiveGroups/DiscreteSeries | 88,461 |
| 15 | Development/AutomorphicArithmetic/IntegralCasts | 29,493 | Development/AutomorphicArithmetic/IntegralCasts | 82,002 |
| 16 | Formalism/SharpRestriction/Divisibility | 19,812 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 53,751 |
| 17 | Development/WeilBound/ThetaLifts | 18,490 | Formalism/SharpRestriction/CuspSpanNormBounds | 51,803 |
| 18 | Formalism/LocalToGlobal/Columns | 13,407 | Development/WeilBound/ThetaLifts | 43,589 |
| 19 | GroundTheory/ArithmeticGeometry/SchemeCohomology | 12,435 | Formalism/GL3MeanSquares/GenusMeanAsymptotics | 39,610 |
| 20 | Formalism/LocalToGlobal/ProjectiveLattices | 12,144 | Formalism/SharpRestriction/GrowthBounds | 38,880 |
| 21 | Development/AutomorphicArithmetic/ThetaCorrespondence | 9,961 | Development/EtaleCohomology/EtaleSheaves | 37,447 |
| 22 | Formalism/SharpRestriction/GrowthBounds | 9,452 | Development/AutomorphicArithmetic/CommutativeAlgebra | 36,409 |
| 23 | Formalism/LocalToGlobal/IndefiniteReal | 9,165 | Formalism/LocalToGlobal/TorsionIntegrality | 36,244 |
| 24 | Formalism/SatakeDualWeyl/AdelicIwasawaHecke | 8,538 | Formalism/LocalToGlobal/Columns | 30,602 |
| 25 | Development/EtaleCohomology/TateTwists | 8,211 | Formalism/SharpRestriction/Divisibility | 27,011 |
| 26 | GroundTheory/GlobalFields/TateThesis | 7,663 | Development/AbelianVarietyTheory/BlockTheory | 26,257 |
| 27 | Formalism/PieriBlockIdeals/PieriColumnMinors | 7,329 | Formalism/LocalToGlobal/IndefiniteReal | 22,308 |
| 28 | ReciprocityTheory/AnalyticForms/PlurisubharmonicFunctions | 7,046 | Formalism/SharpRestriction/LevelLetterCocycles | 21,436 |
| 29 | ReciprocityTheory/ClassFieldTheory/LocalClassField | 6,586 | Formalism/LocalToGlobal/ProjectiveLattices | 16,923 |
| 30 | Development/AbelianVarietyTheory/BlockTheory | 6,363 | Development/AutomorphicArithmetic/ThetaCorrespondence | 16,445 |

### Covolume — depth 4

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 538,520 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 983,754 |
| 2 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 233,931 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 320,422 |
| 3 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 155,106 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 223,446 |
| 4 | Development/AutomorphicSpectrum/Proofs/GeometryProofs | 152,914 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 206,317 |
| 5 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 112,995 | Development/AbelianVarietyTheory/Proofs/FlagMeasures | 199,290 |
| 6 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 106,747 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 177,541 |
| 7 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 99,453 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 171,578 |
| 8 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 90,842 | Development/AutomorphicSpectrum/Proofs/GeometryProofs | 154,798 |
| 9 | Development/AutomorphicSpectrum/Proofs/MetricProofs | 81,943 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 127,520 |
| 10 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 69,857 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 124,429 |
| 11 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 64,690 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 110,969 |
| 12 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 59,890 | Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts | 103,758 |
| 13 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 54,234 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 93,346 |
| 14 | Development/AutomorphicArithmetic/Foundations/Convolution | 53,730 | Development/AutomorphicSpectrum/Proofs/MetricProofs | 82,602 |
| 15 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 46,646 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 79,695 |
| 16 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 40,978 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 76,664 |
| 17 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 38,630 | Development/AutomorphicArithmetic/Foundations/Convolution | 74,044 |
| 18 | GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness | 37,190 | Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs | 69,900 |
| 19 | CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis | 37,014 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 66,802 |
| 20 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 35,695 | Development/AbelianVarietyTheory/Proofs/JetHarmonics | 63,039 |
| 21 | Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof | 35,538 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 56,396 |
| 22 | Development/WeilBound/CoreStatements/HodgeTatePoints | 34,866 | Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization | 54,013 |
| 23 | GroundTheory/HeightsAndTheta/Heights/DiscreteValuationNumbers | 34,685 | GroundTheory/HeightsAndTheta/Heights/HilbertSamuel | 47,491 |
| 24 | Development/WeilBound/CoreStatements/AutomorphicKernels | 30,853 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 44,975 |
| 25 | Development/AutomorphicSpectrum/Proofs/AlgebraProofs | 30,553 | Development/AbelianVarietyTheory/Proofs/GlobalInterpolation | 44,550 |
| 26 | Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs | 29,599 | Development/WeilBound/CoreStatements/AutomorphicKernels | 44,232 |
| 27 | Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations | 29,422 | Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits | 43,210 |
| 28 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 27,869 | GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness | 42,465 |
| 29 | Development/AbelianVarietyTheory/Proofs/ThetaShiftProofs | 27,614 | Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof | 41,959 |
| 30 | Development/WeilBound/CoreStatements/PadicHodgeComparison | 27,487 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 41,886 |

### Window — depth 3

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs | 1,231,723 | Development/AbelianVarietyTheory/Proofs | 2,858,415 |
| 2 | Development/AutomorphicArithmetic/AutomorphicVarieties | 406,592 | Development/AutomorphicArithmetic/AutomorphicVarieties | 613,884 |
| 3 | Development/AutomorphicSpectrum/Proofs | 267,774 | Development/AutomorphicSpectrum/Proofs | 419,124 |
| 4 | Development/AutomorphicArithmetic/Foundations | 265,327 | Formalism/HermitianCurvature/HermitianCurvatureProofs | 297,969 |
| 5 | Development/WeilBound/RepresentationTheoryGL | 137,282 | Development/AutomorphicArithmetic/Foundations | 296,540 |
| 6 | Development/WeilBound/CoreStatements | 83,415 | GroundTheory/HeightsAndTheta/Heights | 260,803 |
| 7 | Development/AbelianVarietyTheory/Definitions | 60,016 | Formalism/LocalToGlobal/SiegelLatticeTheory | 222,987 |
| 8 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 50,475 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 210,866 |
| 9 | Development/AutomorphicArithmetic/IntegralCasts | 47,997 | Development/WeilBound/RepresentationTheoryGL | 166,788 |
| 10 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 39,608 | Development/AbelianVarietyTheory/Definitions | 164,200 |
| 11 | Development/EtaleCohomology/EtaleSheaves | 34,651 | Development/WeilBound/CoreStatements | 150,603 |
| 12 | Development/AutomorphicArithmetic/CommutativeAlgebra | 30,394 | ReciprocityTheory/ReductiveGroups/ArithmeticGeometry | 116,135 |
| 13 | Formalism/LocalToGlobal/SiegelLatticeTheory | 27,663 | Development/ResolutionOfSingularities/EmbeddedResolution | 104,019 |
| 14 | Formalism/PeriodIntegrals/UnitaryGroupMassFormula | 24,855 | Development/AutomorphicArithmetic/IntegralCasts | 91,285 |
| 15 | PositivityTheory/AutomorphicForms/PublishedInputs | 22,045 | ReciprocityTheory/ReductiveGroups/DiscreteSeries | 88,459 |
| 16 | GroundTheory/HeightsAndTheta/Heights | 19,109 | CompanionTheory/SpectralGeometry/LocalGlobalProofs | 53,758 |
| 17 | GroundTheory/AutomorphicForms/GL2 | 18,968 | Formalism/SharpRestriction/CuspSpanNormBounds | 51,822 |
| 18 | Development/WeilBound/ThetaLifts | 18,498 | Development/WeilBound/ThetaLifts | 43,726 |
| 19 | Formalism/SharpRestriction/Divisibility | 14,393 | Formalism/GL3MeanSquares/GenusMeanAsymptotics | 39,611 |
| 20 | Formalism/LocalToGlobal/Columns | 13,045 | Formalism/SharpRestriction/GrowthBounds | 38,817 |
| 21 | GroundTheory/ArithmeticGeometry/SchemeCohomology | 10,876 | Development/EtaleCohomology/EtaleSheaves | 37,445 |
| 22 | Development/AutomorphicArithmetic/WhittakerHecke | 9,362 | Development/AutomorphicArithmetic/CommutativeAlgebra | 36,410 |
| 23 | Formalism/LocalToGlobal/IndefiniteReal | 8,739 | Formalism/LocalToGlobal/TorsionIntegrality | 36,312 |
| 24 | Formalism/SatakeDualWeyl/AdelicIwasawaHecke | 8,502 | Formalism/LocalToGlobal/Columns | 30,279 |
| 25 | Development/EtaleCohomology/TateTwists | 8,211 | PositivityTheory/AutomorphicForms/PublishedInputs | 27,197 |
| 26 | GroundTheory/GlobalFields/TateThesis | 7,708 | Formalism/SharpRestriction/Divisibility | 25,828 |
| 27 | Formalism/PieriBlockIdeals/PieriColumnMinors | 7,470 | Development/AbelianVarietyTheory/BlockTheory | 25,805 |
| 28 | Development/AbelianVarietyTheory/PublishedTheorems | 5,391 | Formalism/LocalToGlobal/IndefiniteReal | 22,295 |
| 29 | Formalism/SharpRestriction/LevelLetterCocycles | 5,329 | Formalism/SharpRestriction/LevelLetterCocycles | 21,494 |
| 30 | GroundTheory/AutomorphicForms/CuspidalDiscreteness | 5,253 | GroundTheory/AutomorphicForms/GL2 | 20,653 |

### Window — depth 4

| Rank | Single-target directory | Lines | All-candidates directory | Lines |
|---|---|---|---|---|
| 1 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 389,699 | Development/AbelianVarietyTheory/Proofs/DivisorProofs | 931,935 |
| 2 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 252,174 | Development/AutomorphicSpectrum/Proofs/BlockDecomposition | 321,265 |
| 3 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 161,829 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 222,001 |
| 4 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 137,749 | Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument | 214,285 |
| 5 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 123,785 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 207,177 |
| 6 | Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues | 109,928 | Development/AbelianVarietyTheory/Proofs/FlagMeasures | 198,108 |
| 7 | Development/AutomorphicArithmetic/Foundations/Convolution | 71,497 | Development/AutomorphicArithmetic/Foundations/GaloisRepresentations | 178,833 |
| 8 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 70,066 | Development/AbelianVarietyTheory/Proofs/TwistedOperators | 177,226 |
| 9 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 67,564 | Development/AbelianVarietyTheory/Proofs/FoundationProofs | 171,223 |
| 10 | Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition | 59,768 | Development/AbelianVarietyTheory/Proofs/ModuliProofs | 110,850 |
| 11 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 59,740 | Formalism/LocalToGlobal/SiegelLatticeTheory/CokernelGLCounts | 103,758 |
| 12 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 54,227 | Development/AbelianVarietyTheory/Proofs/DegenerationProofs | 93,336 |
| 13 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 52,953 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 88,978 |
| 14 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 46,634 | Development/AutomorphicArithmetic/Foundations/Convolution | 82,994 |
| 15 | Development/AutomorphicArithmetic/IntegralCasts/CapelliIdentities | 46,373 | Development/AbelianVarietyTheory/Proofs/SatakeParameters | 77,215 |
| 16 | CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis | 37,013 | Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs | 69,719 |
| 17 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 36,777 | Development/AbelianVarietyTheory/Proofs/UniformizationProofs | 66,807 |
| 18 | Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules | 36,362 | Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange | 56,398 |
| 19 | Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof | 35,538 | Development/ResolutionOfSingularities/EmbeddedResolution/IdealPrincipalization | 54,011 |
| 20 | Development/WeilBound/CoreStatements/AutomorphicKernels | 31,839 | Development/AbelianVarietyTheory/Proofs/JetHarmonics | 52,112 |
| 21 | Development/AbelianVarietyTheory/Proofs/AdelicLatticeProofs | 28,169 | Development/AbelianVarietyTheory/Proofs/GlobalInterpolation | 44,218 |
| 22 | Development/WeilBound/CoreStatements/PadicHodgeComparison | 27,480 | Development/WeilBound/CoreStatements/AutomorphicKernels | 44,048 |
| 23 | Development/AutomorphicArithmetic/AutomorphicVarieties/WeakShimuraTheory | 25,773 | Formalism/LocalToGlobal/SiegelLatticeTheory/ClosedLocalOrbits | 43,210 |
| 24 | Development/WeilBound/RepresentationTheoryGL/UnitaryDualProof | 22,233 | GroundTheory/HeightsAndTheta/Heights/HilbertSamuel | 43,126 |
| 25 | Development/AutomorphicArithmetic/AutomorphicVarieties/LiteratureResults | 22,077 | Development/AutomorphicArithmetic/AutomorphicVarieties/PatchingModules | 42,977 |
| 26 | Development/AbelianVarietyTheory/Proofs/AbelianSchemeLawProofs | 21,599 | Development/WeilBound/RepresentationTheoryGL/SiegelWeilProof | 41,959 |
| 27 | Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations | 20,371 | Development/AbelianVarietyTheory/Proofs/SiegelThetaTransformation | 41,736 |
| 28 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 19,119 | Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors | 41,631 |
| 29 | Development/AutomorphicArithmetic/AutomorphicVarieties/BuildingsResidueChars | 18,065 | Development/AbelianVarietyTheory/Proofs/UnitaryExistence | 41,526 |
| 30 | Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary | 16,829 | Development/AbelianVarietyTheory/Definitions/Divisors | 39,907 |

## Appendix B. Hub statements

**READ / COMPILED** These are the complete written declaration headers from the pinned source. The first 40 appear in headline-depth order for the single-target line ranking. Additional declarations needed for the all-candidates line ranking follow. Shared statements appear once. “Rank” in this appendix always refers to descending strict descendant lines.

### riemannHypothesis

**READ / COMPILED** `Main.lean:4` · single-target rank 1 · all-candidates rank 1.

```lean
theorem riemannHypothesis : RiemannHypothesis
```

### rhOfAll

**READ / COMPILED** `Supplements/Kernels/MainTheorems.lean:9` · single-target rank 2 · all-candidates rank 2.

```lean
theorem rhOfAll : RiemannHypothesis
```

### allChi

**READ / COMPILED** `Supplements/Kernels/MainTheorems.lean:7` · single-target rank 3 · all-candidates rank 3.

```lean
theorem allChi : UpperTheory.EveryCharacter
```

### UpperTheory.FinalTheorems.everyCharacter

**READ / COMPILED** `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:10` · single-target rank 4 · all-candidates rank 4.

```lean
theorem UpperTheory.FinalTheorems.everyCharacter : UpperTheory.EveryCharacter
```

### UpperTheory.FinalTheorems.everyCharacter_of_row

**READ / COMPILED** `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:7` · single-target rank 5 · all-candidates rank 5.

```lean
theorem UpperTheory.FinalTheorems.everyCharacter_of_row (h : UpperTheory.GalStar.Row0b fun h rc => UpperTheory.Zero.LLC.IsRecT h rc) : UpperTheory.EveryCharacter
```

### UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:810` · single-target rank 6 · all-candidates rank 6.

```lean
theorem UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin (O : _root_.UpperTheory.LiteratureTheorems.OpenLiteratureStatements) (hV : UpperTheory.Top.VWin) : UpperTheory.EveryCharacter
```

### UpperTheory.Lit.every_character_of_theta_integrals_local_matching

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69` · single-target rank 7 · all-candidates rank 7.

```lean
theorem every_character_of_theta_integrals_local_matching (P : _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses) (F : _root_.GlobalTheory.FunPr.ThetaLocalInputs) (hA : GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree)
    (hM : GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching) (hX : _root_.GlobalTheory.CovTop.CovolumeBoundOfX) (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (hV : VWin) :
    UpperTheory.EveryCharacter
```

### SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolSlim2Use.lean:16` · single-target rank 15 · all-candidates rank 12.

```lean
theorem topCovolSlim2_use_alt_alt : GlobalTheory.CompanionTheory.Hypotheses₂.ResolutionCharZero → GlobalTheory.CompanionTheory.Hypotheses₂.PrincipalisationCharZero → GlobalTheory.CompanionTheory.Hypotheses₂.PoincareLelongInv → PositivityTheory.MbHsUse.HSUse → ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.MoriwakiBigStatement → HT.FarguesExact → GR.ZarhinStatement → Pub.NefRR → GlobalTheory.Published.SiegelToroidalIntegral → GlobalTheory.Published.ToroidalForFanKS → GlobalTheory.Published.SemiAbelianLieSeminegative → GlobalTheory.Published.PointSeparationPair → GlobalTheory.Published.ArDegree → _root_.GlobalTheory.CovTop.PublishedHodgeBundleTheorems → GlobalTheory.Published.GrothendieckDeformation → _root_.GlobalTheory.CovTop.CovolumeBoundOfX
```

### UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:44` · single-target rank 8 · all-candidates rank 8.

```lean
theorem nonempty_hyps_definite_side_of_closed_bound : _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses → _root_.GlobalTheory.FunPr.ThetaLocalInputs → GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.ThetaIntegralsAgree → GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.LocalMatching → _root_.GlobalTheory.CovTop.CovolumeBoundOfX → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists), (∀ cDep : ℝ, _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfDependence hL cDep) (fun Q L => _root_.GlobalTheory.Fc.R1.SlotNormCondition Q L fun 𝒞 => Formalism.MainNotions.Closed 𝒞 fun Fm _ => _root_.GlobalTheory.NLink.BoundAtTwoThreeFamilyFonAlt Fm)) → Nonempty (_root_.GlobalTheory.Fc.HypsAlt S0.NL _root_.GlobalTheory.Fc.DefiniteSideCondition)
```

### PositivityTheory.HtPt.Ah.deep_slim_use

**READ / COMPILED** `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/AhSlimU.lean:9` · single-target rank 28 · all-candidates rank 17.

```lean
theorem deep_slim_use (h₁ : GlobalTheory.CompanionTheory.Hypotheses₂.ResolutionCharZero) (h₂ : GlobalTheory.CompanionTheory.Hypotheses₂.PrincipalisationCharZero)
    (hPL : GlobalTheory.CompanionTheory.Hypotheses₂.PoincareLelongInv) (hU : PositivityTheory.MbHsUse.HSUse)
    (hBig : ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.MoriwakiBigStatement) (hF : HT.FarguesExact) (hZ : GR.ZarhinStatement)
    (hN : Pub.NefRR) : Plug.DeepStR
```

### SelfIntersectionVolumeEstimates.topCovolG_alt_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolG.lean:39` · single-target rank 32 · all-candidates rank outside 40.

```lean
theorem topCovolG_alt_alt : _root_.SelfIntersectionVolumeEstimates.VolumeEstimateHypotheses → GlobalTheory.CovTop.HypothesesX → _root_.GlobalTheory.CovTop.PublishedHodgeBundleTheorems → GlobalTheory.CovHt.HypothesesH → GlobalTheory.Published.GrothendieckDeformation → GlobalTheory.HSCore.Quoted → GlobalTheory.CompanionTheory.Ar.Plug.DeepStR → _root_.GlobalTheory.CovTop.CovolumeBoundOfX
```

### GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean:41` · single-target rank 9 · all-candidates rank 9.

```lean
theorem hypotheses_nonempty_of_unramified_exponents_alt : _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses → S0.RowRat → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (cDep : ℝ) (A : GroupRetwisting.AtP), EvLgG A → _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfDependence hL cDep) (fun Q L => _root_.GlobalTheory.Fc.R1.SlotNormCondition Q L fun 𝒞 => Formalism.MainNotions.Closed 𝒞 fun Fm _ => _root_.GlobalTheory.NLink.BoundAtTwoThreeFamilyFonAlt Fm) → _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)) _root_.GlobalTheory.Fc.S0.FunctionalCondition → _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)) _root_.GlobalTheory.Fc.S0.CovolumeBoundThirdPlaceSeries → Nonempty (_root_.GlobalTheory.Fc.HypsAlt S0.NL _root_.GlobalTheory.Fc.DefiniteSideCondition)
```

### GlobalTheory.T.open0_of_unitary_group_hypotheses

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:75` · single-target rank 13 · all-candidates rank 20.

```lean
theorem _root_.GlobalTheory.T.open0_of_unitary_group_hypotheses : _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (cDep : ℝ), _root_.GlobalTheory.Fc.S0.OpenParameterStatements (_root_.GlobalTheory.Mem.Top.Bl.parametersOfDependence hL cDep)
```

### GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SurjectiveAndLowWeightOfUnramifiedExponents.lean:16` · single-target rank 24 · all-candidates rank 16.

```lean
theorem ontoX_and_lamLow_of_unitaryGroupHypotheses' :
    _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses → _root_.GlobalTheory.BigOn.SurjectiveOntoX ∧ _root_.GlobalTheory.BigTop.LambdaLowerBound₂
```

### GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use

**READ / COMPILED** `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/DeepStROfUse.lean:12` · single-target rank 29 · all-candidates rank 18.

```lean
theorem deepStR_of_use : ReciprocityTheory.ChartRestriction.G.Geo.ArithIntersectionSystemStatement → PositivityTheory.MbHsUse.HSUse → ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.MoriwakiBigStatement → ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement → GlobalTheory.Published.SemiAbelianHomExtension → HT.FarguesHodgeTate → Flat.GagaSections → GR.QuotientByFiniteFlatStatement → GR.ZarhinStatement → Pub.NefRR → Plug.DeepStR
```

### GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean:50` · single-target rank 10 · all-candidates rank 29.

```lean
theorem allRows_of_open0_alt : GlobalTheory.Published.GlobalArtinReciprocity → HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent → GlobalTheory.Published.DiscreteSeriesCover → GlobalTheory.Published.HarishChandraModules → GlobalTheory.Published.CuspRapidDecay → GlobalTheory.Published.CasselmanWallach → GlobalTheory.Published.DiscreteSeriesClassification → _root_.GlobalTheory.BigOn.SurjectiveOntoX → _root_.GlobalTheory.BigTop.LambdaLowerBound₂ → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (N : _root_.GlobalTheory.Mem.Top.Bl.NormChoiceExtension hL) (S : SExt) (Γ : GeoP) (NN : FamClass → Prop), _root_.GlobalTheory.Fc.S0.OpenParameterStatements (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) → _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) _root_.GlobalTheory.Fc.S0.CovolumeBoundThirdPlaceSeries → _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) _root_.GlobalTheory.Fc.S0.FunctionalCondition → _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) (fun Q L => _root_.GlobalTheory.Fc.R1.SlotNormCondition Q L NN) → _root_.GlobalTheory.Fc.AllRowsAlt KPx (IsBuiltE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ).s) (IsGoodE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ).s) (_root_.GlobalTheory.Mem.Top.Bl.BundleLinkage (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ)) NN _root_.GlobalTheory.Fc.DefiniteSideCondition
```

### GlobalTheory.T.large_unramified_exponent_bundles_exist_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean:69` · single-target rank 11 · all-candidates rank 10.

```lean
theorem _root_.GlobalTheory.T.large_unramified_exponent_bundles_exist_alt : _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses → S0.RowRat → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (cDep : ℝ) (A : GroupRetwisting.AtP), EvLgG A → StandardLattice.SiegelMassRatioCM ∧ MemberE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)).s ∧ ExBL KPx (IsBuiltE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)).s) (IsGoodE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)).s) (_root_.GlobalTheory.Mem.Top.Bl.BundleLinkage (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)))
```

### GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:39` · single-target rank 14 · all-candidates rank 21.

```lean
theorem open_orbit_of_unramified_exponents_alt : _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (cDep : ℝ), _root_.GlobalTheory.Fc.S0.OpenParameterStatements (_root_.GlobalTheory.Mem.Top.Bl.parametersOfDependence hL cDep)
```

### GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfPrints.lean:28` · single-target rank 27 · all-candidates rank 19.

```lean
theorem ontoX_of_hypotheses_alt_alt : GlobalTheory.Published.GreenCuspidal → GlobalTheory.Published.ClozelCohomological → GlobalTheory.Published.HeckeLAdicCharacter → GlobalTheory.Published.ChebotarevDegreeOne → _root_.UpperTheory.GalS.CuspUAlt → _root_.GlobalTheory.Published.BaseChangeDefiniteUnitaryGroup → GlobalTheory.Published.BhattScholzeCrystallineLattices → GlobalTheory.Published.HeckeLAdicCharacterAbove → GlobalTheory.Published.CuspRapidDecay → _root_.UpperTheory.Zero.LLC.RecTExists → GlobalTheory.Published.DiscreteSeriesCover → GlobalTheory.Published.CasselmanWallach → _root_.GlobalTheory.BigOn.SurjectiveOntoX
```

### UpperTheory.GalC.final_alt_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean:19` · single-target rank 30 · all-candidates rank 15.

```lean
theorem final_alt_alt : _root_.GlobalTheory.NLink.Final.mainTheorem
```

### GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis

**READ / COMPILED** `Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/GoodTowerVolumeTheoremBis.lean:9` · single-target rank 31 · all-candidates rank 27.

```lean
theorem good_tower_volume_theorem_bis :
    ReciprocityTheory.ChartRestriction.G.Geo.ArithIntersectionSystemStatement → PositivityTheory.MbHsUse.HSUse →
    ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.MoriwakiBigStatement → ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement →
    GlobalTheory.Published.SemiAbelianHomExtension → HT.FarguesHodgeTate → Flat.GagaSections →
    GroundTheory.Heights₂.Heights.LineOfLargeDegree.Statement → GR.QuotientByFiniteFlatStatement → GR.ZarhinStatement →
    Top.GoodTowerExistsX ∧ Top.VolumeTheoremX
```

### GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean:51` · single-target rank 36 · all-candidates rank outside 40.

```lean
theorem _root_.GlobalTheory.T.hyps_e_third_layer_ser_n_of_geometric_galois : _root_.GlobalTheory.Mem.LiteralAutomorphy.NonEndoscopicHypothesesAlt → _root_.GlobalTheory.NRows.GeometricGaloisRepCompatibility → _root_.GlobalTheory.Mem.Top.Bl.EllipticHypothesis ∧ _root_.GlobalTheory.HeightCounting.Up.PublishedInputsThirdLayerAlt ∧ SerN ∧ ∃ hL : _root_.UpperTheory.Zero.LLC.RecTExists, _root_.GlobalTheory.Mem.Top.Bl.LocalLanglandsHypothesis hL
```

### GlobalTheory.Fc.StageOneU.member_bundles_large_unramified_exponents_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean:34` · single-target rank 12 · all-candidates rank 11.

```lean
theorem member_bundles_large_unramified_exponents_alt : _root_.GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses → S0.RowRat →
    ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (cDep : ℝ) (A : GroupRetwisting.AtP), EvLgG A →
      StandardLattice.SiegelMassRatioCM ∧
      MemberE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)).s ∧
      ExBL KPx (IsBuiltE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)).s)
        (IsGoodE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)).s)
        (_root_.GlobalTheory.Mem.Top.Bl.BundleLinkage (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.Mem.LiteralAutomorphy.extensionWithAtProperty hL (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) A) SExt.none (geoCl anyGeometry)))
```

### GlobalTheory.T.main_theorem_published_inputs_third_alt_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean:34` · single-target rank 18 · all-candidates rank outside 40.

```lean
theorem _root_.GlobalTheory.T.main_theorem_published_inputs_third_alt_alt : GlobalTheory.Published.HarishChandraFinite → GlobalTheory.Published.CuspRapidDecay → GlobalTheory.Published.DiscreteSeriesCover → GlobalTheory.Published.HarishChandraModules → GlobalTheory.Published.CasselmanWallach → GlobalTheory.Hk3.HoweUnram → GlobalTheory.Published.WeilRepresentationUnitaryPair → GlobalTheory.Published.WeilSiegelFormulaUnitary → GlobalTheory.Published.SiegelWeilUnitaryConvergent → _root_.GlobalTheory.Published.DoublingMethodLocalZetaIntegrals → GlobalTheory.Published.UnramifiedDoublingGL → GlobalTheory.Published.DiscreteSeriesClassification → GlobalTheory.Published.StrongApproxSU → HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (N : _root_.GlobalTheory.Mem.Top.Bl.NormChoiceExtension hL) (S : SExt) (Γ : GeoP), _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) (fun Q L => Row Q L (AtAll fun _ _ _ (b : _root_.GlobalTheory.Fc.BundleCondition _ _ _) => (b.B.Q.Rl.toCx3 b.B.Q.F).MIstar2 (b.B.Q.F.eV (b.B.Q.Rl.toCx3 b.B.Q.F).zs) b.B.Q.sEE)) ∧ _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) _root_.GlobalTheory.Fc.RL.RowMultiplicityCondition
```

### GlobalTheory.LocalRows.lg1_sLp_sO_hTF

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean:27` · single-target rank 20 · all-candidates rank outside 40.

```lean
theorem lg1_sLp_sO_hTF : HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent → ∀ (KP : ∀ B : GlobalTheory.Mem.Base, Fr B.toPre → Prop) (Q Q' : V4.Slot) (Lk : LkT _root_.GlobalTheory.Fc.BundleCondition), (Lg1 KP Q Q' fun S => _root_.GlobalTheory.Fc.R1.SlotLpCondition S Lk) ∧ (Lg1 KP Q Q' fun S => _root_.GlobalTheory.Fc.R1.SlotOrderCondition S Lk) ∧ Lg1 KP Q Q' fun S => _root_.GlobalTheory.Fc.R1.SlotTorsionFreeCondition S Lk
```

### GlobalTheory.T.final_theorem_of_inputs_right

**READ / COMPILED** `Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRightStatement.lean:19` · single-target rank 34 · all-candidates rank 30.

```lean
theorem _root_.GlobalTheory.T.final_theorem_of_inputs_right : (PartI ∧ N1ab ∧ N1c ∧ ∀ (E : Type) [Field E] [NumberField E] [IsCMField E] (H : Host E) (D : Datum H), ToroidalLevelCompatibility (D := D) ∧ ToroidalHeckeCompatibility (D := D)) → KeyFormula → GlobalTheory.Published.SemiAbelianHomExtension → GroundTheory.Heights₂.Heights.NumbersDVR.NumericalSegre.Statement → ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement → HT.FarguesHodgeTate → Flat.GagaSections → GroundTheory.Heights₂.Heights.LineOfLargeDegree.Statement → PB.Inputs → Prov.HS → Prov.An → Prov.ZhangDimensionPushDownGrassmannianHeightBounds → ReciprocityTheory.ChartRestriction.G.Geo.PtsIntegrableStatement → ReciprocityTheory.ChartRestriction.G.AI.I2.AvoidStatement → GlobalTheory.CompanionTheory.Ar.GR.QuotientByFiniteFlatStatement → GlobalTheory.CompanionTheory.Ar.GR.ZarhinStatement → ThetaUnifAV → Top.GoodTowerExistsX ∧ Top.VolumeTheoremX
```

### GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ThetaLiftHypothesesOfNonvanishing.lean:24` · single-target rank 37 · all-candidates rank outside 40.

```lean
theorem GlobalTheory.MemberClose.exists_hyp_n_of_geometric_galois_compat : _root_.GlobalTheory.Mem.LiteralAutomorphy.NonEndoscopicHypothesesAlt → _root_.GlobalTheory.NRows.GeometricGaloisRepCompatibility → _root_.GlobalTheory.Mem.Top.Bl.EllipticHypothesis ∧ _root_.GlobalTheory.HeightCounting.Up.PublishedInputsThirdLayerAlt ∧ SerN ∧ ∃ hL : _root_.UpperTheory.Zero.LLC.RecTExists, _root_.GlobalTheory.Mem.Top.Bl.LocalLanglandsHypothesis hL
```

### GlobalTheory.BigOn.ontoX_of_twist_shares_exp_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OntoXOfTwistSharesExp.lean:21` · single-target rank 38 · all-candidates rank outside 40.

```lean
theorem ontoX_of_twist_shares_exp_alt : _root_.GlobalTheory.BigOn.ExportedStatement → _root_.GlobalTheory.BigOn.TwistStatement' → _root_.GlobalTheory.BigOn.ShareStatement → _root_.GlobalTheory.BigOn.BadPlacesStatement → _root_.GlobalTheory.BigOn.ExponentStatement → _root_.GlobalTheory.BigOn.SurjectiveOntoX
```

### GlobalTheory.T.member_exists_baseLattice_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean:80` · single-target rank 16 · all-candidates rank 13.

```lean
theorem _root_.GlobalTheory.T.member_exists_baseLattice_alt : _root_.GlobalTheory.Mem.Top.Bl.HypAAlt → _root_.GlobalTheory.Mem.Top.Bl.EllipticHypothesis → _root_.GlobalTheory.Mem.Top.Bl.MultiplicityCoverHypotheses → ExistsUnlocalizedSaturatedState → ∀ hL : _root_.UpperTheory.Zero.LLC.RecTExists, _root_.GlobalTheory.Mem.Top.Bl.LocalLanglandsHypothesis hL → ∀ cDep : ℝ, _root_.GlobalTheory.Mem.Top.Bl.MultiplicityCondition (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)) → MemberE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)).s ∧ GlobalTheory.Fc.ExBL KPx (IsBuiltE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)).s) (IsGoodE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)).s) (_root_.GlobalTheory.Mem.Top.Bl.BundleLinkage (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)))
```

### GlobalTheory.miStarRow_alt_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MainTheoremPublishedInputsThird.lean:22` · single-target rank 19 · all-candidates rank outside 40.

```lean
theorem miStarRow_alt_alt : GlobalTheory.Published.HarishChandraFinite → GlobalTheory.Published.CuspRapidDecay → GlobalTheory.Published.DiscreteSeriesCover → GlobalTheory.Published.HarishChandraModules → GlobalTheory.Published.CasselmanWallach → GlobalTheory.Hk3.HoweUnram → GlobalTheory.Published.WeilRepresentationUnitaryPair → GlobalTheory.Published.WeilSiegelFormulaUnitary → GlobalTheory.Published.SiegelWeilUnitaryConvergent → _root_.GlobalTheory.Published.DoublingMethodLocalZetaIntegrals → GlobalTheory.Published.UnramifiedDoublingGL → GlobalTheory.Published.DiscreteSeriesClassification → GlobalTheory.Published.StrongApproxSU → HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent → ∀ (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (N : _root_.GlobalTheory.Mem.Top.Bl.NormChoiceExtension hL) (S : SExt) (Γ : GeoP), _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) (fun Q L => Row Q L (AtAll fun _ _ _ (b : _root_.GlobalTheory.Fc.BundleCondition _ _ _) => (b.B.Q.Rl.toCx3 b.B.Q.F).MIstar2 (b.B.Q.F.eV (b.B.Q.Rl.toCx3 b.B.Q.F).zs) b.B.Q.sEE)) ∧ _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N S Γ) _root_.GlobalTheory.Fc.RL.RowMultiplicityCondition
```

### GlobalTheory.LocalRows.sLp_sO_hTF_of_siegelWeil

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean:24` · single-target rank 21 · all-candidates rank outside 40.

```lean
theorem sLp_sO_hTF_of_siegelWeil : HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent → ∀ (Q : V4.Slot) (Lk : LkT _root_.GlobalTheory.Fc.BundleCondition), _root_.GlobalTheory.Fc.R1.SlotLpCondition Q Lk ∧ _root_.GlobalTheory.Fc.R1.SlotOrderCondition Q Lk ∧ _root_.GlobalTheory.Fc.R1.SlotTorsionFreeCondition Q Lk
```

### GlobalTheory.CompanionTheory.Ar.Top.goodTower_volume_of_reduced

**READ / COMPILED** `Development/AutomorphicSpectrum/Proofs/GeometryProofs/FinalTheoremOfInputsRight.lean:28` · single-target rank 35 · all-candidates rank 31.

```lean
theorem goodTower_volume_of_reduced : (PartI ∧ N1ab ∧ N1c ∧ ∀ (E : Type) [Field E] [NumberField E] [IsCMField E] (H : Host E) (D : Datum H), ToroidalLevelCompatibility (D := D) ∧ ToroidalHeckeCompatibility (D := D)) → KeyFormula → GlobalTheory.Published.SemiAbelianHomExtension → GroundTheory.Heights₂.Heights.NumbersDVR.NumericalSegre.Statement → ReciprocityTheory.ChartRestriction.G.Geo.ResK.ResKStatement → HT.FarguesHodgeTate → Flat.GagaSections → GroundTheory.Heights₂.Heights.LineOfLargeDegree.Statement → PB.Inputs → Prov.HS → Prov.An → Prov.ZhangDimensionPushDownGrassmannianHeightBounds → ReciprocityTheory.ChartRestriction.G.Geo.PtsIntegrableStatement → ReciprocityTheory.ChartRestriction.G.AI.I2.AvoidStatement → GlobalTheory.CompanionTheory.Ar.GR.QuotientByFiniteFlatStatement → GlobalTheory.CompanionTheory.Ar.GR.ZarhinStatement → ThetaUnifAV → Top.GoodTowerExistsX ∧ Top.VolumeTheoremX
```

### GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_prime_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean:57` · single-target rank 17 · all-candidates rank 14.

```lean
theorem exists_baseLattice_of_prime_alt : _root_.GlobalTheory.Mem.Top.Bl.HypAAlt → _root_.GlobalTheory.Mem.Top.Bl.EllipticHypothesis → _root_.GlobalTheory.Mem.Top.Bl.MultiplicityCoverHypotheses → ExistsUnlocalizedSaturatedState → ∀ hL : _root_.UpperTheory.Zero.LLC.RecTExists, _root_.GlobalTheory.Mem.Top.Bl.LocalLanglandsHypothesis hL → ∀ cDep : ℝ,
    _root_.GlobalTheory.Mem.Top.Bl.MultiplicityCondition (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)) → MemberE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)).s ∧
      GlobalTheory.Fc.ExBL KPx (IsBuiltE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)).s)
        (IsGoodE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)).s) (_root_.GlobalTheory.Mem.Top.Bl.BundleLinkage (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension (_root_.GlobalTheory.HeightCounting.Up.extensionWithOrigin hL cDep) SExt.none (geoCl anyGeometry)))
```

### GlobalTheory.LocalRows.at_choice_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/AtChoice.lean:16` · single-target rank 22 · all-candidates rank outside 40.

```lean
theorem at_choice_alt (hSW : HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent) (𝒜 : FamClass) (σ : RawSel _root_.GlobalTheory.Fc.BundleCondition 𝒜) :
    _root_.GlobalTheory.Fc.R1.SelectionLpBound 𝒜 σ ∧ _root_.GlobalTheory.Fc.R1.SelectionOrderBound 𝒜 σ ∧ R1.H_hTF 𝒜
```

### GlobalTheory.T.diagonalRow_of_siegelWeil_unitary

**READ / COMPILED** `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DiagonalRowOfSiegelWeilUnitaryStatement.lean:45` · single-target rank 25 · all-candidates rank outside 40.

```lean
theorem _root_.GlobalTheory.T.diagonalRow_of_siegelWeil_unitary : HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent → GlobalTheory.Core.Rk.RowDiag (fun D L C' => GlobalTheory.Core.Rk.IsScaleWithBoundedGamma D L C' ∧ ∀ u, GlobalTheory.Core.Rk.RankMu D u)
```

### GlobalTheory.Mem.Top.Bl.exists_baseLattice_of_pair_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExistsBaseLatticeOfPrime.lean:36` · single-target rank 23 · all-candidates rank 40.

```lean
theorem exists_baseLattice_of_pair_alt (hA : _root_.GlobalTheory.Mem.Top.Bl.HypAAlt) (hE : _root_.GlobalTheory.Mem.Top.Bl.EllipticHypothesis) (hH : _root_.GlobalTheory.Mem.Top.Bl.MultiplicityCoverHypotheses) (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (hN : _root_.GlobalTheory.Mem.Top.Bl.LocalLanglandsHypothesis hL) (N Ng : _root_.GlobalTheory.Mem.Top.Bl.NormChoiceExtension hL)
    (toB : ∀ K B f T w Z Wt p0 t nch n xd c, N K B f T w Z Wt p0 t nch n xd c → Nonempty (_root_.GlobalTheory.HeightCounting.Up.extensionWithLaw hL K B f T w Z Wt p0 t nch n xd c))
    (toN : ∀ K B f T w Z Wt p0 t nch n xd c, Ng K B f T w Z Wt p0 t nch n xd c →
      Nonempty (N K B f T w Z Wt p0 t nch n xd c) ∧ GoodO (w.D Z) nch xd)
    (has3 : StepW Start (Has3 (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)).s))
    (lv : LevelThreeCondition (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)).s) (lvg : LevelThreeCondition (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension Ng SExt.none (geoCl anyGeometry)).s)
    (intersection_update_fsHerm_neg_one : PositionMv (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)).s)
    (second : Pass KPx (IsBuiltE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)).s) fun K B f T =>
      ∃ w : ColW B f T, Start K B f T w ∧ Has3 (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension Ng SExt.none (geoCl anyGeometry)).s K B f T w)
    (hMQ : _root_.GlobalTheory.Mem.Top.Bl.MultiplicityCondition (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry))) :
    MemberE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)).s ∧
      GlobalTheory.Fc.ExBL KPx (IsBuiltE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)).s) (IsGoodE (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)).s)
        (_root_.GlobalTheory.Mem.Top.Bl.BundleLinkage (_root_.GlobalTheory.Mem.Top.Bl.parametersOfExtension N SExt.none (geoCl anyGeometry)))
```

### GlobalTheory.Core.Rk.rowDiag_of_siegelWeilUnitary

**READ / COMPILED** `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/DiagonalRowOfSiegelWeilUnitary.lean:50` · single-target rank 26 · all-candidates rank outside 40.

```lean
theorem rowDiag_of_siegelWeilUnitary
    (hSW : HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent) :
    GlobalTheory.Core.Rk.RowDiag (fun D L C' => GlobalTheory.Core.Rk.IsScaleWithBoundedGamma D L C' ∧ ∀ u, GlobalTheory.Core.Rk.RankMu D u)
```

### GlobalTheory.CarrierGap.offDiag

**READ / COMPILED** `Development/AbelianVarietyTheory/Proofs/FlagMeasures/OffK0Closed.lean:673` · single-target rank 33 · all-candidates rank outside 40.

```lean
theorem offDiag : PI.VolStabS.MassDataS.SWXS → Formalism.L2.SG.RowsPos.RowNGP → Formalism.L2.SG.RowsDef.RowsFinDim → ∀ (𝒞 : FamClass) (sel : SSel 𝒞), (∀ {eps : ℝ} (Fm : FamP eps) (hc : 𝒞 Fm) x (hx : Fm.x1 < x) (h0 : (sel Fm hc).1 ≤ x) (i : Fm.Ix x), Formalism.L2.SG.Pf.LocCP.LocTied (Fm.D x i)) → Formalism.L2.SG.Pf.SzHypFam.RanksRow 3 𝒞 → LoopRowS 3 𝒞 sel → Closed 𝒞 fun Fm _ => ∀ hc : 𝒞 Fm, TheoremSSelected Fm 3 (sel Fm hc)
```

### GlobalTheory.T.corankOnePairsFamilyBounds_of_siegelWeil

**READ / COMPILED** `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/CorankOnePairsFamilyBoundsOfSiegelWeilStatement.lean:45` · single-target rank 39 · all-candidates rank outside 40.

```lean
theorem _root_.GlobalTheory.T.corankOnePairsFamilyBounds_of_siegelWeil : HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent → ∀ c : ℝ, GlobalTheory.Core.Diag.OneOn {c} true ∧ GlobalTheory.Core.Diag.OneOn {c} false
```

### GlobalTheory.Core.Diag.oneOn_singleton_of_siegelWeil

**READ / COMPILED** `Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/CorankOnePairsFamilyBoundsOfSiegelWeil.lean:10` · single-target rank 40 · all-candidates rank outside 40.

```lean
theorem oneOn_singleton_of_siegelWeil :
    HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent →
      ∀ c : ℝ, GlobalTheory.Core.Diag.OneOn {c} true ∧ GlobalTheory.Core.Diag.OneOn {c} false
```

### UpperTheory.One.vwin_of_row

**READ / COMPILED** `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean:4` · single-target rank outside 40 · all-candidates rank 22.

```lean
theorem UpperTheory.One.vwin_of_row (h : UpperTheory.GalStar.Row0b fun h rc => UpperTheory.Zero.LLC.IsRecT h rc) : UpperTheory.Top.VWin
```

### UpperTheory.One.Join.automorphic_window_of_inputs

**READ / COMPILED** `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TopMainZj.lean:71` · single-target rank outside 40 · all-candidates rank 23.

```lean
theorem UpperTheory.One.Join.automorphic_window_of_inputs (O : _root_.UpperTheory.LiteratureTheorems.OpenImageCondition)
 (bc : _root_.PositivityTheory.Rg.BcN.BaseChangeIsobaricN) (gal : _root_.UpperTheory.V.Z.Win.RowT) :
    UpperTheory.Top.VWin
```

### UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm

**READ / COMPILED** `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TopMainZj.lean:55` · single-target rank outside 40 · all-candidates rank 24.

```lean
theorem UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm (O : _root_.UpperTheory.LiteratureTheorems.OpenImageCondition)
 (bc : _root_.PositivityTheory.Rg.BcN.BaseChangeIsobaricN) (gal : _root_.UpperTheory.V.Z.Win.RowT) (cm : _root_.GlobalTheory.Mem.LiteralAutomorphy.LiteratureCMHypothesis) :
    UpperTheory.Top.VWin
```

### UpperTheory.Top.every_character_of_green_v_win

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean:16` · single-target rank outside 40 · all-candidates rank 33.

```lean
theorem UpperTheory.Top.every_character_of_green_v_win (hG : GlobalTheory.GLq.Green) (hV : UpperTheory.Top.VWin)
    (h : Nonempty (_root_.GlobalTheory.Fc.HypsAlt (fun 𝒞 => Closed 𝒞 fun Fm _ => LinkN Fm) _root_.GlobalTheory.Fc.DefiniteSideCondition)) : UpperTheory.EveryCharacter
```

### UpperTheory.V.v_window_of_literal_automorphy_n

**READ / COMPILED** `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WindowBoundOfLiteratureLevel.lean:33` · single-target rank outside 40 · all-candidates rank 25.

```lean
theorem UpperTheory.V.v_window_of_literal_automorphy_n (hN : _root_.GlobalTheory.Mem.LiteralAutomorphy.LiteratureRankNHypothesis) : VWin
```

### UpperTheory.Top.zero_free_all_of_green_v_win

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean:12` · single-target rank outside 40 · all-candidates rank 34.

```lean
theorem UpperTheory.Top.zero_free_all_of_green_v_win (hG : GlobalTheory.GLq.Green) (hV : UpperTheory.Top.VWin)
    (h : Nonempty (_root_.GlobalTheory.Fc.HypsAlt (fun 𝒞 => Closed 𝒞 fun Fm _ => LinkN Fm) _root_.GlobalTheory.Fc.DefiniteSideCondition)) : Formalism.HC.ZeroFreeAll
```

### UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd

**READ / COMPILED** `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WindowBoundOfLiteratureLevel.lean:30` · single-target rank outside 40 · all-candidates rank 26.

```lean
theorem v_window_of_automorphy_csd_ss_mono_odd (hN : _root_.GlobalTheory.Mem.LiteralAutomorphy.LiteratureRankNHypothesis) : VWin
```

### UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WindowBoundOfLiteratureLevel.lean:25` · single-target rank outside 40 · all-candidates rank 28.

```lean
theorem vwin_of_hypotheses_H_E_alt (hH : _root_.UpperTheory.V.Af.HypothesesH') : VWin
```

### UpperTheory.GalC.final_of_alt

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean:75` · single-target rank outside 40 · all-candidates rank 32.

```lean
theorem final_of_alt (hP : Hypotheses₂) (hG : _root_.UpperTheory.GalC.CutGivesAlt) (prN : _root_.GlobalTheory.HeightCounting.Up.PublishedInputsThirdLayerAlt) (hX : _root_.GlobalTheory.NRows.GeometricGaloisRepCompatibility)
    (dzs : GlobalTheory.Published.DepthZeroSupport) (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (cDep : ℝ)
    (hF : _root_.GlobalTheory.HeightCounting.Up.MemberAtLayerPoint hL fun _ _ _ _ w Z _ _ _ nch _ _ => _root_.UpperTheory.GalC.GaloisPreconditions (w.D Z) nch)
    (hAt : _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfDependence hL cDep) (fun Q L => _root_.GlobalTheory.Fc.R1.SlotNormCondition Q L fun 𝒞 => Formalism.MainNotions.Closed 𝒞 fun Fm _ => _root_.GlobalTheory.NLink.BoundAtTwoThreeFamilyFonAlt Fm)) :
    _root_.GlobalTheory.Fc.RL.LinkedAt (_root_.GlobalTheory.Mem.Top.Bl.parametersOfDependence hL cDep) (fun Q L => _root_.GlobalTheory.Fc.R1.SlotNormCondition Q L fun 𝒞 => Formalism.MainNotions.Closed 𝒞 fun Fm _ => Formalism.MainNotions.LinkN Fm)
```

### UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean:64` · single-target rank outside 40 · all-candidates rank 37.

```lean
theorem linkedAt_linkN_of_boundAtTwoThree (hP : Hypotheses₂) (hG : _root_.UpperTheory.GalC.CutGivesAlt) (hL : _root_.UpperTheory.Zero.LLC.RecTExists) (p : _root_.GlobalTheory.Mem.Top.Bl.Parameters hL)
    (h1 : _root_.GlobalTheory.Fc.RL.LinkedAt p (fun S L => GlobalTheory.Fc.RowE S L fun _ D O _ _ => _root_.UpperTheory.GalC.GaloisPreconditions D O.ex.nch ∧ Tie4 D))
    (h3 : _root_.GlobalTheory.Fc.RL.LinkedAt p (fun S L => _root_.GlobalTheory.Fc.R1.SlotNormCondition S L fun 𝒞 => Closed 𝒞 fun Fm _ => _root_.GlobalTheory.NLink.BoundAtTwoThreeFamilyFonAlt Fm)) :
    _root_.GlobalTheory.Fc.RL.LinkedAt p (fun S L => _root_.GlobalTheory.Fc.R1.SlotNormCondition S L fun 𝒞 => Closed 𝒞 fun Fm _ => Formalism.MainNotions.LinkN Fm)
```

### GlobalTheory.T.good_tower_volume_theorem

**READ / COMPILED** `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheoremStatement.lean:26` · single-target rank outside 40 · all-candidates rank 35.

```lean
theorem _root_.GlobalTheory.T.good_tower_volume_theorem : Top.Given → PtsIntegrableStatement → ReciprocityTheory.ChartRestriction.G.AI.I2.AvoidStatement → Out.WeilSt → GlobalTheory.CompanionTheory.Ar.Num.FamilyExistsPos → Cmp.CmpPair → Top.GoodTowerExistsX ∧ Top.VolumeTheoremX
```

### UpperTheory.GalC.linkN_of_boundAtTwoThree_slot

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean:54` · single-target rank outside 40 · all-candidates rank 38.

```lean
theorem linkN_of_boundAtTwoThree_slot (hP : Hypotheses₂) (hG : _root_.UpperTheory.GalC.CutGivesAlt) (Q : GlobalTheory.Mem.Top.V4.Slot) (Lk : GlobalTheory.Fc.LkT _root_.GlobalTheory.Fc.BundleCondition)
    (hE : GlobalTheory.Fc.RowE Q Lk (fun _ D O _ _ => _root_.UpperTheory.GalC.GaloisPreconditions D O.ex.nch ∧ Tie4 D))
    (h23 : _root_.GlobalTheory.Fc.R1.SlotNormCondition Q Lk (fun 𝒞 => Closed 𝒞 fun Fm _ => _root_.GlobalTheory.NLink.BoundAtTwoThreeFamilyFonAlt Fm)) :
    _root_.GlobalTheory.Fc.R1.SlotNormCondition Q Lk (fun 𝒞 => Closed 𝒞 fun Fm _ => Formalism.MainNotions.LinkN Fm)
```

### GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume

**READ / COMPILED** `Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheorem.lean:36` · single-target rank outside 40 · all-candidates rank 36.

```lean
theorem goodTower_and_volume :
    Top.Given → PtsIntegrableStatement → ReciprocityTheory.ChartRestriction.G.AI.I2.AvoidStatement → Out.WeilSt → GlobalTheory.CompanionTheory.Ar.Num.FamilyExistsPos →
      Cmp.CmpPair → Top.GoodTowerExistsX ∧ Top.VolumeTheoremX
```

### UpperTheory.GalC.linkN_of_twGood_galoisPreconditions

**READ / COMPILED** `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean:37` · single-target rank outside 40 · all-candidates rank 39.

```lean
theorem linkN_of_twGood_galoisPreconditions (hP : Hypotheses₂) (hG : _root_.UpperTheory.GalC.CutGivesAlt) {eps : ℝ} (Fm : FamP eps) (hTw : TwGood Fm)
    (hF : ∀ (x : ℝ) (hx : Fm.x1 < x) (i : Fm.Ix x), _root_.UpperTheory.GalC.GaloisPreconditions (Fm.D x i) (Fm.ex x hx i).nch ∧ Tie4 (Fm.D x i)) : LinkN Fm
```

**COMPILED** A second traversal on independently constructed sparse adjacency matrices reproduced the eight reachable sets and their boundary sets, all directory rankings, and the descendant totals of every listed hub. **READ** denotes source inspection and **DERIVED** denotes interpretation. **COMPILED** in this report denotes execution of the analysis programs.
