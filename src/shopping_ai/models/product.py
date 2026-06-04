from dataclasses import dataclass

@dataclass
class Product:

    product_id: str

    brand: str

    name: str

    price: float

    rating: float | None

    review_count: int | None

    image_url: str

    product_url: str

    is_ad: bool = False
    category: str = "unknown"

    trust_score: float | None = None
    value_score: float | None = None

