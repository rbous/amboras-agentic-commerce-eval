from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Check:
    key: str
    label: str
    weight: int


@dataclass(frozen=True)
class Scenario:
    name: str
    checks: tuple[Check, ...]


@dataclass(frozen=True)
class Candidate:
    scenario: str
    name: str
    passed: set[str]
    warnings: tuple[str, ...] = ()


FRESH_STORE = Scenario(
    name="fresh_store_from_prompt",
    checks=(
        Check("checkout", "checkout wired and testable", 18),
        Check("products", "products have variants, pricing, descriptions, and images", 15),
        Check("trust", "trust signals: reviews, policies, contact, shipping", 12),
        Check("seo", "SEO/GEO basics: titles, meta, schema, crawlable copy", 12),
        Check("analytics", "first-party analytics events are present", 10),
        Check("email", "transactional email sender and templates configured", 9),
        Check("mobile", "mobile hero, PDP, cart, and checkout paths inspected", 9),
        Check("merchant_control", "merchant can edit or reject AI defaults", 8),
        Check("rollback", "rollback path exists before publishing", 7),
    ),
)

BLACK_FRIDAY = Scenario(
    name="autonomous_black_friday_change",
    checks=(
        Check("margin", "discount margin risk checked", 18),
        Check("stacking", "promo stacking rules verified", 14),
        Check("sample_size", "test has holdout and sample-size guard", 14),
        Check("rollback", "rollback plan exists", 13),
        Check("copy", "offer copy is clear and non-misleading", 10),
        Check("inventory", "inventory and fulfillment constraints checked", 10),
        Check("analytics", "conversion and AOV events are tracked", 9),
        Check("approval", "merchant approval threshold is explicit", 7),
        Check("expiration", "promo expiration is scheduled", 5),
    ),
)

MIGRATION = Scenario(
    name="shopify_migration",
    checks=(
        Check("products", "products, variants, pricing, and inventory preserved", 16),
        Check("customers", "customers and marketing consent preserved", 12),
        Check("orders", "order history and refunds preserved", 12),
        Check("redirects", "301 redirect coverage generated", 14),
        Check("seo", "sitemap, schema, and canonical URLs rebuilt", 11),
        Check("reviews", "reviews imported and attached to products", 9),
        Check("email", "transactional email sender verified", 8),
        Check("checkout", "payment methods and checkout tested", 10),
        Check("rollback", "migration rollback plan exists", 8),
    ),
)

SCENARIOS = {s.name: s for s in (FRESH_STORE, BLACK_FRIDAY, MIGRATION)}

CANDIDATES = (
    Candidate(
        scenario="fresh_store_from_prompt",
        name="Ironjaw launch",
        passed={
            "checkout",
            "products",
            "trust",
            "seo",
            "analytics",
            "email",
            "mobile",
            "merchant_control",
        },
    ),
    Candidate(
        scenario="autonomous_black_friday_change",
        name="Aggressive flash-sale agent",
        passed={"stacking", "copy", "inventory", "analytics", "approval", "expiration"},
        warnings=(
            "missing rollback plan",
            "discount margin risk not checked",
            "no holdout or sample-size guard",
        ),
    ),
    Candidate(
        scenario="shopify_migration",
        name="Legacy skincare migration",
        passed={"products", "customers", "orders", "seo", "checkout", "rollback"},
        warnings=(
            "missing 301 redirect coverage",
            "review import not validated",
            "transactional email sender not verified",
        ),
    ),
)


def score_candidate(scenario: Scenario, candidate: Candidate) -> tuple[float, list[str]]:
    total = sum(check.weight for check in scenario.checks)
    earned = sum(check.weight for check in scenario.checks if check.key in candidate.passed)
    missing = [check.label for check in scenario.checks if check.key not in candidate.passed]
    return round((earned / total) * 100, 1), missing


def decision(score: float) -> str:
    if score >= 85:
        return "ship"
    if score >= 60:
        return "review"
    return "block"


def top_gaps(candidate: Candidate, missing: Iterable[str]) -> str:
    gaps = list(candidate.warnings) or list(missing)[:3]
    return "; ".join(gaps) if gaps else "none"


def main() -> None:
    for candidate in CANDIDATES:
        scenario = SCENARIOS[candidate.scenario]
        score, missing = score_candidate(scenario, candidate)
        print(f"Scenario: {scenario.name}")
        print(f"Candidate: {candidate.name}")
        print(f"Score: {score}/100 -> {decision(score)}")
        print(f"Top gaps: {top_gaps(candidate, missing)}")
        print()


if __name__ == "__main__":
    main()
