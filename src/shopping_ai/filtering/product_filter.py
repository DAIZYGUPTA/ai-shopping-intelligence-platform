from shopping_ai.models.product import Product


class ProductFilter:

    BLOCK_WORDS = [

        # Kids

        "kid",
        "kids",
        "boy",
        "boys",
        "girl",
        "girls",
        "baby",
        "infant",
        "toddler",
        "junior",

        # Women

        "women",
        "woman",
        "ladies",
        "female",

        # Loungewear

        "lounge",
        "sleepwear",
        "nightwear",
        "pyjama",
        "pajama",

        # Not T-Shirts

        "tank top",
        "vest",
        "camisole"
    ]

    def filter_products(
        self,
        products: list[Product]
    ) -> list[Product]:

        filtered = []

        for product in products:

            if self._should_remove(
                product
            ):
                continue

            filtered.append(
                product
            )

        return filtered

    def _should_remove(
        self,
        product: Product
    ) -> bool:

        name = (
            product.name.lower()
            if product.name
            else ""
        )

        # -------------------------
        # Remove Ads
        # -------------------------

        if product.is_ad:
            return True

        # -------------------------
        # Remove Irrelevant Products
        # -------------------------

        if any(
            word in name
            for word in self.BLOCK_WORDS
        ):
            return True

        return False

    def deduplicate_products(
        self,
        products: list[Product]
    ) -> list[Product]:

        unique = {}

        for product in products:

            key = (
                product.brand
                .lower()
                .strip(),

                product.name
                .lower()
                .strip()
            )

            existing = unique.get(
                key
            )

            if existing is None:

                unique[key] = product

                continue

            existing_reviews = (
                existing.review_count
                or 0
            )

            current_reviews = (
                product.review_count
                or 0
            )

            if (
                current_reviews >
                existing_reviews
            ):
                unique[key] = product

        return list(
            unique.values()
        )