from datetime import date

class Alpaca:
	def __init__(self, name, species, shift):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Jackass:
	def __init__(self, name, species, shift):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"


class Pony:
	def __init__(self, name, species, shift):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"

class Goat:
	def __init__(self, name, species, shift):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"

class Hedgehog:
	def __init__(self, name, species, shift):
		self.date_added = date.Today()
		self.walking = True
		self.requiredSpeed = "Fast"
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"