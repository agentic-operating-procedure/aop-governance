# CR-009-3: Cumulative Authority, Budgets and Delegation Attenuation (Normative Spec and Harness)

Parent: CR-009. Review item: CR-3. Reconciliation: genuine gap. Class: normative + implementation. Status: In progress (NM-CRD-4, NM-AUT-8/9 normative; budgets + irreversibility enforced under CR-028).

## Problem

Per-decision rights miss the sum of many individually permitted actions, and multi-agent estates compound it.

## Change (planned)

- Aggregate budgets, rate limits and a blast-radius cap per action class, declared in the Coordination dimension (NM-CRD-4) and enforced at the guardrail beside the authority check.
- Per-action reversibility classification: reversible, compensable, irreversible. Irreversible requires approval or dual control; compensable declares its compensation path (NM-AUT-8).
- Delegation attenuation: delegated authority narrows along any delegation chain (NM-AUT-9).
- Acceptance: fixtures where each action is individually permitted but the cumulative total breaches a cap are all blocked.

## Landing note (2026-11-05)

Landed under CR-028: NM-CRD-4, NM-AUT-8, NM-AUT-9 normative; the harness enforces budgets beside the authority check (HAR-13) and raises irreversible autonomous verdicts to approval. Remainder: rate-limit windows at run time, blast-radius enforcement tests, delegation-chain attenuation tests.
