#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

        print(f"[asking the {self.name} to produce shade]")


        #def produce_shade():
        super().show()


class Flower(Plant):
    def __init__(self, name, height, age, colour):
        super().__init__(name, height, age)
        self.colour = colour
        super().show()

        def bloom():
            self.is_blooming = True
            if()
                print(f"{self.name} is blooming beautifully!")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest, nutritional):
        super().__init__(name, height, age)
        self.harvest = harvest
        self.nutritional = nutritional
        super().show()

        print(f"Trunk diameter: {self.height}cm")
        print(f"[make {self.name} grow and age for {self.height} days]")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    print(f"Colour: {rose.colour}")
    print()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    print(f"Harvest season: {tomato.harvest}")
    print(f"Nutritional value: {tomato.nutritional}")


#"Overriding"
