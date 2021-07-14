class PettingZoo:
	def __init__(self, name, description = None): # make description optional
		self.attraction_name = name
		self.description = description or "cute and fuzzy critters to cuddle" # if no description, a default
		# an empty list to store our animals in
		self.animals = list()

class SnakePit:
	def __init__(self, name, description = None): # make description optional
		self.attraction_name = name
		self.description = description or "all crawlies and admittedly some creepies" # if no description, a default
		# an empty list to store our animals in
		self.animals = list()

class Wetlands:
	def __init__(self, name, description = None): # make description optional
		self.attraction_name = name
		self.description = description or "splish splash" # if no description, a default
		# an empty list to store our animals in
		self.animals = list()