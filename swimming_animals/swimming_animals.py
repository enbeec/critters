from datetime import date

class SpottedEel:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Koi:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Trout:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Seahorse:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Piranha:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
