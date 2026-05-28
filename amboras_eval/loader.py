from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import Candidate


def load_candidate(path: Path) -> Candidate:
    raw: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return Candidate(
        scenario=raw["scenario"],
        name=raw["name"],
        passed=frozenset(raw.get("passed_checks", [])),
        warnings=tuple(raw.get("warnings", [])),
        metadata=raw.get("metadata", {}),
    )
