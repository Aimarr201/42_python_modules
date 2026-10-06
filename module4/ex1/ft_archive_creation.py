
import sys


def text_recovery() -> None:
    argc = len(sys.argv)

    if argc != 2:
        print("Usage: ft_archive_creation.py <file>\n")
        return

    file_content = []

    file_name = sys.argv[1]
    print(f"Accessing file '{file_name}'")

    try:
        file = open(file_name, "r")

        for line in file:
            file_content.append(line)

        print("---\n")

        for line in file_content:
            print(line.rstrip())
        print("\n---")

        file.close()
        print(f"File '{file_name}' closed.\n")

    except Exception as e:
        print(f"Error opening file '{file_name}': {e}\n")
        return

    print("Transform data:\n---\n")

    new_content = []
    for line in file_content:
        temp_line = line.rstrip('\n')
        new_line = f"{temp_line}#"
        new_content.append(new_line)
        print(new_line)
    print("\n---")

    new_name = input("Enter new file name (or empty):")
    if new_name.strip():
        print(f"Saving data to '{new_name}'")
        try:
            new_file = open(new_name, "w")
            final_content = "\n".join(new_content)
            new_file.write(final_content)
            print(f"Data saved in file '{new_name}'.")
        except Exception as e:
            print(f"Error opening file: {e}")
            print("Data not saved.")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    text_recovery()
