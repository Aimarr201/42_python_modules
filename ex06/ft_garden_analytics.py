
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age
        self.stats = self._create_stats()

    def _create_stats(self) -> "Plant.Stats":
        return Plant.Stats()

    @staticmethod
    def is_older_than_a_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(anonymous_plant) -> "Plant":
        return anonymous_plant("Unknown plant", 0, 0)

    def grow_plant(self, growth_height: float) -> None:
        self.height = self.height + growth_height
        self.stats._grow_count += 1

    def age_plant(self, growth_days: int) -> None:
        self.age = self.age + growth_days
        self.stats._age_count += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.age} days old")
        self.stats._show_count += 1

    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, "
                  f"{self._show_count} show")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def grow_plant(self, growth_height: float) -> None:
        super().grow_plant(growth_height)

    def bloom(self) -> None:
        print(f"[asking the {self.name.lower()} to bloom]")
        self.blooming = True
        self.show()

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.stats: Tree.Stats = Tree.Stats()

    def _create_stats(self) -> "Tree.Stats":
        return Tree.Stats()

    def produce_shade(self) -> None:
        print(f"[asking the {self.name.lower()} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {(self.height):.1f}"
              f"cm long and {self.trunk_diameter:.1f}cm wide.")
        self.stats._shade_count += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter:.1f}cm")

    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def grow_seed(self, new_seeds: int) -> None:
        self.seeds = self.seeds + new_seeds
        self.blooming = True
        print(f"[make {self.name.lower()} grow, age and bloom]")

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def displaystats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.display()


def ft_plant_analytics() -> None:
    print("=== Check year-old")
    days_to_check = 30
    print(f"Is {days_to_check} days more than a year? -> "
          f"{Plant.is_older_than_a_year(days_to_check)}")
    days_to_check = 400
    print(f"Is {days_to_check} days more than a year? -> "
          f"{Plant.is_older_than_a_year(days_to_check)}")
    print("")

    print("=== Flower")
    f1 = Flower("rose", 15, 10, "red")
    f1.show()
    displaystats(f1)
    f1.grow_plant(8)
    f1.bloom()
    displaystats(f1)
    print("")

    print("=== Tree")
    t1 = Tree("oak", 200, 365, 5)
    t1.show()
    displaystats(t1)
    t1.produce_shade()
    displaystats(t1)
    print("")

    print("=== Seed")
    s1 = Seed("sunflower", 80, 45, "yellow", 0)
    s1.show()
    s1.grow_plant(30)
    s1.age_plant(20)
    s1.grow_seed(42)
    s1.show()
    displaystats(s1)
    print("")

    print("=== Anonymous")
    a1 = Plant.anonymous()
    a1.show()
    displaystats(a1)


if __name__ == "__main__":
    print("=== Garden statistics ===")
    ft_plant_analytics()
