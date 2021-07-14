from datetime import date

class Animal:
	def __init__(self, name, species, food, chip_num):
		self.name = name
		self.species = species
		self.food = food
		self.__chip_num = chip_num
		self.date_added = date.today()

	def __str__(self):
		return f'{self.name} ({self.chip_num}) is a {self.species}'

	@property
	def chip_num(self):
		return self.__chip_num

	@chip_num.setter
	def chip_num(self, number):
		pass # do nothing

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')