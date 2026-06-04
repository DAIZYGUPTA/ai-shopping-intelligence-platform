from math import log10

from shopping_ai.models.product import Product


class ValueRanker:

    def calculate_score(
        self,
        product: Product
    ) -> float:

        if (
            product.rating is None
            or product.review_count is None
            or product.price is None
            or product.price <= 0
        ):
            return 0.0

        trust_score = (
            product.rating *
            log10(
                product.review_count + 1
            )
        )
        price_penalty = log10(
            product.price + 10
        )

        value_score = (
            trust_score /
            price_penalty
        )

        return round(
            value_score,
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