# CR-009-2: The Compilation Ratification Gate (Normative Spec and Toolkit)

Parent: CR-009. Review item: CR-2. Reconciliation: genuine gap, observation-annex partial. Class: normative + implementation.

## Problem

Mining observed work makes frequency look like correctness and encodes workarounds with clean provenance. A rule compiled from observation grants authority with no human act in between.

## Change (landed in block 1)

- NM-AUT-7: a decision rule carries a status, observed, reviewed or ratified. Only ratified rules grant authority (autonomous or approval-required). Prohibited rules need no ratification.
- The governance manifest ratifies rules by condition; the compiler stamps status and records what was ratified.
- NM-STR-18: a declared minimum support floor; variants and rules below it are flagged and cannot be ratified. NM-STR-19: declared rare-but-critical variants are exempt from frequency pruning, not from ratification.
- NM-PRV-6: stitching confidence propagates from cases to variant provenance; rules derived below the declared confidence floor cannot exceed reviewed.
- Policy-conflict flagging: where the SOP's claimed authority differs from the manifest's, the conflict is recorded at compile time.
- Observation annex: CG-O9 requires a declared lawful basis and completed consultation before capture begins (strengthening the existing posture).
- Acceptance: the linter rejects an AOP granting authority from an unratified rule (must-fail fixture unratified-authority); a below-support variant is flagged (must-fail fixture variant-below-support).
