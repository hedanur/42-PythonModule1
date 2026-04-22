#!/usr/bin/env python3

class Plant:
    name: str
    height: float
    age: int

    def __init__(self) -> None:
        self.age = 0
        self.name = ""
        self.height = 0
        self.growth_rate = 0.8

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age_plant(self) -> None:
        self.age += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.age = 30

    print("=== Garden Plant Growth ===")
    rose.show()
    rose.grow()
    rose.age_plant()
    i = 1
    while i < 8:
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow()
        rose.age_plant()
        i += 1
    print(f"Growth this week: {round(0.8 * 7, 1)}cm")
