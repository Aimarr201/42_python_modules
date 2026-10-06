
from alchemy.grimoire.dark_spellbook import dark_spell_record


if __name__ == "__main__":
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    ingredients = "Cats, rats, tails and snake"
    print(f"Testing record light spell:"
          f" {dark_spell_record('Fantasy', ingredients)}")
