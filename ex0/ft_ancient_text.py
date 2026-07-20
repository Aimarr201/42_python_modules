
import sys


def text_recovery() -> None:
    argc = len(sys.argv)

    if argc != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return
    else:
        file_name = sys.argv[1]
        print(f"Accessing file '{file_name}'")

        try:
            file = open(file_name, "r")
            print("---\n")

            file_content = file.read()
            print(f"{file_content}")
            print("\n---")

            file.close()
            print(f"File '{file_name}' closed.")

        except Exception as e:
            print(f"Error opening file '{file_name}': {e}")
            print("")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    text_recovery()
