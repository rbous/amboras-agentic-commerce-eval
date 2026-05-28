from __future__ import annotations

from .models import Candidate, Decision, Evaluation, Scenario


def evaluate_candidate(scenario: Scenario, candidate: Candidate) -> Evaluation:
    total = sum(check.weight for check in scenario.checks)
    earned = sum(check.weight for check in scenario.checks if check.key in candidate.passed)
    missing = tuple(check for check in scenario.checks if check.key not in candidate.passed)
    blockers = tuple(check for check in missing if check.required_for_ship)
    score = round((earned / total) * 100, 1)

    if score < 60:
        decision = Decision.BLOCK
    elif blockers or score < 85:
        decision = Decision.REVIEW
    else:
        decision = Decision.SHIP

    return Evaluation(
        candidate=candidate,
        scenario=scenario,
        score=score,
        decision=decision,
        missing=missing,
        blockers=blockers,
        warnings=candidate.warnings,
    )
