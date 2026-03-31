class Plant:
	def __init__(self, name, height, age):
		self.age = age
		self.name = name
		self.height = height
def plant_str(p):
	print(f"{p.name}: {p.height}cm, {p.age} days old")

if __name__ == "__main__":
	plant1 = Plant("Rose",25,30)
	plant2 = Plant("Sunflower",80,45)
	plant3 = Plant("Cactus",15,120)
	print("=== Garden Plant Registry ===")
	plant_str(plant1)
	plant_str(plant2)
	plant_str(plant3)
