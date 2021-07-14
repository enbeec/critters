from datetime import date

class Alpaca:
	def __init__(self, name, species, shift, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Jackass:
	def __init__(self, name, species, shift, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Pony:
	def __init__(self, name, species, shift, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Goat:
	def __init__(self, name, species, shift, food):
		self.date_added = date.Today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Hedgehog:
	def __init__(self, name, species, shift, food):
		self.date_added = date.Today()
		self.walking = True
		self.requiredSpeed = "Fast"
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
