
def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    return temperature


def test_temperature() -> None:
    temps = ["25", "abc", "100", "-50"]

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
    print("=== Garden Temperature Checker ===")
    print("")
    test_temperature()
