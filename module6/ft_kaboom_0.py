
from alchemy.grimoire.light_spellbook import light_spell_record


if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    ingredients = "Earth, wind and fire"
    print(f"Testing record light spell:"
          f" {light_spell_record('Fantasy', ingredients)}")
