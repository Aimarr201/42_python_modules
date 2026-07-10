
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days_old = age

    def show(self) -> None:
        print(f"Created: {self.name}: {self.height:.1f}cm, "
              f"{self.days_old} days old")


def ft_plant_factory() -> None:
    p1 = Plant("rose", 25, 30)
    p2 = Plant("sunflower", 80, 45)
    p3 = Plant("cactus", 15, 120)
    p4 = Plant("tulip", 45, 60)
    p5 = Plant("daisy", 50, 50)
    p6 = Plant("fern", 15, 120)
    garden = [p1, p2, p3, p4, p5, p6]

    for plant in garden:
        plant.show()


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
