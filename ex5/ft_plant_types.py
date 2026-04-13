#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._age = age  #_age kullanmak mantıklı mı
        self.height = height
        self.is_bloom = False

    def grow(self, added_height):
        self.height += added_height

    def age(self, added_age):
        self._age += added_age

    def show(self):
        print(f"{self.name}: {self.height}cm, {self._age} days old")


class Tree(Plant):
    def __init__(self, name, height, _age, trunk_diameter):
        super().__init__(name, height, _age)
        self.trunk_diameter = trunk_diameter

        print(f"[asking the {self.name} to produce shade]") #bu print burada mi kalmalı

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}\
 long and {self.trunk_diameter} wide.")


class Flower(Plant):
    def __init__(self, name, height, _age, colour):
        super().__init__(name, height, _age)
        self.colour = colour

    def show(self):
        super().show()
        print(f" Colour: {rose.colour}")

    def bloom(self):
        if not self.is_bloom:
            self.is_bloom = True
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Vegetable(Plant):
    def __init__(self, name, height, _age, harvest, nutritional):
        super().__init__(name, height, _age)
        self.harvest = harvest
        self.nutritional = nutritional

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest}")
        print(f"Nutritional value: {self.nutritional}")

    def age(self, n):
        self.nutritional += n
        super().age(n)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print("[asking the rose to bloom]")
    rose.show()
    rose.bloom()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print(f"[make {tomato.name} grow and age for 20 days]")
    tomato.grow(42)
    tomato.age(20)
    tomato.show()



#"Overriding"
