# CR-013: Observation Data Governance and Loop Hygiene

| Field | Value |
|---|---|
| Estate ID | CR-013 (Review 2, item 4 + CR-009-6, merged) |
| Class | Normative + Architecture |
| Priority | P1 |
| Depends on | CR-010 |
| State | In progress (origin tagging, reservoir, corpus quality, contestability, quarantine clauses + evaluation filtering landed under CR-029) |

## Problem

The observation posture (declared surface, minimisation, retention, CG-O1 to O9), the governance-manifest boundary, and the ratification gate (only ratified rules grant authority) exist. The remaining risk: real corpora can be incomplete, skewed, or dominated by unsafe workarounds; frequency plus provenance does not establish that behaviour is safe, representative or desirable; and once agents execute, ARC-P5 feeds their behaviour back into the corpus they are measured against.

## Change

Merge the CR-009-6 loop-hygiene obligations with the corpus-quality remainder: origin tagging (human, agent, mixed) on every case; agent-originated cases excluded from baseline mining by default with a protected human reservoir for drift; the context graph records sampling method, inclusion and exclusion, missingness, cohort and coverage gaps; provenance reports counts and uncertainty, not only frequencies; a documented contestability process for derived rules and data use; capture and retention controls demonstrably operating as specified.

## Acceptance

- Drift detection runs against the reservoir; a recompile cannot ratify itself (extends NM-AUT-7: ratification is a human act on a human-reviewed corpus).
- Low-support and low-confidence rules are flagged and cannot silently gain autonomy (landed; verified here end to end).
- A team can reproduce why a case was excluded from a corpus.
- Vocabulary reconciliation: the landed observed/reviewed/ratified statuses stand; this CR maps, not renames.

## Landing note (2026-11-05)

origin tagging, reservoir, corpus quality, contestability, quarantine clauses + evaluation filtering landed under CR-029. See CR-029 for the full audit.
