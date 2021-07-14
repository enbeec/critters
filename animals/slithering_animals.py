from .animal import Animal

class GiantSnail(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.slithering = True

class Worm(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.slithering = True

class Snake(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.slithering = True

class LeglessLizard(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.slithering = True

class MysteriousSlime(Animal):
	def __init__(self, name, _, food, chip_num):
		super().__init__(name, "UNKNOWN SPECIES", food, chip_num)
		self.slithering = True
