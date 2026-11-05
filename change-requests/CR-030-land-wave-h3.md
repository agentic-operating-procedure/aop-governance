# CR-030: Land Wave H3 of the Comprehensive CR Plan

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-05 |
| Owner | Emmanuel A. Otchere |
| Layer | Normative, Architecture, Security, Assurance, Tooling, Registry |
| Depends on | CR-029 (merged), CR-021, CR-022, CR-024, CR-025, CR-026 |

## 1. Problem statement

The comprehensive CR plan sequences Wave H3 as the security and lifecycle wave: supply-chain attestation (CR-021), workload identity and controlled egress (CR-022), revalidation after component changes (CR-024), incident response and in-flight recovery (CR-025), and erasure-compatible evidence (CR-026). Until these land, digests alone do not establish who built an artefact, workload identity and egress are deployment assumptions rather than normative clauses, component changes can silently invalidate evaluation claims, incident handling is ad hoc, and erasure obligations conflict with the append-only evidence chain.

## 2. Objective

Land Wave H3 across the estate: the normative clauses, the schemas, the compiler and registry enforcement, and the harness implementation (workload identity, component matrix, incident lifecycle, erasure with tombstones, migration markers), with conformance fixtures HAR-19 to HAR-23.

## 3. Scope

- `aop-spec` v0.6.0: NM-VER-7 (build attestation) and NM-VER-8 (the component matrix and impact-classified revalidation gates); SEC-16 (workload identity) and SEC-17 (deny-by-default egress profiles, non-bypassability tested); NM-ASR-7 (erasure-compatible evidence); RA-23 (in-flight migration); SK-12 (skill supply-chain lineage); the build_attestation schema and the skill maintainer and dependencies fields; conformance clauses CC-31 to CC-34.
- `aop-toolkit` v0.3.0: the build attestation emitted by the compiler (compiler version, builder identity, input digests for the SOP, corpus and manifest).
- `aop-registry` v0.2.1: NM-VER-7 enforcement at publication: an artefact claiming operational applicability without an attestation is refused; entries carry the attestation.
- `aop-reference-harness` v0.5.0: workload identity per run with cross-workload credential refusal (SEC-16); the component matrix stamped on every case-record entry (NM-VER-8); the incident lifecycle, declare-respond-recover, with the integrity check and owner-gated resumption (CR-025); payload externalisation to a side store with shredding, appended tombstones, preserved chains and narrowed replay claims (NM-ASR-7); in-flight migration markers (RA-23).
- `aop-conformance` v0.4.0: HAR-19 to HAR-23.
- `aop-architecture` v0.3.0: ARC-IR1/IR2 (the incident lifecycle) and ARC-WS1/WS2 (workload identity and egress).

## 4. Acceptance criteria

- A compiled AOP carries the build attestation; the registry refuses unsigned-effective publication.
- A credential presented by a different workload is refused; the component matrix on every record entry covers the behaviour-affecting components (HAR-19, HAR-20).
- An incident holds the domain; non-owner recovery is refused; owner recovery succeeds on an intact chain and fails on a broken one (HAR-21).
- Erasure shreds the externalised payload, appends the tombstone, preserves the chain, and the record states which replay claims survive and which are withdrawn (HAR-22, RP-5).
- A migration marker is appended and the original entries are byte-identical (HAR-23).
- All estate gates pass; both profiles certify (22 harness checks).
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: this landing CR; no ratified decision is superseded |
| A5 to A9 | IN SCOPE, no change: concept, glossary, non-goals, positioning and the public description unchanged |
| A10 | IN SCOPE, no change: no repository created or retired |
| B1 to B8 | IN SCOPE: new normative text (NM-VER-7/8, SEC-16/17, NM-ASR-7, RA-23, SK-12, CC-31..34); schemas additive; the harness and registry enforce |
| C1 to C7 | IN SCOPE: ARC-IR and ARC-WS clauses; T3's credential-leak answer gains the workload binding; no new threat class |
| D1 to D5 | IN SCOPE, no change: the substrate is untouched in this wave |
| E1 to E6 | IN SCOPE: the compiler emits the build attestation; nothing else in the toolchain changes |
| F1 to F8 | IN SCOPE: the harness gains identity, matrix, incidents, erasure and migration; the loop and enforcement obligations re-verified by the gate |
| G1 to G4 | IN SCOPE: publication gains the attestation gate; resolution surfaces the attestation; provenance chains unchanged |
| H1 to H4 | IN SCOPE: HAR-19 to HAR-23 added; both profiles certified; the must-fail discipline holds |
| I1 to I4 | IN SCOPE, no change: the evaluation tier is untouched in this wave (CR-024's gate registry is the follow-up) |
| J1 to J4, K1 to K2 | IN SCOPE, no change: adoption and examples untouched; the 5G gate re-runs green |
| L1 to L8 | IN SCOPE: met, same audit method as CR-029 |

## 6. What this CR is not

It is not the full CR-024: the impact-classified gate registry and its fixtures are the follow-up, tracked in the plan. It is not a signature infrastructure: NM-VER-7 records digest attestations and names signing as the deployment obligation (ARC-TB2). Egress enforcement tests belong to deployment profiles (SEC-17), not to the reference harness, which makes no network calls.

## 7. Implementation

Implemented in aop-spec v0.6.0, aop-toolkit v0.3.0, aop-registry v0.2.1, aop-reference-harness v0.5.0, aop-conformance v0.4.0 and aop-architecture v0.3.0. All gate outputs recorded in the cross-check stage.
