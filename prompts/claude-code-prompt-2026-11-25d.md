# Claude Code: two cheap tests from the spec, T5 and T2 (25 Nov 2026)

Written by Claude in chat. The spec is the Claude Doc "Spec: the arithmetic found outside the Lean" (test plan section). Run whenever there is a gap.
Rules: one Lean process at a time; never `lake exe cache get` for the RH project; stop if C: would drop below 25 GB free; ask Timmy before any new download larger than 1 GB.

## T5. Compile the small Lean files in `../rh-extraction`

Files: `Squarefree.lean` (theorem `class_le_trivial`), `ParityEnergy.lean`, `ScalarBridge.lean`. Its README pins its own Mathlib and suggests `lake exe cache get` for a few Mathlib modules. First check whether that Mathlib pin equals the RH closure's (`0df444a…`); if it does, compile each file with `lake env lean` inside the existing pinned closure. If not, stop and report the pin and the download size before fetching anything. Add `#print axioms` for each main theorem.
**Pass:** each compiles; axioms only `propext`, `Classical.choice`, `Quot.sound`. **Fail:** any other axiom, or an error that is not a missing import.
Save outputs next to the files as `<File>.out`.

## T2. Extend the why-p test

Extend `results/gap2-test-bench/why_p.py` (do not change its existing output) to inert primes p = 23, 31, 43, 47 and degrees n up to 600, keeping p = 3, 7, 11, 19 for comparison.
**Pre-registered (write this at the top of the new results file before running):** pass if, for every p, the naive kernel's rate stays within ±2 of n/(p²−1), and for every p ≥ 7 removing the single term L_(p+1) closes at least 80% of the gap to the full rate n·p/(p²−1) at the largest n computed. Fail otherwise, with the p that fails.
Write `results/gap2-test-bench/why_p_extended_results.txt` and add a short dated section to `WHY-P.md` with the result (COMPUTED).

## Last step

Commit and push the new outputs, the `WHY-P.md` edit and this prompt, saying who wrote what. Report pass or fail for T5 and T2.
