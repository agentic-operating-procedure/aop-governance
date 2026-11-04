# CR-029: Land Wave H2 of the Comprehensive CR Plan

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-05 |
| Owner | Emmanuel A. Otchere |
| Layer | Normative, Architecture, Substrate, Assurance, Registry, Evaluation |
| Depends on | CR-028 (merged), CR-013, CR-016, CR-017, CR-020, CR-023 |

## 1. Problem statement

The comprehensive CR plan sequences Wave H2 as the integrity wave: observation data governance and loop hygiene (CR-013), approval binding and oversight quality (CR-016), the revocation, rollback and compatibility lifecycle (CR-017), observation plane security (CR-020), and parameter-level constraints (CR-023). Until these land, approvals are unbound objects, parameters are unconstrained at enforcement time, revocation has no registry semantics, agent behaviour can contaminate the baseline, and the observation plane's trust boundary is an assumption rather than a contract.

## 2. Objective

Land Wave H2 across the estate: the normative clauses, the schema surfaces, the harness implementation (approval object, canaries, oversight metrics, parameter validation, revocation hook), the registry revocation state, the evaluation origin filtering, and the substrate and architecture clauses with the new threat entry.

## 3. Scope

- `aop-spec` v0.5.0: RA-15 to RA-19 (the approval object: digest and expiry binding, the four-outcome interface, approver eligibility and independence, re-check at issuance and execution, oversight metrics and canaries); RA-20 to RA-22 (typed parameter schemas, canonical payload validation, fail-closed on tampering); NM-VER-6 (per-scope revocation, active-run behaviour, rollback, compatibility); NM-CTL-6 (origin tagging, the protected human reservoir) and NM-AUT-10 (ratification requires a human-reviewed corpus); schema additions (evidence-bundle action_digest, expiry, approver_outcome; AOP action_schemas and oversight block); validator CC-29 with the fixture parameter-schema-without-bounds.
- `aop-reference-harness` v0.4.0: the approval object in the dispatch (digest, expiry, four outcomes, non-response routing to the fallback, never auto-approve); canary bundles and the failing-approver alert; oversight metrics (approval rate, time-to-approve, canary detection); parameter validation at execution time; the revocation hook with hold on revoked versions.
- `aop-conformance` v0.3.0: HAR-14 to HAR-18.
- `aop-registry` v0.2.0: per-scope revocation as a separate recorded decision; resolve() surfaces the revocation state (NM-VER-6).
- `aop-evaluation` v0.2.0: origin filtering with the protected human reservoir and the corpus quality block (NM-CTL-6, CG-S15).
- `aop-context-graph` v0.3.0: CG-S15 (origin stitched from actor classes), CG-S16 (corpus quality facts), CG-S17 (source identity and integrity metadata), CG-O10 (contestability as a governed finding), CG-O11 (quarantine on provenance failure); the case schema origin field and provenance corpus_quality block.
- `aop-architecture` v0.2.0: ARC-OP1 to ARC-OP4 (the observation plane trust boundary) and threat entry T8.

## 4. Acceptance criteria

- Approvals bind to the action digest and expire; changed payload yields a stale digest (HAR-14); non-response routes to the fallback as a recorded defer and never approves (HAR-15); an approver that approves injected canaries raises the failing-approver alert (HAR-16).
- A revoked version holds at the enforcement point with the reason recorded (HAR-17).
- Parameter tampering, unknown fields and missing required fields fail closed against the declared schema (HAR-18).
- Baseline mining excludes agent-originated cases by default and reports the origin mix.
- The observation plane carries identity, integrity, quarantine and audited-administration clauses with T8's testable mitigations.
- All estate gates pass: the spec gate (13 fixtures), Phase 4 end-to-end, Wave 6 reproduction, both conformance profiles certified (18 harness checks).
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: this landing CR; no ratified decision is superseded |
| A5 to A9 | IN SCOPE, no change: concept, glossary, non-goals, positioning and the public description unchanged |
| A10 | IN SCOPE, no change: no repository created or retired |
| B1 to B8 | IN SCOPE: new normative text (RA-15..22, NM-VER-6, NM-CTL-6, NM-AUT-10, CC-28..30); schema additive; validator extended; gates re-run |
| C1 to C7 | IN SCOPE: ARC-OP clauses and T8; C3's four mechanisms unchanged (oversight quality deepens Oversee) |
| D1 to D5 | IN SCOPE: CG-S15..17 and CG-O10/11 strengthen the substrate; the entity model is unchanged (origin is a case attribute) |
| E1 to E6 | IN SCOPE, no change: the toolchain is untouched in this wave |
| F1 to F8 | IN SCOPE: the runtime gains the approval object, parameter validation and the revocation hook; the guardrail gains parameter verdicts; all existing obligations re-verified |
| G1 to G4 | IN SCOPE: G1 (publication rules extended with revocation state); G2 to G4 unchanged |
| H1 to H4 | IN SCOPE: HAR-14 to HAR-18 added; both profiles certified; the must-fail discipline holds |
| I1 to I4 | IN SCOPE: I4 (shadow comparison) now separates origins by default; the comparator semantics are unchanged |
| J1 to J4, K1 to K2 | IN SCOPE, no change: adoption and examples untouched; the 5G gate re-runs green |
| L1 to L8 | IN SCOPE: met, same audit method as CR-028 |

## 6. What this CR is not

It is not the full CR-020 implementation: the observation plane has no storage implementation to test at, so the clause contract and T8 land and the enforcement tests land with the substrate implementation, tracked in the plan. It is not CR-025 (incident lifecycle) or CR-026 (erasure): they are Wave H3. The 5G corpus does not carry origin tags (its cases pre-date the clause); the evaluation handles undeclared origins explicitly and the corpus upgrade is tracked in the plan.

## 7. Implementation

Implemented in aop-spec v0.5.0, aop-reference-harness v0.4.0, aop-conformance v0.3.0, aop-registry v0.2.0, aop-evaluation v0.2.0, aop-context-graph v0.3.0 and aop-architecture v0.2.0. All gate outputs recorded in the cross-check stage. The CR-009 addendum restoration (banners, decision records, plan file, option-A note) rides this landing.
