import re


def extract_price(price_text: str) -> float:

    numbers = re.sub(
        r"[^\d]",
        "",
        price_text
    )

    return float(numbers)


def extract_rating(
    rating_text: str
) -> float:

    return float(
        rating_text
    )


def extract_review_count(
    text: str
) -> int:

    text = text.lower().replace("|", "").strip()

    if "k" in text:

        return int(
            float(
                text.replace(
                    "k",
                    ""
                )
            ) * 1000
        )

    numbers = re.sub(
        r"[^\d]",
        "",
        text
    )

    return int(numbers)