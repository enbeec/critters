from animals import ( 
	Alpaca, 
	Pony, 
	Goat, 
	Jackass, 
	Hedgehog,
	SpottedEel, 
	Koi, 
	Trout, 
	Seahorse, 
	Piranha, 
	GiantSnail, 
	Worm, 
	Snake, 
	LeglessLizard, 
	MysteriousSlime 
	)
from attractions import PettingZoo, SnakePit, Wetlands


varmint_village = PettingZoo("Varmint Village")
belly_bay = SnakePit("Belly Bay")
sunny_shores = Wetlands("Sunny Shores")

alfie = Alpaca("Alfie", "huacaya alpaca", "alpaca feed", 123456, "morning")
varmint_village.animals.append(alfie)
peter = Pony("Peter", "shetland pony", "oats and hay", "midday")
varmint_village.animals.append(peter)
gilbert = Goat("Gilbert", "mountain goat", "literally anything", "afternoon")
varmint_village.animals.append(gilbert)

greg = GiantSnail("Greg", "big ass snail", "leaves and shit like that", 234567)
belly_bay.animals.append(greg)
walden = Worm("Walden", "earthworm", "dirt", 234568)
belly_bay.animals.append(walden)

sally = SpottedEel("Sally", "teal spotted eel", "tiny crabs", 345678)
sunny_shores.animals.append(sally)

# we don't have a list of attractions to iterate so we just create one real quick
for attraction in [varmint_village, belly_bay, sunny_shores]:
	for animal in attraction.animals:
		print(f'You can find {animal.name} the {animal.species} in {attraction.attraction_name}')

# separator -- put your test stuff below this
print()