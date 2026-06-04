from shopping_ai.discovery.product_discovery import (
    ProductDiscovery
)

from shopping_ai.intelligence.product_feature_extractor import (
    ProductFeatureExtractor
)

discovery = ProductDiscovery()

extractor = ProductFeatureExtractor()

products = discovery.search_products(
    "cotton tshirt",
    max_pages=1
)

print()

print("=" * 80)
print("PRODUCT FEATURES")
print("=" * 80)

for product in products[:20]:

    features = extractor.extract(
        product
    )

    print()
    print(product.name)
    print(features)