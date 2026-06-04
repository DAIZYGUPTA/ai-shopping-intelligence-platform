from shopping_ai.models.product import Product


class ProductFeatureExtractor:

    MATERIALS = [

        "cotton",
        "linen",
        "polyester",
        "silk",
        "wool",
        "denim",
        "viscose",
        "rayon"

    ]

    FITS = [

        "oversized",
        "regular",
        "slim",
        "relaxed",
        "loose",
        "skinny"

    ]

    SLEEVES = [

        "full sleeve",
        "half sleeve",
        "short sleeve",
        "long sleeve",
        "sleeveless"

    ]

    NECKS = [

        "round neck",
        "crew neck",
        "v neck",
        "v-neck",
        "polo collar",
        "henley neck"

    ]

    PATTERNS = [

        "printed",
        "graphic",
        "striped",
        "solid",
        "checked",
        "typography",
        "colourblocked",
        "colorblocked"

    ]

    COLORS = [

        "black",
        "white",
        "blue",
        "red",
        "green",
        "yellow",
        "grey",
        "gray",
        "pink",
        "purple",
        "orange",
        "brown",
        "beige",
        "navy"

    ]

    def extract(
        self,
        product: Product
    ) -> dict:

        text = ""

        if product.name:

            text += (
                product.name.lower()
                + " "
            )

        if product.brand:

            text += (
                product.brand.lower()
            )

        return {

            "material":
                self._find_first(
                    text,
                    self.MATERIALS
                ),

            "fit":
                self._find_first(
                    text,
                    self.FITS
                ),

            "sleeve":
                self._find_first(
                    text,
                    self.SLEEVES
                ),

            "neck":
                self._find_first(
                    text,
                    self.NECKS
                ),

            "pattern":
                self._find_first(
                    text,
                    self.PATTERNS
                ),

            "color":
                self._find_first(
                    text,
                    self.COLORS
                )
        }

    def _find_first(
        self,
        text: str,
        candidates: list[str]
    ):

        for candidate in candidates:

            if candidate in text:

                return candidate

        return None