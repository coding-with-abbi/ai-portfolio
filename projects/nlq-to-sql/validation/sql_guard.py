import sqlparse

def validate_sql(query: str) -> str:
    parsed = sqlparse.parse(query)[0]

    if parsed.get_type() != "SELECT":
        raise ValueError("Only SELECT statements are allowed.")

    if "limit" not in query.lower():
        query += " LIMIT 100"

    return query

