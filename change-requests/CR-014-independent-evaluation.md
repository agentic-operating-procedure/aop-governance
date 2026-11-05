# CR-014: Independent Out-of-Sample Evaluation; Earning Demonstrated

| Field | Value |
|---|---|
| Estate ID | CR-014 (Review 2, item 5 + CR-009-8, merged) |
| Class | Evidence |
| Priority | P0 |
| Depends on | CR-013 |
| State | In progress (protocol EV-P1..11, cohort module, labelled claims, promotion records landed under CR-031; the prospective live run is the adoption pilot) |

## Problem

The evaluation tier states plainly that the 1.0 agreement result is rule fidelity on the compilation corpus; the exemplar is steward-run over a synthetic corpus and says so. No held-out, prospective or independent evidence exists. This is the highest-value open CR in the set.

## Change

Define the evaluation protocol with separated development, held-out and prospective live cohorts; independent ground truth and adjudicated outcome quality, not only agreement with historical human choices; pre-registered metrics with uncertainty estimates, failure analysis and negative results; a standing replication invitation under the reproducibility protocol; a second exemplar in a low-frequency judgment-heavy domain and a third adversarial exemplar; promotion records identifying version, population, envelope and residual risk.

## Acceptance

- The same cases never serve as both mining input and sole evaluation set.
- At least one independent reproduction is published; negative results reported alongside positive.
- The Wave 6 exit condition (a non-steward pilot) is met or the claim stays steward-run.

## Landing note (2026-11-05)

Landed under CR-031. See the landing CR for the full audit.

## Landing note (2026-11-06)

CR-033 exercised the protocol end to end on the 5G exemplar: deterministic split, development-only compile, held-out shadow evaluation with the correct claim class. Remaining: the prospective live cohort and the independent reproduction.
