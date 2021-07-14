class PettingZoo:
	def __init__(self, name, description = None): # make description optional
		self.attraction_name = name
		self.description = description or "cute and fuzzy critters to cuddle" # if no description, a default
		self.animals = list()

	@property
	def last_animal_added(self):
		return f'Last animal added to {self.attraction_name}: { self.animals[-1].name }'

class SnakePit:
	def __init__(self, name, description = None): # make description optional
		self.attraction_name = name
		self.description = description or "all crawlies and admittedly some creepies" # if no description, a default
		# an empty list to store our animals in
		self.animals = list()

	@property
	def last_animal_added(self):
		return f'Last animal added to {self.attraction_name}: { self.animals[-1].name }'

class Wetlands:
	def __init__(self, name, description = None): # make description optional
		self.attraction_name = name
		self.description = description or "splish splash" # if no description, a default
		# an empty list to store our animals in
		self.animals = list()

	@property
	def last_animal_added(self):
		return f'Last animal added to {self.attraction_name}: { self.animals[-1].name }'