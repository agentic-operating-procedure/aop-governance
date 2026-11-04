# CR-009: Robustness Hardening Umbrella (Reconciliation of the External Review)

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-05 |
| Owner | Emmanuel A. Otchere |
| Layer | Estate, Model, Architecture, Governance |
| Depends on | CR-002 to CR-008 (all merged) |

## 1. Problem statement

An external comprehensive review (held in the local workspace at `CRs/AOP Robustness Hardening Umbrella Change Request.md`) proposes nine hardening changes toward Demonstrated-level authority. The review states its own evidence limitation: it was written from the organisation profile only, without the founding paper, the conformance clauses, or the landscape documents. Before any change lands, each item is reconciled against the actual published text: some items are already covered, some are partially covered, and the remainder are genuine gaps.

## 2. Reconciliation of the nine items against the published estate

| Review item | Verdict | Evidence |
|---|---|---|
| CR-1 trust-classed facts | **Genuine gap** | NM-CTX-1 requires a source and access rule per context element but no trust class; the guardrail matches variants over the raw case context. The threat model's T4 answer (injected instructions reach the agent, not the guardrail) is overstated: the guardrail consumes the same case context, which in a real deployment can carry model-derived or attacker-influenced values |
| CR-2 compilation ratification gate | **Genuine gap, one partial** | Rule-level status, support floors, critical-variant exemption, confidence propagation and policy-conflict flagging do not exist. Partial: the observation posture already defers to each estate's privacy review (CG-O section 5); the lawful-basis and consultation clauses strengthen it |
| CR-3 cumulative authority | **Genuine gap** | The risk axes include reversibility and operational impact, but there are no aggregate budgets, rate limits, blast-radius caps, per-action reversibility classes or delegation attenuation |
| CR-4 trust base | **Partially covered** | Covered: fail-closed degraded enforcement (SEC-7), safe-state on recovery failure (ARC-R3), hash-chained case record (SEC-8), broker threat (T3). New: signed versioned policy bundles, key custody and external anchoring, separation of duties, named accountable owner, hold semantics, emergency stop, threat entries T6 and T7 |
| CR-5 oversight quality | **Partially covered** | Covered: evidence bundles already carry the baseline comparison (SEC-9, `baseline_comparison` field); ruling latency is already named in the adoption change guidance. New: SLA and timeout behaviour, approver independence, oversight metrics emission, sampled audit, injected test escalations |
| CR-6 loop hygiene | **Genuine gap** | NM-ASR-4 prevents a run from mutating its own bound version, but nothing tags case origin, excludes agent-originated cases from baseline mining, or protects a human reservoir. Once agents execute, ARC-P5 makes their work observation, so the baseline drifts toward agent behaviour |
| CR-7 adequacy conformance | **Partially covered** | Covered: the must-fail fixture discipline (five one-defect documents, all failing), semantic lints (prose thresholds DOC-3, authority coverage DOC-5, escalation-without-target-role in the validator). New: adversarial suite, requirement-to-fixture coverage map, tiered profiles (note: graduated conformance levels are already open reconciliation point 6), dual verifiers, byte-pinning |
| CR-8 earning Demonstrated | **Known open item** | The estate states this itself: the exemplar is steward-run over a synthetic corpus, and the live claim belongs to the adoption pilot. New from the review: a second exemplar in a low-frequency judgment-heavy domain, a third adversarial exemplar, pre-registered metrics, a standing replication invitation, negative-result reporting |
| CR-9 disambiguation and crosswalks | **Partially covered, owner decisions required** | Covered: the standards landscape already maps ISO/IEC 42001, NIST AI RMF, ISO/IEC 23894, W3C PROV, OpenTelemetry and others, with the direction of each mapping stated; the differentiation document covers policy engines with the decision-point/enforcement-point boundary. New: the name collisions (Shoham's agent-oriented programming; the review's cited Decagon and Skan usages) are not addressed anywhere. **Owner decisions**: citing the EU AI Act and OWASP conflicts with D-007 (standards sourcing cites ITU-T M.3050.x, ETSI TS, ISO/IEC and NIST only), so the crosswalk extension needs D-007 amended or the rows need different sourcing; softening the specification-layer claim is a positioning decision the programme owner holds |

## 3. Sequencing

As the review proposes, with the reconciliation applied:

1. **First (this landing)**: CR-009-1 (trust classes), CR-009-2 (ratification gate), CR-009-4 (trust base). These close the integrity and trust-root gaps.
2. **Next**: CR-009-3 (cumulative authority), CR-009-5 (oversight quality), CR-009-6 (loop hygiene).
3. **Then**: CR-009-7 (adequacy conformance), which tests everything above.
4. **In parallel**: CR-009-8 (Demonstrated evidence) and CR-009-9 (disambiguation), the latter gated on the owner decisions in section 2.

## 4. Implementation status at filing

Consistent with the estate's established landing pattern, block 1 items are implemented and gated in the same landing as this CR: `aop-spec` v0.3.0, `aop-toolkit` v0.2.0, `aop-reference-harness` v0.2.0, `aop-conformance` v0.1.1, `aop-architecture` v0.1.1, `aop-context-graph` v0.2.1. Items marked owner decisions were not implemented.

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: this CR and its children; no ratified decision is superseded; D-007 is touched only by CR-009-9's owner-decision flag |
| A5 to A9 | IN SCOPE, no change: the concept, glossary, non-goals and public description are unchanged; CR-009-9's disambiguation additions would extend, not alter, the concept |
| A10 | IN SCOPE, no change: no repository created or retired |
| B1 to B8 | IN SCOPE: NM-CTX-5, NM-STR-16 to NM-STR-19, NM-AUT-7, NM-PRV-6, NM-GOV-1, SEC-14, SEC-15, CC-21 to CC-23 are new normative text; schema extended; validator extended; fixture gates re-run |
| C1 to C7 | IN SCOPE: threat model gains T6 and T7; the trust-base mechanisms are added to the trust architecture; no layer or pipeline change |
| D1 to D5 | IN SCOPE: CG-O9 strengthens the observation posture; the substrate schemas are unchanged in block 1 (origin tagging is CR-009-6) |
| E1 to E6 | IN SCOPE: the compiler stamps ratifications, propagates confidence, flags conflicts and honours support floors and critical exemptions; the linter checks the new clauses |
| F1 to F8 | IN SCOPE: the guardrail decides only over attested and derived facts; hold and emergency-stop semantics added; the case record obligations unchanged |
| G1 to G4 | IN SCOPE, no change: registry mechanics untouched |
| H1 to H4 | IN SCOPE: the harness profile gains the poisoned-fact and emergency-stop checks; the must-fail fixture set grows |
| I1 to I4 | IN SCOPE, no change in block 1; CR-009-6 will touch the baseline method |
| J1 to J4, K1 to K2 | IN SCOPE, no change: the playbook cites the new clauses at its stage 3 and 6 gates |
| L1 to L8 | IN SCOPE: met, same audit method as CR-008 |

## 6. What this CR is not

It is not a repositioning: the specification-layer claim and the standards-sourcing scope are the owner's to change, flagged in CR-009-9. It is not the Demonstrated claim: CR-009-8 organises the evidence work; the claim itself remains open until the non-steward pilot and the independent reproduction exist.
