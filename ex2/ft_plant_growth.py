#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int
    growth_rate: float

    def __init__(
        self, name: str = "", height: float = 0.0, age: int = 0
    ) -> None:
        self.age = age
        self.name = name
        self.height = height
        self.growth_rate = 0.8

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age_plant(self) -> None:
        self.age += 1


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    first_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()

    i = 1
    while i < 8:
        rose.grow()
        rose.age_plant()

        print(f"=== Day {i} ===")
        rose.show()
        i += 1
    total_height = round(rose.height - first_height, 1)
    print(f"Growth this week: {total_height}cm")
