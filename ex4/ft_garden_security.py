#!/usr/bin/env python3

class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if (value < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {int(value)}cm")

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days\n")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    print("Plant created: ", end="")
    rose = Plant("Rose", 15.0, 10)
    print(f"{rose._name}: {rose.get_height()}cm, {rose.get_age()} days old\n")

    rose.set_height(25.0)
    rose.set_age(30)

    rose.set_height(-30)
    rose.set_age(-30)
    print(f"\nCurrent state: {rose._name}: {rose.get_height()}cm,\
 {rose.get_age()} days old")
