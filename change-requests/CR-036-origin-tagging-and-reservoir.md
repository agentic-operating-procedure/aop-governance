# CR-036: Origin Tagging and the Reservoir Demonstration

| Field | Value |
|---|---|
| Status | Implemented |
| Date | 2026-11-06 |
| Owner | Emmanuel A. Otchere |
| Layer | Demonstration, Evaluation |
| Depends on | CR-029 (flagged remainder), CR-033 (merged) |

## 1. Problem statement

CR-029's audit flagged that the 5G exemplar corpus predates origin tagging: the evaluation tier handles undeclared origins explicitly, but the exemplar did not exercise CG-S15, and the loop-hygiene machinery (exclusion of agent-originated cases, the protected human reservoir) had never been demonstrated on the exemplar corpus.

## 2. Objective

Tag the exemplar corpus with case origin, demonstrate the exclusion and reservoir machinery on a post-deployment corpus, and re-run the held-out exercise unchanged on the tagged corpus.

## 3. Scope

`aop-examples` only: the corpus generator emits origin (the exemplar models the human-operated era: all cases human-origin) and an `--agent-fraction` flag for post-deployment corpora; the mixed-origin corpus demonstrating the exclusion is published; the held-out exercise is re-run unchanged on the tagged corpus (`AP-RAN-014@v0.2.1`, identical split, agreement 1.0, zero violations, claim class generalisation); the walkthrough gains section 6b.

## 4. Acceptance criteria

- Every case in the exemplar corpus carries origin; the published baseline is unchanged by construction (all human-origin).
- The exclusion is demonstrated: on a 30 percent agent-origin corpus, the baseline is computed from the human-origin set only (13 excluded), reported in the corpus-quality block.
- The held-out result is reproduced on the tagged corpus.
- The Wave 6 reproduction gate passes; L1 clean.

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this CR |
| A2 to A10 | IN SCOPE, no change |
| D1 | IN SCOPE: the corpus gains the origin attribute per CG-S15; the entity model is unchanged |
| I4 | IN SCOPE: the shadow comparison consumes origins; the comparator semantics are unchanged |
| K1, K2 | IN SCOPE: the walkthrough is extended; the reproduction gate re-runs green |
| B to C, E to J | N/A or no change |
| L1, L4, L7, L8 | IN SCOPE: met |

## 6. What this CR is not

It is not a live mixed-origin corpus: the agent-fraction corpus is synthetic, demonstrating the machinery. It is not a baseline change: the published baseline values are unchanged.

## 7. Implementation and evidence

Implemented in `aop-examples v0.4.0`, not v0.3.1. The v0.4.0 changelog groups the origin-tagging work under CR-036 alongside the CR-037 metric-reference work. The current generator emits the `origin` field and `--agent-fraction` option; the repository contains the published mixed-origin corpus and held-out corpus artefacts. [Governance PR #19](https://github.com/agentic-operating-procedure/aop-governance/pull/19) reports the 13-case exclusion and a passing Wave 6 gate. The current changelog records the held-out result and gate outcome.

The implementation evidence is repository-backed. The historical gate output was not independently re-executed during this reconciliation; the result is retained as a recorded implementation claim, not represented as a fresh test run.
