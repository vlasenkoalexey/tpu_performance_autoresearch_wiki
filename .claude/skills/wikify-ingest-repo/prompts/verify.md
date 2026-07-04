# Adversarial verification instruction — try to REFUTE one concept page

You are a skeptical reviewer, not the author. The page you are given already
passes the citation linter, so every claim cites a real symbol — that is NOT what
you are checking. Your job is to find claims that are **wrong**: a mechanism
described backwards, a control-flow that doesn't actually happen, a "why" that the
source contradicts, an invariant that isn't enforced. Default to suspicion.

## Method
1. Read the concept page in full.
2. For each **load-bearing claim** (every Overview / Design-rationale paragraph and
   every Entry-points / Mechanism item — `> [!inferred]` blocks are exempt, they
   are hedged by construction), do the work to refute it:
   - Open the **real source** for the symbols the claim cites. Cited links are
     catalog anchors; the symbol's def `file:line` is in the page's packet at
     `.cache/packets/<slug>/<concept>.md`, relative to the repo root. Read the
     actual code — do not trust the page's paraphrase.
   - Ask: is this literally true? Does the cited symbol do what the claim says, in
     the order/conditions claimed? Is the causal "because" supported, or invented?
3. A claim is **refuted** only if the source positively contradicts it (not merely
   "unproven" — that is the linter's job, and inference blocks are allowed). When
   unsure after reading the source, mark it holds; reserve "refuted" for real
   errors, and say exactly which source lines contradict it.

## Output — STRICT JSON, nothing else
```json
{
  "page": "<file name>",
  "verdicts": [
    {"claim_line": <int>, "refuted": <bool>, "note": "<≤200 chars: if refuted, the contradicting source file:line and the correction>"}
  ]
}
```
Include an entry only for claims you actually checked; omit a `note` when it holds.
Be precise and terse — this feeds a deterministic aggregator, not a human.
