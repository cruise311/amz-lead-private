# tests/conftest.py
"""Shared test fixtures for amz-lead-lookup-private."""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure src/ is in path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).parent.parent


@pytest.fixture
def temp_dir(tmp_path) -> Path:
    """Provide a temporary directory."""
    return tmp_path