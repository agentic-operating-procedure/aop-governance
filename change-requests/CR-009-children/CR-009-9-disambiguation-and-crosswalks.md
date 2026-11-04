# CR-009-9: Disambiguation and Crosswalks (Landscape; Owner Decisions Required)

Parent: CR-009. Review item: CR-9. Reconciliation: partially covered. Class: landscape. Status: Proposed, gated on owner decisions.

## Already covered (reconciled)

The standards landscape maps ISO/IEC 42001, NIST AI RMF, ISO/IEC 23894, W3C PROV and OpenTelemetry with the mapping direction stated; the differentiation document already draws the policy-engine boundary at the decision point and enforcement point.

## Owner decisions required before implementation

1. **Standards sourcing scope.** Crosswalk rows to the EU AI Act and OWASP conflict with D-007 (sourcing cites ITU-T M.3050.x, ETSI TS, ISO/IEC and NIST only). Either D-007 is amended by a superseding ADR, or the crosswalk cites these through the ISO/IEC and NIST material already in scope. Not decided here.
2. **Name-collision disambiguation** (Shoham's agent-oriented programming; the review's cited Decagon and Skan usages) is safe to add as prior-art rows without touching D-007; this part can proceed on the owner's approval of this CR.
3. **Softening the specification-layer claim** is a positioning decision the programme owner holds. Not decided here.
