
class Plant:
    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float) -> None:
        self.name = name.capitalize()
        self.height = height
        self.days_old = age
        self.growth_rate = growth_rate

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")


def ft_garden_data() -> None:
    p1 = Plant("rose", 25.0, 30, 0.8)
    garden = [p1]

    for plant in garden:
        initial_height = plant.height
        plant.show()
        i = 1
        while (i <= 7):
            print(f"=== Day {i} ===")
            plant.grow()
            plant.age()
            plant.show()
            i += 1
        print(f"Growth this week: {plant.height - initial_height:.1f}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_garden_data()
