from __future__ import annotations

from .models import Evaluation


def render_console(evaluations: list[Evaluation]) -> str:
    chunks: list[str] = []
    for evaluation in evaluations:
        chunks.append(f"Scenario: {evaluation.scenario.name}")
        chunks.append(f"Candidate: {evaluation.candidate.name}")
        chunks.append(f"Score: {evaluation.score}/100 -> {evaluation.decision}")
        chunks.append(f"Top gaps: {format_gaps(evaluation)}")
        chunks.append("")
    return "\n".join(chunks).rstrip() + "\n"


def render_markdown(evaluations: list[Evaluation]) -> str:
    lines = ["# Amboras Eval Report", ""]
    for evaluation in evaluations:
        lines.extend(
            [
                f"## {evaluation.candidate.name}",
                "",
                f"- Scenario: `{evaluation.scenario.name}`",
                f"- Score: `{evaluation.score}/100`",
                f"- Decision: `{evaluation.decision}`",
                f"- Top gaps: {format_gaps(evaluation)}",
                "",
            ]
        )
    return "\n".join(lines)


def format_gaps(evaluation: Evaluation) -> str:
    gaps = evaluation.top_gaps
    return "; ".join(gaps) if gaps else "none"
