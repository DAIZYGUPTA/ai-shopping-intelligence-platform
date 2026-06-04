from shopping_ai.intelligence.query_parser import (
    QueryParser
)

parser = QueryParser()

queries = [

    "cotton tshirt",

    "women cotton tshirt under 500",

    "nike running shoes under 3000",

    "boys tshirt",

    "linen shirt above 1000",

    "unisex hoodie"
]

for query in queries:

    result = parser.parse(
        query
    )

    print()
    print("=" * 80)
    print(query)
    print(result)