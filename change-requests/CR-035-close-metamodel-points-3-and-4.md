# CR-035: Close Metamodel Reconciliation Points 3 and 4

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-06 |
| Owner | Emmanuel A. Otchere |
| Layer | Specification (documentation disposition) |
| Depends on | CR-033 (merged), CR-034 (merged) |

## 1. Problem statement

Metamodel reconciliation points 3 (the harness-AOP relationship) and 4 (compiled versus authored provenance) still carry open wording in the mapping document, but both were substantively resolved by later landings: point 3 by SEC-11, the source errata and the hierarchy-metamodel map's composition rule (HM-2); point 4 by the ratification gate (NM-AUT-7, NM-AUT-10, NM-PRV-3) and the errata. The mapping document lags the estate, and the point-4 remainder (whether an authored AOP can conform) now has a determinate answer the document should state.

## 2. Objective

Record the final dispositions for points 3 and 4, leaving the register's E26 to E40 as the sole open item of CR-010.

## 3. Scope

`aop-spec`, the metamodel mapping document only: the two disposition rewrites. No clause, schema, validator or fixture changes; no other repository.

## 4. Acceptance criteria

- Point 3 cites SEC-11, the errata reconciliation and HM-2, and cites the metamodel's Stage 01 decision as consistent.
- Point 4 states the determinate answer: an authored AOP can validate as a document but cannot be operationally authorised, because its rules cannot be ratified without observed provenance on a human-reviewed corpus.
- L1 clean; the specimen gate unaffected.

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 | IN SCOPE: this CR |
| A2 to A10 | IN SCOPE, no change: this is a documentation disposition of already-ratified positions; nothing is newly decided |
| B1 to B8 | IN SCOPE, no change: no clause, schema or validator changes |
| C to K | N/A |
| L1, L4 | IN SCOPE: met |

## 6. What this CR is not

It is not a new decision: both dispositions restate what SEC-11, HM-2, the errata and the ratification gate already establish. It is not CR-010's completion: E26 to E40 remain unpinned pending the owner's Stage 03 and 05 sources.

## 7. Implementation

Implemented in the aop-spec metamodel mapping document.
