import re


class QueryParser:

    GENDER_WORDS = {
        "men": "men",
        "man": "men",
        "male": "men",

        "women": "women",
        "woman": "women",
        "female": "women",

        "boys": "boys",
        "boy": "boys",

        "girls": "girls",
        "girl": "girls",

        "kids": "kids",
        "kid": "kids",

        "unisex": "unisex"
    }

    MATERIAL_WORDS = [
        "cotton",
        "linen",
        "polyester",
        "silk",
        "wool",
        "denim"
    ]

    PRODUCT_TYPES = [
        "tshirt",
        "t-shirt",
        "shirt",
        "jeans",
        "kurta",
        "saree",
        "dress",
        "shoes",
        "sneakers",
        "hoodie",
        "jacket"
    ]

    BRANDS = [
        "nike",
        "adidas",
        "puma",
        "hm",
        "h&m",
        "zara",
        "levis",
        "roadster"
    ]

    def parse(
        self,
        query: str
    ) -> dict:

        query = query.lower()

        return {
            "gender": self._extract_gender(query),
            "material": self._extract_material(query),
            "product_type": self._extract_product_type(query),
            "brand": self._extract_brand(query),
            "price_min": self._extract_min_price(query),
            "price_max": self._extract_max_price(query)
        }

    def _extract_gender(
        self,
        query: str
    ):

        for word, value in self.GENDER_WORDS.items():

            if word in query:
                return value

        return "any"

    def _extract_material(
        self,
        query: str
    ):

        for material in self.MATERIAL_WORDS:

            if material in query:
                return material

        return None

    def _extract_product_type(
        self,
        query: str
    ):

        for product_type in self.PRODUCT_TYPES:

            if product_type in query:
                return product_type

        return None

    def _extract_brand(
        self,
        query: str
    ):

        for brand in self.BRANDS:

            if brand in query:
                return brand

        return None

    def _extract_max_price(
        self,
        query: str
    ):

        match = re.search(
            r"under\s+(\d+)",
            query
        )

        if match:

            return int(
                match.group(1)
            )

        return None

    def _extract_min_price(
        self,
        query: str
    ):

        match = re.search(
            r"above\s+(\d+)",
            query
        )

        if match:

            return int(
                match.group(1)
            )

        return None