
from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    element_to_find = ingredients.lower()
    if any(element.lower() in element_to_find
            for element in light_spell_allowed_ingredients()):
        result = "VALID"
    else:
        result = "INVALID"
    return f"{ingredients}: {result}"
