"""Tests for check_lineage.py and registry consistency."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CHECK = REPO_ROOT / "infrastructure" / "verification" / "check_lineage.py"
REGISTRY = REPO_ROOT / "lineage" / "registry.json"


def test_check_lineage_passes_on_scaffold():
    result = subprocess.run(
        [sys.executable, str(CHECK)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    assert "check_lineage: OK" in result.stdout


def test_registry_lists_expected_seed_ids():
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    ids = {t["id"] for t in data["techniques"]}
    assert "T-001" in ids
    assert "T-002" in ids
    assert "T-003" in ids
    assert "T-004" in ids
    t001 = next(t for t in data["techniques"] if t["id"] == "T-001")
    assert t001["status"] == "originated-here"
    for tid in ("T-002", "T-003", "T-004"):
        entry = next(t for t in data["techniques"] if t["id"] == tid)
        assert entry["status"] == "proposed"


def test_check_lineage_fails_if_method_cites_unknown(tmp_path: Path):
    dest = tmp_path / "lean-LLM-harness"
    shutil.copytree(
        REPO_ROOT,
        dest,
        ignore=shutil.ignore_patterns(
            ".venv", "__pycache__", ".git", "*.pyc", ".pytest_cache"
        ),
    )
    method = dest / "METHOD.md"
    method.write_text(
        method.read_text(encoding="utf-8") + "\n\nSee also T-999.\n",
        encoding="utf-8",
    )
    check = dest / "infrastructure" / "verification" / "check_lineage.py"
    result = subprocess.run(
        [sys.executable, str(check)],
        cwd=dest,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "T-999" in result.stderr
