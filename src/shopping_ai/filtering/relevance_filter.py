from shopping_ai.models.product import Product


class RelevanceFilter:

    def filter_products(
        self,
        products: list[Product]
    ) -> list[Product]:

        filtered = []

        for product in products:

            # --------------------
            # Remove Ads
            # --------------------

            if product.is_ad:

                continue

            # --------------------
            # Remove Kids Products
            # --------------------

            if product.category in [
                "kids",
                "boys",
                "girls"
            ]:

                continue

            filtered.append(
                product
            )

        return filtered