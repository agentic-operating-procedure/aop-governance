# CR-012: Replayable Evidence and Reproducibility Boundaries

| Field | Value |
|---|---|
| Estate ID | CR-012 (Review 2, item 3) |
| Class | Normative + Architecture |
| Priority | P0 |
| Depends on | CR-011 |
| State | In progress (RP-1..7 normative; R1/R2 implemented under CR-028) |

## Problem

Append-only tamper-evident records and replay from the record alone are normative and implemented (hash chain, chain verification). What replay *means* for nondeterministic executors is undefined: reconstructing a decision trail is a different guarantee from re-executing actions, and conflation implies reissuing side effects from a record.

## Change

Define replay levels: record verification, decision-trace reconstruction, and optional controlled re-execution (non-actuating or sandboxed unless separately authorized). Specify the minimum provenance per level (AOP digest, rule versions, snapshot references, executor and tool identifiers, parameters, timestamps, external response identifiers), sensitive-payload minimisation, tamper evidence for ordering, truncation, deletion and export/import, and third-party verification without trusting the producing agent.

## Acceptance

- The replay levels are normative and never imply that reconstruction authorises re-execution.
- A third party verifies a supplied record without trusting the harness or agent that produced it.
- Reconciles with: SEC-8/SEC-10 (chain and replay) and CR-026 (erasure narrows replay claims explicitly).

## Landing note (2026-11-05)

Landed under CR-028: RP-1 to RP-7 normative; the replay module implements R1 and R2 with third-party verification (HAR-12); R3 deliberately unimplemented per RP-2. Remainder: external anchoring exercise, export/import between implementations.
