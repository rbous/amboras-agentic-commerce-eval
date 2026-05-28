# Amboras Agentic Commerce Eval Harness

Tiny proof-of-work for Amboras: a dependency-free evaluator for AI-generated store launches, migrations, and autonomous commerce actions.

Amboras' public promise is that a merchant can describe their business, get a complete store, and let the store keep improving through AI-run tests and changes. That is powerful, but it also means generated changes need a clear gate before they touch checkout, SEO, promotions, or merchant trust.

## Run

```bash
python3 eval_harness.py
```

## What It Shows

- Scores generated store/action candidates against workflow-specific commerce checks.
- Explains the top gaps in founder-readable language.
- Separates outcomes into `ship`, `review`, and `block` instead of a vague pass/fail.
- Keeps subjective LLM judging out of the critical path for the first version; all checks are deterministic and inspectable.

## How Amboras Could Use This

1. Run the gate after store generation, migration preview, promo creation, and A/B-test proposal.
2. Show the score and failure reasons beside the AI action in the admin.
3. Tune weights with real merchant outcomes as the product learns what reliably improves conversion.
