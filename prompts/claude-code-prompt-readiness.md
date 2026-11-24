# Claude Code task: make My-RH-proof ready to share

**Repo:** `C:\Users\timmy\OneDrive\Desktop\XPostCode\My-RH-proof`. I'm sharing it on the Lean Zulip and with Michael Rubinstein. It has to be complete, honest and easy to audit. Don't change any claims, and don't touch the `.lean` files.

**Working alongside Codex.** Codex is working in the same repo tonight. It writes `notes/small-primes-check.md`, `notes/period-map-classical.md` and `results/rubinstein-hypotheses/`, and it will not run Lean builds. Always `git pull --rebase` before you push. Don't edit the files Codex owns.

## Checklist

1. **Commit what's pending.** That's `notes/RH-proof-handoff.md` (Addendum 40) and `prompts/codex-prompt-next.md`. Also commit this prompt as `prompts/claude-code-prompt-readiness.md`. Push.

2. **Do a clean reproducibility run.** First check that no `lake` or `lean` process is running. Then run `results/common-period-map/compile-closure.ps1`. It reuses `C:\rhc`, so it should be quick.
   - Expect "ALL PASSED" and the five axiom lines.
   - Before the run, move the old failed `compile-log.txt` to `logs/compile-log-earlier-failed-run.txt`. Keep it for transparency.
   - Commit the new passing `compile-log.txt` and the fresh `.out` files.
   - If the run fails, stop and show me the error. Don't patch around it.

3. **Make the repo public.** Run `gh repo edit Wesleystone88/My-RH-proof --visibility public --accept-visibility-change-consequences` (run `gh auth login` first if needed). Then check that it can be seen without logging in, for example with `curl -s -o NUL -w "%{http_code}" https://github.com/Wesleystone88/My-RH-proof`, which should print 200.

4. **Set the repo description and topics with gh.**
   - Description: "Lean checks on the Alpöge–Claude proof of the Riemann Hypothesis: one map, three sections (Rubinstein H8)."
   - Topics: `lean4`, `riemann-hypothesis`, `formal-verification`, `number-theory`.

5. **Add "Start here" near the top of the README.** Three one-line bullets:
   - a mathematician: read `results/common-period-map/COMMON-PERIOD-MAP.md`, then the paper;
   - a Lean user: run `compile-closure.ps1`, or read `CommonPeriodMap2.lean`;
   - a curious reader: read `paper/` and the investigation log.

   Also add one dated line: "Status as of 23 Nov 2026: both lemmas compiled; classical dictionary open."

6. **Check the links.** Every relative link in README.md, paper/README.md, notes/PATHS.md, data/README.md and prompts/README.md must point to a file that exists. List the external links. Don't fetch them unless you can.

7. **Fill paper/.** I'm exporting the main write-up doc as Markdown into `paper/`. When the file appears:
   - give it a clear name: `paper/alpoge-claude-rh-reading-notes.md`;
   - link it from README.md and paper/README.md;
   - check that it renders on GitHub (tables and code blocks).

   If it isn't there yet, leave paper/README.md saying it's coming, and tell me.

8. **Check the honesty.** Compare the README claims against the outputs. COMPILED must match the `.out` files, COMPUTED must match `gap2_lemniscate_results.txt`, and the scope section must still say "no new mathematics" and "classical dictionary open". Report any mismatch. Don't fix it silently.

9. **Report back** with a pass/fail checklist covering items 1–8, the public URL, and anything I need to do by hand.
