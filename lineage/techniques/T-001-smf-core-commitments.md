# T-001 — SMF core commitments

```yaml
id: T-001
title: "SMF core commitments"
status: originated-here
date: 2026-09-04
owning_issue: ""
pr: ""
serves_commitments:
  - explicit-epistemic-status
  - permanent-negatives
  - ordered-gates
  - prereg-before-decisive
  - automation-verifies-never-decides
  - generated-not-transcribed
failure_modes:
  - status-inflation
  - post-hoc-prereg-edits
  - deleted-negatives
  - analogy-as-derivation
  - fit-as-prediction
validation_evidence:
  - "Commitments restated as METHOD.md §2; sealed in releases/v0.1.0.json"
notes: >
  Seed lineage record. These commitments were developed as programme methodology
  practice and are recorded here as originated-here so consuming programmes can
  cite a stable id without implying external assimilation.
sources:
  - url: "https://github.com/StigNorland/screen-medium-foundations"
    kind: repository
    commit_or_version: "infrastructure/docs/methodology-scope.md"
    citation: "StigNorland/screen-medium-foundations (methodology scope)"
taken: |
  The core epistemic commitments: explicit status labelling; permanence of
  negatives and underdetermination; ordered gates with no downstream rescue;
  preregistration before decisive steps; automation that verifies but does not
  decide; preference for generated over transcribed claim values.
adapted: |
  Lifted from programme-local methodology prose into a portable living paper
  and lineage ledger, without carrying programme-specific science or ontology.
rejected_parts: |
  Domain ontology, physics/SSV gates, and any programme-specific experimental
  content. Those remain in consuming programmes.
```

## Summary

Original research-honesty commitments extracted from Screen Medium Foundations methodology scope documentation and restated as the portable core of this living method. Status is **originated-here**: this is self-lineage for the first sealed surface, not an external borrow.

## Commitments (extracted)

1. **Explicit epistemic status** — claims state what they are (conjecture, assumption, derivation, report, negative, underdetermined).
2. **Permanent negatives / underdetermination** — failures and open underdetermination stay in the record.
3. **Ordered gates; no downstream rescue** — later success cannot repair earlier gate failure.
4. **Prereg before the decisive step** — decision rules fixed before execution, or deviation logged.
5. **Automation verifies, never decides** — CI and scripts check structure; humans accept claims.
6. **Generated, not transcribed, values** — claim numbers come from declared computation unless explicitly marked transcribed.

## Mapping

Serves all six METHOD §2 commitments and directly targets the §1 failure modes listed above.
