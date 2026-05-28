from __future__ import annotations

import argparse
from pathlib import Path

from .checks import evaluate_candidate
from .loader import load_candidate
from .report import render_console, render_markdown
from .scenarios import SCENARIOS


def main() -> None:
    parser = argparse.ArgumentParser(description="Score Amboras-style AI commerce actions.")
    parser.add_argument("scenarios", nargs="+", type=Path, help="Scenario JSON files to score")
    parser.add_argument("--report", type=Path, help="Optional markdown report path")
    args = parser.parse_args()

    evaluations = []
    for path in args.scenarios:
        candidate = load_candidate(path)
        scenario = SCENARIOS[candidate.scenario]
        evaluations.append(evaluate_candidate(scenario, candidate))

    print(render_console(evaluations), end="")

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(render_markdown(evaluations), encoding="utf-8")


if __name__ == "__main__":
    main()
