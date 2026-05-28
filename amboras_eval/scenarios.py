from __future__ import annotations

from .models import Check, Scenario


FRESH_STORE = Scenario(
    name="fresh_store_from_prompt",
    checks=(
        Check("checkout", "checkout wired and testable", 18, required_for_ship=True),
        Check("products", "products have variants, pricing, descriptions, and images", 15, required_for_ship=True),
        Check("trust", "trust signals: reviews, policies, contact, shipping", 12),
        Check("seo", "SEO/GEO basics: titles, meta, schema, crawlable copy", 12),
        Check("analytics", "first-party analytics events are present", 10),
        Check("email", "transactional email sender and templates configured", 9),
        Check("mobile", "mobile hero, PDP, cart, and checkout paths inspected", 9),
        Check("merchant_control", "merchant can edit or reject AI defaults", 8, required_for_ship=True),
        Check("rollback", "rollback path exists before publishing", 7, required_for_ship=True),
    ),
)

BLACK_FRIDAY = Scenario(
    name="autonomous_black_friday_change",
    checks=(
        Check("margin", "discount margin risk checked", 18, required_for_ship=True),
        Check("stacking", "promo stacking rules verified", 14, required_for_ship=True),
        Check("sample_size", "test has holdout and sample-size guard", 14, required_for_ship=True),
        Check("rollback", "rollback plan exists", 13, required_for_ship=True),
        Check("copy", "offer copy is clear and non-misleading", 10),
        Check("inventory", "inventory and fulfillment constraints checked", 10),
        Check("analytics", "conversion and AOV events are tracked", 9),
        Check("approval", "merchant approval threshold is explicit", 7, required_for_ship=True),
        Check("expiration", "promo expiration is scheduled", 5),
    ),
)

SHOPIFY_MIGRATION = Scenario(
    name="shopify_migration",
    checks=(
        Check("products", "products, variants, pricing, and inventory preserved", 16, required_for_ship=True),
        Check("customers", "customers and marketing consent preserved", 12),
        Check("orders", "order history and refunds preserved", 12),
        Check("redirects", "301 redirect coverage generated", 14, required_for_ship=True),
        Check("seo", "sitemap, schema, and canonical URLs rebuilt", 11),
        Check("reviews", "reviews imported and attached to products", 9),
        Check("email", "transactional email sender verified", 8, required_for_ship=True),
        Check("checkout", "payment methods and checkout tested", 10, required_for_ship=True),
        Check("rollback", "migration rollback plan exists", 8, required_for_ship=True),
    ),
)

SCENARIOS = {scenario.name: scenario for scenario in (FRESH_STORE, BLACK_FRIDAY, SHOPIFY_MIGRATION)}
