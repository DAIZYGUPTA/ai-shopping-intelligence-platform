class UserIntentEngine:

    def build_intent(
        self,
        parsed_query: dict
    ) -> dict:

        gender = parsed_query.get(
            "gender",
            "any"
        )

        allowed_categories = []

        excluded_categories = []

        # ------------------------
        # Gender Logic
        # ------------------------

        if gender == "men":

            allowed_categories = [
                "men",
                "unisex"
            ]

            excluded_categories = [
                "women",
                "boys",
                "girls",
                "kids"
            ]

        elif gender == "women":

            allowed_categories = [
                "women",
                "unisex"
            ]

            excluded_categories = [
                "men",
                "boys",
                "girls",
                "kids"
            ]

        elif gender == "boys":

            allowed_categories = [
                "boys"
            ]

        elif gender == "girls":

            allowed_categories = [
                "girls"
            ]

        elif gender == "kids":

            allowed_categories = [
                "kids",
                "boys",
                "girls"
            ]

        else:

            # Query did not specify gender

            allowed_categories = [
                "men",
                "women",
                "unisex"
            ]

            excluded_categories = [
                "boys",
                "girls",
                "kids"
            ]

        return {

            "gender": gender,

            "allowed_categories":
                allowed_categories,

            "excluded_categories":
                excluded_categories,

            "material":
                parsed_query.get(
                    "material"
                ),

            "product_type":
                parsed_query.get(
                    "product_type"
                ),

            "brand":
                parsed_query.get(
                    "brand"
                ),

            "price_min":
                parsed_query.get(
                    "price_min"
                ),

            "price_max":
                parsed_query.get(
                    "price_max"
                )
        }