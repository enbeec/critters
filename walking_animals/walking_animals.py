from datetime import date

class Alpaca:
	def __init__(self, name, species, shift = None):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"

class Jackass:
	def __init__(self, name, species, shift = None):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"


class Pony:
	def __init__(self, name, species, shift = None):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"

class Goat:
	def __init__(self, name, species, shift = None):
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"

class Hedgehog:
	def __init__(self, name, species, shift = None):
		self.date_added = date.today()
		self.walking = True
		self.requiredSpeed = "Fast"
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"