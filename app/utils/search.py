from sqlalchemy import func, or_, and_
from unidecode import unidecode


def ilike_search(model, field, keyword):
    return or_(
        func.unaccent(getattr(model, field)).ilike(f"%{(keyword.lower())}%"),
        func.lower(getattr(model, field)).ilike(f"%{unidecode(keyword.lower())}%"),
    )


def combine_conditions(conditions):
    """
    Utility function to combine multiple conditions using AND.
    """
    combined_condition = True
    for condition in conditions:
        combined_condition = and_(combined_condition, condition)
    return combined_condition
