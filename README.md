# Amboras Agentic Commerce Eval Harness

A small proof-of-work eval framework for Amboras-style AI commerce actions: generated stores, autonomous promo changes, and migrations.

Amboras' public promise is that a merchant can describe their business, get a complete store, and let the store keep improving through AI-run tests and changes. This repo shows one way to gate those actions before they touch checkout, SEO, promotions, or merchant trust.

## Run

Score all included scenarios:

```bash
python3 -m amboras_eval scenarios/*.json
```

Write a markdown report:

```bash
python3 -m amboras_eval scenarios/*.json --report reports/sample-report.md
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

## What It Shows

- Workflow-specific checks for fresh store generation, Black Friday autonomous changes, and Shopify migrations.
- Weighted scoring with `ship`, `review`, and `block` decisions.
- Founder-readable gap explanations instead of a generic pass/fail.
- JSON fixtures that mimic the shape of generated commerce actions.
- Unit tests for the decision boundaries and high-risk promo gate.

## Why This Matters For Amboras

For an AI-native commerce platform, evals are product infrastructure. A generated hero section can be subjective, but checkout wiring, promo margin risk, rollback, redirect coverage, transactional email, analytics, and merchant approval thresholds should be deterministic gates.

This is intentionally small, but the shape is production-friendly: Amboras could run this kind of gate after store generation, migration previews, promo creation, pricing experiments, and A/B-test proposals, then show the score and reasons beside the AI action in the admin.
