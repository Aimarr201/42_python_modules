
def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    return temperature


def test_temperature() -> None:
    temps = ["25", "abc"]

    for temp in temps:
        print(f"Input data is '{temp}'")
        try:
            temperature = input_temperature(temp)
            print(f"Temperature is now {temperature}°C")
            print("")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
            print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("")
    test_temperature()
