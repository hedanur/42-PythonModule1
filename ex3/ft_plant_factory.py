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


