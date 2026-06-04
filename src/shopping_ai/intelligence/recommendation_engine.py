from shopping_ai.models.product import Product


class RecommendationEngine:

    def recommend(
        self,
        products: list[Product],
        limit: int = 20
    ) -> list[Product]:

        return products[:limit]