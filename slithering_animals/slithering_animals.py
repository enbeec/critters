from datetime import date

class GiantSnail:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Worm:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Snake:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class LeglessLizard:
	def __init__(self, name, species):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class MysteriousSlime:
	def __init__(self, name):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = "UNKNOWN" 

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
