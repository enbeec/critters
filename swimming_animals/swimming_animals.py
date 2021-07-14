from datetime import date

class SpottedEel:
	def __init__(self, name, species, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Koi:
	def __init__(self, name, species, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Trout:
	def __init__(self, name, species, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Seahorse:
	def __init__(self, name, species, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Piranha:
	def __init__(self, name, species, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
