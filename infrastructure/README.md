# Portable method tooling

Home for governance stubs, contracts, and verification CLIs that programmes can reuse when pinning this method.

| Path | Role |
|------|------|
| [`governance.json`](governance.json) | Minimal policy structure and rationales |
| [`contracts/`](contracts/) | Interface notes for consuming programmes |
| [`verification/`](verification/) | Admission and lineage checkers |

## Verify locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install pytest jsonschema
python infrastructure/verification/admit.py
python infrastructure/verification/check_lineage.py
python -m pytest infrastructure/verification/tests
```

Automation **verifies**; it does not decide scientific acceptance.
