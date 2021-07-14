from .animal import Animal

class SpottedEel(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.swimming = True

class Koi(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.swimming = True
		
class Trout(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.swimming = True

class Seahorse(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.swimming = True

class Piranha(Animal):
	def __init__(self, name, species, food, chip_num):
		super().__init__(name, species, food, chip_num)
		self.swimming = True