# Black-box map of the RH Lean proof (commit e50d098)

Claude, 2026-11-21. Source: `rh-source/src`. Every one of the 175,187 `.lean` files (17,374,215 lines) is in the import closure of `Main` (also stated in `rh-source/verification/NOTES.md`). So the import closure says nothing about which files the proof actually uses. A usage (term-level) map is Codex task 1.

**Coverage so far:** the handoff cites 251 files, about 0.14% of the files.

## By library

| library | lines | share | files | files cited in handoff |
|---|---:|---:|---:|---:|
| Development | 12,232,663 | 70.4% | 141,928 | 49 |
| Formalism | 3,200,748 | 18.4% | 18,254 | 194 |
| GroundTheory | 1,119,138 | 6.4% | 8,507 | 3 |
| ReciprocityTheory | 563,016 | 3.2% | 3,845 | 4 |
| CompanionTheory | 194,218 | 1.1% | 2,027 | 0 |
| PositivityTheory | 55,130 | 0.3% | 449 | 0 |
| Lemmata | 9,232 | 0.1% | 167 | 0 |

## Largest directories (depth 3), with how many of their files the handoff cites

| directory | lines | files | cited |
|---|---:|---:|---:|
| `Development/AbelianVarietyTheory/Proofs` | 7,436,698 | 95,418 | 3 |
| `Development/AutomorphicSpectrum/Proofs` | 1,163,468 | 14,864 | 3 |
| `Development/AutomorphicArithmetic/AutomorphicVarieties` | 848,614 | 7,959 | 4 |
| `GroundTheory/HeightsAndTheta/Heights` | 626,821 | 6,348 | 1 |
| `Development/AbelianVarietyTheory/Definitions` | 508,569 | 2,198 | 3 |
| `Development/WeilBound/CoreStatements` | 455,457 | 3,746 | 3 |
| `Formalism/HermitianCurvature/HermitianCurvatureProofs` | 437,211 | 1,854 | 0 |
| `Formalism/PeriodIntegrals/UnitaryGroupMassFormula` | 430,489 | 3,615 | 3 |
| `Development/AutomorphicArithmetic/Foundations` | 419,572 | 4,413 | 0 |
| `Formalism/LocalToGlobal/SiegelLatticeTheory` | 339,004 | 2,085 | 1 |
| `Development/WeilBound/RepresentationTheoryGL` | 274,147 | 2,486 | 1 |
| `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry` | 239,112 | 1,623 | 0 |
| `Formalism/SharpRestriction/GrowthBounds` | 231,225 | 1,210 | 22 |
| `Development/AutomorphicArithmetic/ThetaCorrespondence` | 178,983 | 3,201 | 8 |
| `Formalism/SharpRestriction/LevelLetterCocycles` | 170,849 | 758 | 0 |
| `ReciprocityTheory/ReductiveGroups/DiscreteSeries` | 154,332 | 1,021 | 1 |
| `Development/ResolutionOfSingularities/EmbeddedResolution` | 135,525 | 477 | 0 |
| `Formalism/SharpRestriction/CuspSpanNormBounds` | 132,978 | 399 | 3 |
| `Development/AutomorphicArithmetic/IntegralCasts` | 123,617 | 907 | 2 |
| `Development/WeilBound/ThetaLifts` | 115,848 | 788 | 0 |
| `CompanionTheory/SpectralGeometry/LocalGlobalProofs` | 104,890 | 1,250 | 0 |
| `Development/AbelianVarietyTheory/BlockTheory` | 104,027 | 753 | 0 |
| `Formalism/LocalToGlobal/Columns` | 95,905 | 376 | 0 |
| `Formalism/LocalToGlobal/IndefiniteReal` | 78,821 | 435 | 0 |
| `Formalism/LocalToGlobal/TorsionIntegrality` | 70,444 | 489 | 1 |
| `Formalism/LocalToGlobal/GlobalTheory` | 69,295 | 389 | 13 |
| `GroundTheory/PAdicHodge` | 64,317 | 226 | 0 |
| `Formalism/SharpRestriction/Divisibility` | 63,162 | 274 | 2 |
| `GroundTheory/AutomorphicForms` | 61,033 | 217 | 0 |
| `Development/AbelianVarietyTheory/PublishedTheorems` | 56,194 | 493 | 0 |

## Inside the four largest unread boxes (lines per subfolder)

- `Development/AbelianVarietyTheory/Proofs` (7.4M lines):
  - DivisorProofs 2,848,282, the single biggest folder (about 16% of the repo). The √x dial lemma lives here (`FiveElementaryInequalitiesEventually.lean`).
  - InertiaEigenvalues 676,661; IwasawaDecomposition 600,348; TwistedOperators 548,833; FlagMeasures 394,262.
  - DecoratedLatticeProofs 362,431; FoundationProofs 291,980; SatakeParameters 236,891; ModuliProofs 170,603; DegenerationProofs 146,184.
- `Development/AutomorphicSpectrum/Proofs` (1.16M):
  - BlockDecomposition 689,539; GeometryProofs 220,952 (Chowla–Selberg, FlatDegree, Add. 17); MetricProofs 118,136.
  - GlobalProofs 44,921; AlgebraProofs 43,990; DivisibilityProofs 22,281 (GoodTowerVolumeTheorem).
- `Development/AutomorphicArithmetic/AutomorphicVarieties` (849k):
  - ModularityArgument 292,016; LiteratureResults 53,296; PatchingModules 50,353.
  - WeakShimuraTheory 44,963; GaloisLibrary 33,262. This is probably guide §7, Galois representations; LayeredIsomorphisms (`window1`) also sits here.
- `GroundTheory/HeightsAndTheta/Heights` (627k):
  - HilbertSamuel 88,665; ComplexAnalyticSets 74,689; KleimanAmpleness 68,571; HeightKernels 33,510; ArithmeticBezout 27,354.
- Also large and uncited:
  - `Formalism/HermitianCurvature/HermitianCurvatureProofs` (437k; contains the `addDecl` copy command);
  - `Development/AutomorphicArithmetic/Foundations` (420k);
  - `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry` (239k);
  - `Formalism/SharpRestriction/LevelLetterCocycles` (171k);
  - `Development/WeilBound/ThetaLifts` (116k).

## Facts that limit searching (from `verification/NOTES.md`, READ)

- Building takes 7–10 h on 48 cores and 503 GB of RAM. The proof export is 61 GB. So neither we nor Codex can build it or query the compiled environment. Everything is text analysis.
- The source has no comments. It has 818,755 theorems and 242,067 definitions, and many names repeat (≥15 `KudlaFamilyStatement`, many `Conclusion1`, three `structure Loc`). Always resolve by namespace and path.
- `kexactB` (67 files) and `kcopy` assign terms without the elaborator checking their type. Only the kernel checks these. That is sound, but it means the stated type is the only reliable description.
