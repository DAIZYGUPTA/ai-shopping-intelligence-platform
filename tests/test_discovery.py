
from shopping_ai.filtering.relevance_filter import (
    RelevanceFilter
)

from shopping_ai.discovery.product_discovery import (
    ProductDiscovery
)

from shopping_ai.filtering.product_filter import (
    ProductFilter
)

from shopping_ai.ranking.trust_ranker import (
    TrustRanker
)
from shopping_ai.ranking.value_ranker import (
    ValueRanker
)


# --------------------------------------------------
# Discovery
# --------------------------------------------------

discovery = ProductDiscovery()

products = discovery.search_products(
    query="cotton tshirt",
    max_pages=5
)

print()
print("=" * 80)
print(
    f"Products Found: {len(products)}"
)
print("=" * 80)

for product in products[:20]:

    print(
        product.product_id,
        "|",
        product.brand,
        "|",
        product.is_ad,
        "|",
        product.name
    )

# --------------------------------------------------
# Filtering
# --------------------------------------------------

filter_engine = ProductFilter()

print()
print(
    f"Before Filter : {len(products)}"
)

products = filter_engine.filter_products(
    products
)

print(
    f"After Filter  : {len(products)}"
)

# --------------------------------------------------
# Deduplication
# --------------------------------------------------

products = (
    filter_engine
    .deduplicate_products(
        products
    )
)

print(
    f"After Dedup   : {len(products)}"
)

# --------------------------------------------------
# Show Dedup Results
# --------------------------------------------------

print()
print("AFTER DEDUP PRODUCTS")
print("=" * 80)

for product in products[:20]:

    print(
        product.brand,
        "|",
        product.name
    )

# --------------------------------------------------
# Ranking
# --------------------------------------------------

# ranker = TrustRanker()
ranker = ValueRanker()

ranked_products = (
    ranker.rank_products(
        products
    )
)

print()
print("=" * 80)
#print("TOP PRODUCTS")
print("\nTOP VALUE PRODUCTS")
print("=" * 80)

for product in ranked_products[:20]:

    print()

    print(product.brand)

    print(product.name)

    print(
        f"Rating: {product.rating}"
    )

    print(
        f"Reviews: {product.review_count}"
    )

    #print( f"Trust Score: "  f"{ranker.calculate_score(product)}")
    print(
    f"Value Score: "
    f"{ranker.calculate_score(product)}"
)