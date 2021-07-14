from .animal import Animal

class Alpaca(Animal):
	def __init__(self, name, species, food, chip_num, shift = None): # this makes shift optional when creating
		super().__init__(name, species, food, chip_num)
		self.shift = shift or "unassigned"


class Jackass(Animal):
	def __init__(self, name, species, food, chip_num, shift = None): # this makes shift optional when creating
		super().__init__(name, species, food, chip_num)
		self.shift = shift or "unassigned"

class Pony(Animal):
	def __init__(self, name, species, food, chip_num, shift = None): # this makes shift optional when creating
		super().__init__(name, species, food, chip_num)
		self.shift = shift or "unassigned"

class Goat(Animal):
	def __init__(self, name, species, food, chip_num, shift = None): # this makes shift optional when creating
		super().__init__(name, species, food, chip_num)
		self.shift = shift or "unassigned"

class Hedgehog(Animal):
	def __init__(self, name, species, food, chip_num, shift = None): # this makes shift optional when creating
		super().__init__(name, species, food, chip_num)
		self.shift = shift or "unassigned"
		self.requiredSpeed = "Fast"

