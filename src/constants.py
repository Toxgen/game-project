from .components.items import Armor, Consumable, Item, Weapons

# might need to put this into the pyinstaller hidden files thingy !!

# weapons
# name, description, buy, sell, damage increase
Fist = Weapons("Fist", "Your Fist", 0, 0, 2)
Goblin_Sword = Weapons("Goblin_sword", "A green, wooden sword", 10, 5, 4)
weapon_list = (Fist, Goblin_Sword)

# Items
# name, description, buy, sell, effect
sHP = Consumable("small_health_potion", "A small, red potion", 5, 5, 5)
mHP = Consumable("medium_health_potion", "A medium, red potion", 20, 10, 10)
lHP = Consumable("large_health_potion", "A large, red potion", 30, 15, 20)
potion_list = (sHP, mHP, lHP)
