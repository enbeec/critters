from datetime import date

class Alpaca:
	def __init__(self, name, species, food, chip_num, shift = None): # this makes shift optional when creating
		self.__chip_num = chip_num
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

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

class Jackass:
	def __init__(self, name, species, food, shift = None): # this makes shift optional when creating
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Pony:
	def __init__(self, name, species, food, shift = None): # this makes shift optional when creating
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Goat:
	def __init__(self, name, species, food, shift = None): # this makes shift optional when creating
		self.date_added = date.today()
		self.walking = True
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

class Hedgehog:
	def __init__(self, name, species, food, shift = None): # this makes shift optional when creating
		self.date_added = date.today()
		self.walking = True
		self.requiredSpeed = "Fast"
		self.name = name
		self.species = species
		# shift defaults to "unassigned"
		self.shift = shift or "unassigned"
		self.food = food

	def __str__(self):
		return f'{self.name} is a {self.species}'

	def feed(self):
		print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
