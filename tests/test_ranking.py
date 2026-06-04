from shopping_ai.discovery.product_discovery import (
    ProductDiscovery
)

from shopping_ai.ranking.ranking_engine import (
    RankingEngine
)


discovery = ProductDiscovery()

products = discovery.search_products(
    "cotton tshirt"
)

engine = RankingEngine()

ranked_products = (
    engine.rank_products(
        products
    )
)

print()

print("=" * 80)
print("TOP PRODUCTS")
print("=" * 80)

for product in ranked_products[:10]:

    score = (
        engine.calculate_score(
            product
        )
    )

    print()

    print(
        f"{product.brand}"
    )

    print(
        f"{product.name}"
    )

    print(
        f"Rating: {product.rating}"
    )

    print(
        f"Reviews: {product.review_count}"
    )

    print(
        f"Trust Score: {score}"
    )