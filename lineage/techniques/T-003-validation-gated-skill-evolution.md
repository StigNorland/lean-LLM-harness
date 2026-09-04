# T-003 — Validation-gated skill evolution

```yaml
id: T-003
title: "Validation-gated skill evolution"
status: proposed
date: 2026-09-04
owning_issue: ""
pr: ""
serves_commitments:
  - ordered-gates
  - automation-verifies-never-decides
  - prereg-before-decisive
failure_modes:
  - post-hoc-prereg-edits
  - status-inflation
validation_evidence: []
notes: >
  Intake example only. Not adopted. Illustrates citation format for externally
  sourced validation-gated evolution of agent skills / procedures.
sources:
  - url: "https://github.com/microsoft/SkillOpt"
    kind: repository
    commit_or_version: ""
    citation: "SkillOpt"
taken: |
  If adopted: the idea that skill or procedure updates advance only when they
  pass declared validation gates—evolution is gated, not free-form.
adapted: |
  Would be reframed for methodology/technique admission (lineage + tests),
  not for proprietary skill-optimization product semantics.
rejected_parts: |
  Any automated “decision” that promotes a technique to adopted without human
  programme ownership; opaque reward hacks; silent prompt mutation.
```

## Summary

**Proposed** (not adopted). [SkillOpt](https://github.com/microsoft/SkillOpt) explores validation-gated evolution of skills. This stub cites the source as a possible inspiration for **ordered, validation-gated** technique intake—never as a license for automation to decide scientific status.

## Why it might matter

Aligns with ordered gates and verify≠decide: candidates advance only after declared checks. Adoption would require an explicit mapping to this repo’s admission proposal schema and human decision step.
