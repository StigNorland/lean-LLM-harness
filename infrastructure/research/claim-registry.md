# Claim registry — current entry contract

The claim ledger separates three questions that prose easily collapses:

1. **What kind of assertion is this?** `claim_class` distinguishes declared
   structure, conditional implication, emitted artifact, empirical
   implementation, and physical establishment.
2. **What standing has it earned?** `status` retains the programme vocabulary
   (`candidate`, `conditional`, `derived`, `supported`, and the negative states).
3. **What would defeat it?** `falsifier` and `scope_if_false` make the failure
   boundary part of the claim rather than an afterthought.

Every claim ID introduced after this contract must carry the current fields in
`claim-evidence.schema.json`. The commit guard enforces this only for new IDs;
historical and sealed ledgers remain valid and unchanged.

## Required current fields

| Field | Role |
|---|---|
| `claim_class` | Assertion type, independent of epistemic status |
| `premises` | Named postulates, inputs, derived premises, and open premises |
| `falsifier` | Concrete counterexample, observation, proof, or failed check |
| `scope_if_false` | What fails and what explicitly survives |
| `gate_ids` | Gate ownership; empty only when no programme gate applies |
| `evidence_kinds` | Declaration, proof, replay, certificate, mutation test, observation, or literature |
| `dependency_edges` | Typed premise, consumer, boundary, and non-consumer edges |
| `formal_proof_ids` | Links to formal-proof manifests, never proof by label |
| `verification_ids` | Links to independent replay or mutation evidence |

`claim_class=physical_establishment` is never inferred from a green check,
formal theorem, numerical fit, or another status. It requires the physical
attachment and evidence stated by the claim itself.

A `conditional_implication` may not report `status` `derived` or `supported`
while any named premise has `standing: open`. That combination is an over-read:
the implication is still conditional on the open attachment, and listing `G0`
does not pass G0. Use `status: conditional` and omit the gate, or close the
premise. Historical claims without `claim_class` are not rewritten.

## Boundary

A complete ledger can describe a false theory perfectly. The registry prevents
scope drift and makes criticism local; it does not decide truth.
