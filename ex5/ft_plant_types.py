#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._age = age
        self._height = float(height)

    def grow(self, added_height: float) -> None:
        self._height += added_height

    def age(self, added_age: int) -> None:
        self._age += added_age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


class Tree(Plant):
    _trunk_diameter: float

    def __init__(
                self, name: str, height: float, age: int,
                trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:

        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm\
 long and {self._trunk_diameter}cm wide.")


class Flower(Plant):
    _color: str
    _is_bloom: bool

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._is_bloom = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if not self._is_bloom:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

    def bloom(self) -> None:
        self._is_bloom = True


class Vegetable(Plant):
    _harvest: str
    _nutritional: int

    def __init__(
                self, name: str, height: float, age: int,
                harvest: str, nutritional: int = 0) -> None:
        super().__init__(name, height, age)
        self._harvest = harvest
        self._nutritional = nutritional

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest}")
        print(f" Nutritional value: {self._nutritional}")

    def grow(self, n: float) -> None:
        super().grow(n)

    def age(self, n: int) -> None:
        self._nutritional += n
        super().age(n)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[asking the {oak._name.lower()} to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print(f"[make {tomato._name.lower()} grow and age for 20 days]")
    tomato.grow(42.0)
    tomato.age(20)
    tomato.show()
