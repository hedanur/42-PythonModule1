#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._age = age  #_age kullanmak mantıklı mı
        self.height = height
        self.is_bloom = False
        self.__stats = self.Stats()

    def get_stats(self):
        return self.__stats

    def grow(self, added_height):
        self.height += added_height
        self.__stats.grow_count += 1

    def age(self, added_age):
        self._age += added_age
        self.__stats.age_count += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self._age} days old")
        self.__stats.show_count += 1

    @staticmethod
    def is__big_age(day):
        if day > 365:
            return True
        else:
            return False

    class Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self, plant_name):
            print(f"[statistics for {plant_name}]")
            print(f"Stats: {self.grow_count} grow, {self.age_count} age\
 {self.show_count} show")


def display_plant_stats(plant): #?
    name = plant.name
    stats_obj = plant.get_stats()
    stats_obj.display(name)


class Tree(Plant):
    def __init__(self, name, height, _age, trunk_diameter):
        super().__init__(name, height, _age)
        self.trunk_diameter = trunk_diameter

    def show(self):
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}")
        print(f"[asking the {self.name} to produce shade]")

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self.height}\
 long and {self.trunk_diameter} wide.")


class Flower(Plant):
    def __init__(self, name, height, _age, color):
        super().__init__(name, height, _age)
        self.color = color

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if not self.is_bloom:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def bloom(self):
        if not self.is_bloom:
            self.is_bloom = True


class Vegetable(Plant):
    def __init__(self, name, height, _age, harvest, nutritional):
        super().__init__(name, height, _age)
        self.harvest = harvest
        self.nutritional = nutritional

    def show(self):
        super().show()
        print(f" Harvest season: {self.harvest}")
        print(f" Nutritional value: {self.nutritional}")

    def age(self, n):
        self.nutritional += n
        super().age(n)


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
    print("[asking the rose to bloom]")
    rose.show()
    display_plant_stats(rose)

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
