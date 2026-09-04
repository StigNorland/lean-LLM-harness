"""Tests for admit.py against the scaffold and induced failures."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
ADMIT = REPO_ROOT / "infrastructure" / "verification" / "admit.py"
REGISTRY = REPO_ROOT / "lineage" / "registry.json"


def run_admit(*args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(ADMIT), *args],
        cwd=cwd or REPO_ROOT,
        capture_output=True,
        text=True,
    )


def test_admit_passes_on_scaffold():
    result = run_admit()
    assert result.returncode == 0, result.stderr
    assert "admit: OK" in result.stdout


def test_admit_fails_when_registry_entry_removed(tmp_path: Path):
    # Copy minimal tree pieces admit needs
    dest = tmp_path / "lean-LLM-harness"
    shutil.copytree(
        REPO_ROOT,
        dest,
        ignore=shutil.ignore_patterns(
            ".venv", "__pycache__", ".git", "*.pyc", ".pytest_cache"
        ),
    )
    reg_path = dest / "lineage" / "registry.json"
    data = json.loads(reg_path.read_text(encoding="utf-8"))
    # Remove T-001 (in-method) so METHOD citation / registry consistency breaks
    data["techniques"] = [t for t in data["techniques"] if t["id"] != "T-001"]
    reg_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    admit_script = dest / "infrastructure" / "verification" / "admit.py"
    result = subprocess.run(
        [sys.executable, str(admit_script)],
        cwd=dest,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0, result.stdout
    assert "ERROR" in result.stderr


def test_admit_fails_when_required_field_broken(tmp_path: Path):
    dest = tmp_path / "lean-LLM-harness"
    shutil.copytree(
        REPO_ROOT,
        dest,
        ignore=shutil.ignore_patterns(
            ".venv", "__pycache__", ".git", "*.pyc", ".pytest_cache"
        ),
    )
    tech = dest / "lineage" / "techniques" / "T-001-smf-core-commitments.md"
    text = tech.read_text(encoding="utf-8")
    # Break required field: remove status line from yaml fence
    broken = text.replace("status: originated-here\n", "")
    tech.write_text(broken, encoding="utf-8")

    admit_script = dest / "infrastructure" / "verification" / "admit.py"
    result = subprocess.run(
        [sys.executable, str(admit_script)],
        cwd=dest,
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0, result.stdout
    assert "status" in result.stderr.lower() or "ERROR" in result.stderr


def test_admit_pr_diff_no_lineage_skips_deep_checks(tmp_path: Path):
    diff_file = tmp_path / "changed.txt"
    diff_file.write_text("README.md\nCHANGELOG.md\n", encoding="utf-8")
    result = run_admit("--pr-diff", str(diff_file))
    assert result.returncode == 0, result.stderr
