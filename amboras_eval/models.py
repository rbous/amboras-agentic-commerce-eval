from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class Decision(StrEnum):
    SHIP = "ship"
    REVIEW = "review"
    BLOCK = "block"


@dataclass(frozen=True)
class Check:
    key: str
    label: str
    weight: int
    required_for_ship: bool = False


@dataclass(frozen=True)
class Scenario:
    name: str
    checks: tuple[Check, ...]


@dataclass(frozen=True)
class Candidate:
    scenario: str
    name: str
    passed: frozenset[str]
    warnings: tuple[str, ...]
    metadata: dict[str, Any]


@dataclass(frozen=True)
class Evaluation:
    candidate: Candidate
    scenario: Scenario
    score: float
    decision: Decision
    missing: tuple[Check, ...]
    blockers: tuple[Check, ...]
    warnings: tuple[str, ...]

    @property
    def top_gaps(self) -> tuple[str, ...]:
        if self.warnings:
            return self.warnings[:3]
        return tuple(check.label for check in self.missing[:3])
