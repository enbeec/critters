from datetime import date

class Alpaca:
	def __init__(self, name, species):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species

class Jackass:
	def __init__(self, name, species):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species


class Pony:
	def __init__(self, name, species):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species

class Goat:
	def __init__(self, name, species):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species

class Hedgehog:
	def __init__(self, name, species):
		self.date_added = date.today()
		self.walking = True
		self.requiredSpeed = "Fast"
		self.name = name
		self.species = species