#!/usr/bin/env python3

class Plant:
    name: str
    _height: float
    _age: int

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._age = age
        self._height = height

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, value: float) -> None:
        if (value < 0):
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {int(value)}cm")

    def set_age(self, value: int) -> None:
        if (value < 0):
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
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




# #!/usr/bin/env python3

# class Plant:
#     name: str
#     _height: float
#     _age: int

#     def __init__(self, name: str, height: float, age: int) -> None:
#         self.name = name

#         # SUBJECT KURALI: Başlangıç değerleri geçersizse varsayılan (0) ata
#         if height < 0:
#             print(f"{self.name}: Error, initial height can't be negative. Setting to 0.0")
#             self._height = 0.0
#         else:
#             self._height = height

#         if age < 0:
#             print(f"{self.name}: Error, initial age can't be negative. Setting to 0")
#             self._age = 0
#         else:
#             self._age = age

#     def get_height(self) -> float:
#         return self._height

#     def get_age(self) -> int:
#         return self._age

#     def set_height(self, value: float) -> None:
#         if value < 0:
#             print(f"{self.name}: Error, height can't be negative")
#             print("Height update rejected")
#             # Değişiklik yapmıyoruz, veri eski haliyle kalıyor (Data Integrity)
#         else:
#             self._height = value
#             print(f"Height updated: {int(value)}cm")

#     def set_age(self, value: int) -> None:
#         if value < 0:
#             print(f"{self.name}: Error, age can't be negative")
#             print("Age update rejected")
#         else:
#             self._age = value
#             print(f"Age updated: {value} days\n")

# def main() -> None:
#     print("=== Garden Security System ===")

#     # Test 1: Geçerli başlangıç
#     rose = Plant("Rose", 15.0, 10)
#     print(f"Plant created: {rose.name}: {rose.get_height()}cm, {rose.get_age()} days old\n")

#     # Test 2: Geçersiz güncelleme (Rejected kısmı)
#     rose.set_height(-30.0)

#     # Test 3: Geçersiz başlangıç (Default value kısmı)
#     print("\nAttempting to create a plant with negative values:")
#     cactus = Plant("Cactus", -5.0, -10)
#     cactus.show_status() # Bilgileri basan bir metodun olduğunu varsayarsak

# if __name__ == "__main__":
#     main()
