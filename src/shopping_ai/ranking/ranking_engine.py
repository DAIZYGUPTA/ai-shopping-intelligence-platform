from math import log10

from shopping_ai.models.product import Product


class RankingEngine:

    def calculate_score(
        self,
        product: Product
    ) -> float:

        if (
            product.rating is None
            or
            product.review_count is None
        ):
            return 0.0

        score = (
            product.rating *
            log10(
                product.review_count + 1
            )
        )

        return round(
            score,
            2
        )

    def rank_products(
        self,
        products: list[Product]
    ) -> list[Product]:

        return sorted(
            products,
            key=self.calculate_score,
            reverse=True
        )