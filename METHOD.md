# lean-LLM-harness

**Status:** living paper (canonical prose)  
**Sealed companion:** [`releases/v0.1.0.json`](releases/v0.1.0.json)  
**Lineage index:** [`lineage/registry.json`](lineage/registry.json)

This document is the controlled, traceable methodology for research honesty. It is portable: programmes clone or pin a release and apply the commitments locally. It is not a science paper about any particular domain.

---

## 1. Problem

Even good-faith authors degrade under pressure, habit, and tooling gaps. Recurring failure modes include:

| Failure mode | What goes wrong |
|--------------|-----------------|
| **Status inflation** | Speculative sketches, analogies, or exploratory fits are presented with the force of established results. |
| **Post-hoc prereg edits** | Registration or planned analysis is quietly revised after seeing the decisive outcome. |
| **Deleted negatives** | Failed checks, null results, and underdetermining evidence disappear from the record. |
| **Analogy → derivation** | A useful metaphor is rewritten as if it were a formal derivation. |
| **Fit-as-prediction** | Parameters tuned to the data are sold as independent predictions. |

These are not primarily malice problems. They are **process and incentive** problems. A method that cannot *see* them cannot correct them.

---

## 2. Core commitments

1. **Explicit epistemic status.** Every non-trivial claim carries a stated status (e.g. conjecture, model assumption, derived result, empirical report, negative, underdetermined). Status must be updatable without rewriting history.
2. **Permanent negatives and underdetermination.** Failed tests, excluded alternatives, and genuine underdetermination remain in the record. Deletion is not a resolution.
3. **Ordered gates; no downstream rescue.** Upstream failure is not repaired by later success. Downstream work may *depend on* upstream clearance; it may not *substitute for* it.
4. **Preregistration before the decisive step.** The analysis or decision rule that would settle a claim is fixed before that step is executed, or the deviation is logged as such.
5. **Automation verifies; it never decides.** Scripts and CI check consistency, lineage, and structural admission. Scientific acceptance remains a human (programme) decision.
6. **Generated, not transcribed, values.** Numbers that enter claims are produced by declared computation from declared inputs—not typed from a notebook after the fact—unless explicitly marked as transcribed with provenance.

These commitments originated as programme practice and are recorded as lineage technique **[T-001](lineage/techniques/T-001-smf-core-commitments.md)** (*originated-here*).

---

## 3. Living paper and lineage rule

This file is a **living paper**: it evolves under controlled update ([`docs/update-strategy.md`](docs/update-strategy.md)), not silent rewrite.

**Lineage rule.** Any technique borrowed from another project, paper, or codebase **must** have a record under `lineage/techniques/` and an entry in `lineage/registry.json` *before* it may be marked `adopted` or `adapted` and cited as part of the method. `METHOD.md` cites techniques by stable id (`T-XXX`). **Silent assimilation is forbidden.**

Proposed techniques may be stubbed with status `proposed` to illustrate intake and to support discussion; they are not part of the sealed method until adopted.

---

## 4. What this method cannot do

- It cannot guarantee honesty. It reduces certain classes of process failure and makes others auditable.
- It cannot replace domain expertise, experimental design, or ethics review.
- It cannot decide scientific truth via CI. Admission green means structural and lineage checks passed.
- It cannot absorb programme-specific ontology. Domain content belongs in consuming programmes.
- It cannot cite what was never recorded. Missing lineage is a gap, not a soft suggestion.

---

## 5. How to apply elsewhere (high level)

1. **Pin a sealed release** (see [`docs/consuming-programmes.md`](docs/consuming-programmes.md)).
2. **Map commitments** to local artefacts: status labels, gate order, prereg hooks, negative logs.
3. **Route borrowed tooling** through lineage proposals before adoption.
4. **Keep verify ≠ decide:** local automation checks structure; owners accept claims.
5. **Bump the pin** only when a new sealed method release is intentional.

---

## 6. Lineage appendix (indexed)

This section is **generated / indexed from** [`lineage/registry.json`](lineage/registry.json). Adopted, adapted, and originated-here techniques must appear here by id. Proposed stubs are listed separately for transparency and are **not** part of the sealed method.

### In method (sealed surface)

| Id | Title | Status |
|----|-------|--------|
| **T-001** | SMF core commitments | originated-here |

### Intake examples (not adopted)

| Id | Title | Status |
|----|-------|--------|
| T-002 | showyourwork paper↔figure binding | proposed |
| T-003 | Validation-gated skill evolution | proposed |
| T-004 | Feasibility quarantine | proposed |

Verification (`infrastructure/verification/admit.py`) requires that every `adopted` / `adapted` / `originated-here` technique is registered and that this paper mentions its `T-XXX` id.
