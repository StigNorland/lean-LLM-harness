# T-002 — showyourwork paper↔figure binding

```yaml
id: T-002
title: "showyourwork paper↔figure binding"
status: proposed
date: 2026-09-04
owning_issue: ""
pr: ""
serves_commitments:
  - generated-not-transcribed
  - automation-verifies-never-decides
failure_modes:
  - fit-as-prediction
  - status-inflation
validation_evidence: []
notes: >
  Intake example only. Not adopted. Illustrates citation format for an external
  reproducible-article workflow that binds figures to generating scripts.
sources:
  - url: "https://github.com/showyourwork/showyourwork"
    kind: repository
    commit_or_version: ""
    citation: "showyourwork"
taken: |
  If adopted: the practice of declaring which script produces which figure
  (paper↔figure binding) so builds regenerate graphics from declared code
  rather than committing opaque binary outputs alone.
adapted: |
  Would need mapping onto this method's verify≠decide rule and lineage
  admission; not a drop-in of the full showyourwork stack.
rejected_parts: |
  Full Snakemake/LaTeX article template lock-in; Zenodo/Overleaf integrations
  unless separately proposed.
```

## Summary

**Proposed** (not adopted). [showyourwork](https://github.com/showyourwork/showyourwork) ties article figures to the scripts that generate them, supporting reproducible builds. This stub records the citation for possible future intake around **generated-not-transcribed** graphics.

## Why it might matter

Reduces silent replacement of computed figures with hand-edited or post-hoc tuned plots. Any adoption would still require lineage decision and validation evidence—CI binding is verification, not scientific acceptance.
