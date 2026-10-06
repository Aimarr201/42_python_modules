
class GardenError(Exception):
    def __init__(self, message: str = "Unknown error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


def test_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water() -> None:
    raise WaterError("Not enough water in the tank!")


def custom_errors() -> None:
    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("")

    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("")

    print("Testing catching all garden errors...")
    try:
        test_plant()
    except PlantError as error:
        print(f"Caught GardenError: {error}")
    try:
        test_water()
    except WaterError as error:
        print(f"Caught GardenError: {error}")
    print("")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    custom_errors()
