# Change Request Register (CR-001 to CR-042)

One line per change request, with its reconciled landing state. The register is the index; the CR files under `change-requests/` are the record. Estate waves refer to the original programme plan; hardening waves H1 to H5 refer to the comprehensive CR plan.

| CR | Title | Wave | State |
|---|---|---|---|
| CR-001 | Seed the Wave 1 governance surface | Estate 1 | Implemented |
| CR-002 | Land the Wave 2 specification and architecture repositories | Estate 2 | Implemented |
| CR-003 | Land the Wave 3 substrate repository | Estate 3 | Implemented |
| CR-004 | Land the Wave 4 tooling, runtime and registry repositories | Estate 4 | Implemented |
| CR-005 | Align the estate with the OpenDEA process and metrics catalogs | Alignment | Implemented |
| CR-006 | Commit the telecom 5G anomaly management exemplar programme | Estate 6 | Implemented (CR-008) |
| CR-007 | Land the Wave 5 assurance and evaluation repositories | Estate 5 | Implemented |
| CR-008 | Land the Wave 6 adoption and exemplar repositories | Estate 6 | Implemented |
| CR-009 | Robustness hardening umbrella (external review 1) | Hardening | Implemented (children below) |
| CR-009-1/2/4/9 | Trust classes; ratification gate; trust base; disambiguation | H1 (early) | Implemented |
| CR-009-3 | Cumulative authority, budgets, delegation | H1 | Implemented (CR-028) |
| CR-009-5/6/7/8 | Merged into CR-016/013/015/014 | (none) | Merged |
| CR-010 | Close the metamodel reconciliation | H1/H2 | In progress (E26 to E40 pending sources) |
| CR-011 | Runtime action, retry, concurrency, recovery semantics | H1 | Implemented (CR-028) |
| CR-012 | Replayable evidence and reproducibility boundaries | H1 | Implemented (CR-028) |
| CR-013 | Observation governance and loop hygiene | H2 | Implemented (CR-029) |
| CR-014 | Independent out-of-sample evaluation | H4 | Protocol + held-out exercise landed; prospective cohort is the pilot's |
| CR-015 | Conformance expansion: adversarial, interoperability, tiers | H4 | Implemented (CR-031); two independent verifiers remain open |
| CR-016 | Approval binding and oversight quality | H2 | Implemented (CR-029) |
| CR-017 | Publication, revocation, rollback, compatibility | H2 | Implemented (CR-029) |
| CR-018 | Independent governance and claims discipline | H5 | Layer landed; running it on real reviews is the maturity step |
| CR-019 | Risk-tiered adoption and promotion gates | H5 | Gates landed; per-family thresholds land with pilots |
| CR-020 | Observation plane and Context Graph security | H2 | Clauses + T8 landed; enforcement tests await the substrate implementation |
| CR-021 | Supply-chain attestation | H3 | Implemented (CR-030); signing remains a deployment obligation |
| CR-022 | Workload identity and controlled egress | H3 | Clauses landed; egress tests belong to deployment profiles |
| CR-023 | Parameter-level action constraints | H2 | Implemented (CR-029) |
| CR-024 | Revalidation after component changes | H3 | Matrix landed; the gate registry and fixtures remain |
| CR-025 | Incident response and in-flight recovery | H3 | Implemented (CR-030) |
| CR-026 | Erasure-compatible evidence | H3 | Implemented (CR-030); backup propagation remains |
| CR-027 | Optional Pi harness adapter | H5 | Experimental adapter + self-test landed; live integration remains |
| CR-028 | Land Wave H1 | H1 | Implemented |
| CR-029 | Land Wave H2 | H2 | Implemented |
| CR-030 | Land Wave H3 | H3 | Implemented |
| CR-031 | Land Wave H4 | H4 | Implemented |
| CR-032 | Land Wave H5 | H5 | Implemented |
| CR-033 | Held-out cohort run; metamodel map | Closure | Implemented |
| CR-034 | Governance reconciliation | Governance | Implemented |
| CR-035 | Close metamodel reconciliation points 3 and 4 | Specification | Proposed; point 4 resolved, point 3 incomplete |
| CR-036 | Origin tagging and reservoir demonstration | Demonstration / Evaluation | Implemented in aop-examples v0.4.0 |
| CR-037 | Gap-to-reference swap for published metric records | Demonstration | Implemented in aop-examples v0.4.0 |
| CR-038 | Recognise Zero-TAF as the trust framework whose runtime realisation AOP profiles | Alignment | Implemented |
| CR-039 | Repair the estate's version records and guard them in CI | Governance tooling | Proposed; partial implementation, CI acceptance not met |
| CR-040 | Site repository and changelog verification tooling | Governance tooling | Proposed; retrospective reconstruction, original provenance unknown |
| CR-041 | Restore fault-management fixture integrity and execution-policy consistency | Model | Proposed |
| CR-042 | Reconcile governance state and restore estate integrity controls | Governance | Proposed |

## Register reconciliation note

CR-034, CR-036, CR-037 and CR-038 are marked Implemented because their implementation artefacts and acceptance records are present; the supporting evidence and limits are recorded in [FND-002](../findings/FND-002-cr-lifecycle-and-provenance-reconciliation.md). CR-035 remains Proposed because point 3 is not fully dispositioned in the current aop-spec mapping. CR-039 remains Proposed because the verifier's estate-wide acceptance criterion is not met: twelve latest runs failed, and the shared verifier dependency is fetched from mutable site `main`. CR-040 is a retrospective reconstruction, not recovery of the original CR; original author, date, approval and original scope remain unknown. CR-041 remains Proposed. CR-042 remains Proposed and governs the wider estate-integrity remediation. This register records evidence-backed dispositions; it does not convert unverified historical claims into approvals.
