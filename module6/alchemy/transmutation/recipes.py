
from ..elements import create_air
from alchemy import potions
import elements


def lead_to_gold():
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
            f" and '{potions.strength_potion()}'"
            f" mixed with '{elements.create_fire()}'")
