def format_search_query(
    query: str
) -> str:

    return (
        query.strip()
        .lower()
        .replace(" ", "-")
    )