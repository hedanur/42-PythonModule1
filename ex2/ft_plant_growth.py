#!/usr/bin/env python3

class Plant:
    def __init__(self):
        self.age = None
        self.name = None
        self.height = None

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age_plant(self):
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
    while (i < 8):
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow()
        rose.age_plant()
        i += 1
    print(f"Growth this week: {round(0.8 * 7, 1)}cm")
