#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._age = age
        self._height = height

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, value):
        if (value < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
            self.height = value
        else:
            self._height = value
            print(f"Height updated: {int(value)}cm")

    def set_age(self, value):
        if (value < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
            self.age = value
        else:
            self._age = value
            print(f"Age updated: {value} days\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    print("Plant created: ", end="")
    rose = Plant("Rose", 15.0, 10)
    print(f"{rose.name}: {rose.get_height()}cm, {rose.get_age()} days old\n")

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-30)
    rose.set_age(-30)
    print(f"\nCurrent state: {rose.name}: {rose.get_height()}cm,\
 {rose.get_age()} days old")
