from __future__ import annotations

import unittest
from pathlib import Path

from amboras_eval.checks import evaluate_candidate
from amboras_eval.loader import load_candidate
from amboras_eval.models import Decision
from amboras_eval.scenarios import SCENARIOS

ROOT = Path(__file__).resolve().parents[1]


class EvalHarnessTests(unittest.TestCase):
    def evaluate_fixture(self, name: str):
        candidate = load_candidate(ROOT / "scenarios" / name)
        return evaluate_candidate(SCENARIOS[candidate.scenario], candidate)

    def test_complete_fresh_store_can_ship(self) -> None:
        evaluation = self.evaluate_fixture("fresh-store-good.json")
        self.assertEqual(evaluation.decision, Decision.SHIP)
        self.assertEqual(evaluation.score, 100.0)

    def test_risky_black_friday_action_is_blocked(self) -> None:
        evaluation = self.evaluate_fixture("black-friday-risky.json")
        self.assertEqual(evaluation.decision, Decision.BLOCK)
        self.assertIn("margin", {check.key for check in evaluation.blockers})
        self.assertIn("rollback", {check.key for check in evaluation.blockers})

    def test_migration_with_missing_redirects_needs_review(self) -> None:
        evaluation = self.evaluate_fixture("shopify-migration-review.json")
        self.assertEqual(evaluation.decision, Decision.REVIEW)
        self.assertIn("redirects", {check.key for check in evaluation.blockers})


if __name__ == "__main__":
    unittest.main()
