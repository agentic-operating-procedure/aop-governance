# CR-007: Land the Wave 5 Assurance and Evaluation Repositories

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-11-04 |
| Owner | Emmanuel A. Otchere |
| Layer | Assurance, Evaluation |
| Depends on | CR-004, CR-005 |

## 1. Problem statement

The programme's claims are currently asserted by the repositories that built them. The repository map places assurance and evaluation in Wave 5 precisely because conformance and value must be demonstrable, not asserted: the Phase 5 exit gate requires that a harness pass the conformance suite and that a shadow-mode run report agreement against the human baseline. Neither exists yet.

## 2. Objective

Create and seed `aop-conformance` (tier: assurance) and `aop-evaluation` (tier: evaluation) per the repository map, and meet the Phase 5 exit gate on both halves.

## 3. Scope

- `aop-conformance` v0.1.0: profile AOP-DOC-1 (twelve checks: completeness CC-1, decision specificity CC-4 and CC-5, authority coverage CC-7 and CC-8, provenance CC-6 and CC-13, fail-closed CC-18, assurance CC-19 and CC-20) consuming the shared aop-spec validator; profile HAR-1 (seven behavioural checks: fail-closed SEC-5, poisoned-context self-authorisation injection SEC-1 and SEC-2, credential scoping SEC-3 and ARC-C1, approval-gated refusal ARC-C2, evidence bundle completeness SEC-9, case-record tamper detection by chain break SEC-8 and NM-ASR-1, recordable dispositions SEC-6); the must-fail fixture set (five documents, each one defect from the conformant fixture, all failing); the certification process with content-digest certificates; the reference harness and the fixture document certified under AOP-CONF-1.0.0.
- `aop-evaluation` v0.1.0: metric definitions with canonical OpenDEA bindings (three `dea:metric-*` references, five declared gaps per NM-INT-5); baseline extraction (NM-ASR-2); shadow-mode evaluation in observation-only mode with declining-in-substance counting as agreement; the Phase 5 gate reading against the declared 0.85 promotion band; the reproducibility protocol (standard library only, deterministic, version-pinned, machine-diffable reports).

Out of scope: adoption content (Wave 6), the 5G exemplar programme (CR-006), any change to the Wave 2 to 4 repositories.

## 4. Acceptance criteria

- Both repositories are public, with authority-stating READMEs, licence commits, CODEOWNERS, changelog entries, and the local-only doctrine exclusion (ADR-0008).
- The must-fail fixtures all fail; the conformant fixture passes and certifies.
- The harness profile passes against `aop-reference-harness` and certifies (Phase 5 gate, first half).
- The shadow-mode run reports agreement 1.0, within the declared 0.85 promotion band, framed as rule fidelity against the compiled corpus, not live generalisation (Phase 5 gate, second half).
- Metric gaps are declared, not silently missing.
- Published artefacts avoid em dashes, ellipsis glyphs and prohibited vendor references (L1).

## 5. Cascade audit

| # | Outcome |
|---|---|
| A1 to A4 | IN SCOPE: recorded here; no decision, gate or ladder change |
| A5 to A9 | IN SCOPE, no change: concept, glossary, non-goals, positioning and public description unchanged |
| A10 | IN SCOPE: the profile repository list gains the two new repositories when created |
| B1 to B8 | IN SCOPE, no change: the profiles consume the published clauses; the validator is loaded, not modified |
| C1 to C7 | IN SCOPE, no change: HAR-1 tests the published trust mechanisms; no mechanism added or removed |
| D1 to D5 | IN SCOPE, no change: the corpus is consumed; substrate semantics untouched |
| E1 to E6 | IN SCOPE, no change: the toolkit compile chain is exercised, not altered |
| F1 to F8 | IN SCOPE, no change: the harness is assessed, not altered; the assessment output is recorded |
| G1 to G4 | IN SCOPE, no change: certificates reference subjects by content digest; no registry change |
| H1 to H4 | IN SCOPE: this landing satisfies H1 (document profile), H2 (harness profile), H3 (broken fixtures still fail), H4 (certification process) |
| I1 to I4 | IN SCOPE: this landing satisfies I1 (metric definitions), I2 (stale marking rule stated in the protocol), I3 (reproducibility protocol), I4 (shadow-mode comparison) |
| J1 to J4, K1 to K2 | N/A: Wave 6 repositories do not exist; the exemplar programme is CR-006 |
| L1 to L8 | IN SCOPE: met, same audit method as CR-004 |

## 6. What this CR is not

It is not a live-performance claim: the fixture corpus is synthetic and the shadow result is rule fidelity, framed as such in the repository. It is not certification of a deployment: the certificate binds the harness checkout at its content digest. It is not a change to the promoted-artefact process: promotion to bounded execution remains a governance decision recorded in `aop-governance`.

## 7. Implementation

Implemented in the `v0.1.0` landings of `aop-conformance` and `aop-evaluation`. Both gate outputs recorded in the cross-check stage.
