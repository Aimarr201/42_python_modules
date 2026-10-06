
class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    p1 = Plant("rose", 25, 30)
    p2 = Plant("sunflower", 80, 45)
    p3 = Plant("cactus", 15, 120)
    garden = [p1, p2, p3]

    for plant in garden:
        plant.show()


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
