# Agent rules — lean-LLM-harness

Hard constraints for humans and automated agents contributing to this repository.

## Never

1. **Adopt without lineage.** No technique enters `adopted` / `adapted` status without a `lineage/techniques/T-XXX-*.md` record and a matching `registry.json` entry.
2. **Invent citations.** Every `sources[]` URL, commit, or bibliographic key must be real and checkable. If you cannot verify a source, leave status `proposed` and say so in `notes`.
3. **Let verify become decide.** Scripts, CI, and schemas check structure and consistency. They do not accept or reject scientific claims. Humans (or programme owners) decide.
4. **Silent assimilation.** Do not paste ideas from other projects into `METHOD.md` or tooling without a lineage id and a citation in the living paper.
5. **Programme science here.** No domain ontology, physics gates, or programme-specific results belong in this repo.
6. **Secrets.** No tokens, credentials, or private keys in any file.

## Always

1. Open or link an issue for technique proposals (`technique-proposal` template).
2. Keep `registry.json` consistent with technique files; run `admit.py` locally before opening a PR.
3. Ensure PRs that add or change features leave **admission CI green**.
4. When METHOD cites a technique, use the stable id (`T-001`, …) so verification can grep it.
5. Prefer sealing a `releases/vX.Y.Z.json` over asking programmes to pin an arbitrary commit.

## Admission checklist (PR)

- [ ] Lineage id present (or N/A with rationale for docs-only changes)
- [ ] Source citation for any borrowed technique
- [ ] Tests updated / `admit.py` passes
- [ ] Status transitions justified (`proposed` → `adopted` only after validation evidence)
