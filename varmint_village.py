from walking_animals import Alpaca, Pony, Goat, Jackass, Hedgehog
from swimming_animals import SpottedEel, Koi, Trout, Seahorse, Piranha
from slithering_animals import GiantSnail, Worm, Snake, LeglessLizard, MysteriousSlime

class PettingZoo:
	def __init__(self, name, description = None): # make description optional
		self.attraction_name = name
		self.description = description or "cute and fuzzy critters to cuddle" # if no description, a default
		# an empty list to store our animals in
		self.animals = list()

vv = PettingZoo("Varmint Village")

# let's get some crowd pleasers in there
alfie = Alpaca("Alfie", "Huacaya Alpaca", "alpaca feed", "morning")
vv.animals.append(alfie)

for animal in vv.animals:
	print(f'You can find {animal.name} the {animal.species} in {vv.attraction_name}')