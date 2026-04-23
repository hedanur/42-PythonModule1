#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int
    _is_bloom: bool

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._age = age
        self._height = float(height)
        self._is_bloom = False
        self._stats = self.Stats()

    def get_stats(self) -> 'Plant.Stats':
        return self._stats

    def grow(self, added_height: float) -> None:
        self._height += added_height
        self._stats.grow_count += 1

    def age(self, added_age: int) -> None:
        self._age += added_age
        self._stats.age_count += 1

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._stats.show_count += 1

    @staticmethod
    def is__big_age(day: int) -> bool:
        if day > 365:
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        grow_count: int
        age_count: int
        show_count: int

        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self, plant_name: str) -> None:
            print(f"[statistics for {plant_name}]")
            print(f"Stats: {self.grow_count} grow, {self.age_count} age,\
 {self.show_count} show")


def display_plant_stats(plant: Plant) -> None:
    stats_obj = plant.get_stats()
    stats_obj.display(plant._name)


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
                self, name: str, height: float, age: int,
                trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter
        self._stats = self.Stats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm\
 long and {self._trunk_diameter}cm wide.")
        if isinstance(self._stats, Tree.Stats):
            self._stats.shade_count += 1

    class Stats(Plant.Stats):
        shade_count: int

        def __init__(self) -> None:
            super().__init__()
            self.shade_count = 0

        def display(self, plant_name: str) -> None:
            super().display(plant_name)
            print(f" {self.shade_count} shade")


class Flower(Plant):
    _color: str

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._is_bloom:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._is_bloom = True


class Seed(Flower):
    _seeds: int

    def __init__(
                self, name: str, height: float, age: int,
                color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self._seeds = seeds

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def age(self, n: int, n_seed: int = 0) -> None:
        super().age(n)
        self._seeds += n_seed


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is__big_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is__big_age(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)
    rose.grow(8.0)
    rose.bloom()
    print("[asking the rose to grow and bloom]")
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)
    print(f"[asking the {oak._name.lower()} to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 0)
    sunflower.show()
    sunflower.bloom()
    print(f"[make {sunflower._name.lower()} grow, age and bloom]")
    sunflower.grow(30)
    sunflower.age(20, 42)
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous")
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_stats(anon)
