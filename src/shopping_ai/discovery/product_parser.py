from bs4 import Tag

from shopping_ai.models.product import Product

from shopping_ai.config.urls import (
    MYNTRA_BASE_URL
)

from shopping_ai.config.selectors import (
    PRODUCT_BRAND,
    PRODUCT_NAME,
    PRODUCT_PRICE,
    PRODUCT_RATING_CONTAINER,
    PRODUCT_REVIEW_COUNT,
    PRODUCT_IMAGE,
    PRODUCT_LINK
)

from shopping_ai.utils.text_utils import (
    extract_price,
    extract_review_count,
    extract_rating
)

from shopping_ai.utils.logger import (
    get_logger
)


logger = get_logger(__name__)


class ProductParser:

    def parse(
        self,
        card: Tag
    ) -> Product:

        product_id = card.get(
            "id",
            ""
        )

        # =================================
        # Advertisement Detection
        # =================================

        is_ad = False

        watermark = card.select_one(
            ".product-waterMark"
        )

        if watermark:

            watermark_text = (
                watermark.get_text(
                    strip=True
                )
                .upper()
            )

            if "AD" in watermark_text:

                is_ad = True

        # =================================
        # Brand
        # =================================

        brand_elem = card.select_one(
            PRODUCT_BRAND
        )

        brand = (
            brand_elem.get_text(
                strip=True
            )
            if brand_elem
            else ""
        )

        # =================================
        # Product Name
        # =================================

        name_elem = card.select_one(
            PRODUCT_NAME
        )

        name = (
            name_elem.get_text(
                strip=True
            )
            if name_elem
            else ""
        )

        # =================================
        # Category Detection
        # =================================

        category = self.detect_category(
            f"{brand} {name}"
        )

        # =================================
        # Price
        # =================================

        price = 0.0

        price_elem = card.select_one(
            PRODUCT_PRICE
        )

        if price_elem:

            try:

                price = extract_price(
                    price_elem.get_text(
                        strip=True
                    )
                )

            except Exception:

                logger.exception(
                    f"Failed parsing price: {name}"
                )

        # =================================
        # Rating
        # =================================

        rating = None

        rating_container = card.select_one(
            PRODUCT_RATING_CONTAINER
        )

        if rating_container:

            try:

                spans = (
                    rating_container
                    .find_all("span")
                )

                if spans:

                    rating = extract_rating(
                        spans[0].get_text(
                            strip=True
                        )
                    )

            except Exception:

                logger.exception(
                    f"Failed parsing rating: {name}"
                )

        # =================================
        # Review Count
        # =================================

        review_count = None

        review_elem = card.select_one(
            PRODUCT_REVIEW_COUNT
        )

        if review_elem:

            try:

                review_count = (
                    extract_review_count(
                        review_elem.get_text(
                            strip=True
                        )
                    )
                )

            except Exception:

                logger.exception(
                    f"Failed parsing reviews: {name}"
                )

        # =================================
        # Image
        # =================================

        image_url = ""

        image_elem = card.select_one(
            PRODUCT_IMAGE
        )

        if image_elem:

            image_url = image_elem.get(
                "src",
                ""
            )

        # =================================
        # Product URL
        # =================================

        product_url = ""

        link_elem = card.select_one(
            PRODUCT_LINK
        )

        if link_elem:

            href = link_elem.get(
                "href",
                ""
            )

            if href:

                product_url = (
                    f"{MYNTRA_BASE_URL}/{href}"
                )

        return Product(
            product_id=product_id,
            brand=brand,
            name=name,
            price=price,
            rating=rating,
            review_count=review_count,
            image_url=image_url,
            product_url=product_url,
            is_ad=is_ad,
            category=category
        )

    def detect_category(
        self,
        text: str
    ) -> str:

        text = text.lower()

        if any(
            word in text
            for word in [
                "women",
                "woman",
                "ladies",
                "female"
            ]
        ):
            return "women"

        if any(
            word in text
            for word in [
                "men",
                "man",
                "male"
            ]
        ):
            return "men"

        if "boys" in text:
            return "boys"

        if "girls" in text:
            return "girls"

        if "kids" in text:
            return "kids"

        if "unisex" in text:
            return "unisex"

        return "unknown"