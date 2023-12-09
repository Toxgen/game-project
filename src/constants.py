from src.components.items import Armor, Consumable, Item, Weapons

from typing import Final
import pygame

# pygame constants
screen_dim: Final = (1152, 704) # 36 by 22 (x32)

# weapons
# name, description, buy, sell, damage increase
Fist = Weapons("Fist", "Your Fist", 0, 0, 2)
Goblin_Sword = Weapons("Goblin_sword", "A green, wooden sword", 10, 5, 4)
Weapon_tuple = (Fist, Goblin_Sword)

# Items
# name, description, buy, sell, effect
Small_Health_Potion = Consumable("small_health_potion", "A small, red potion", 5, 5, 5) # maybe do id if names are too much
Medium_Health_Potion = Consumable("medium_health_potion", "A medium, red potion", 20, 10, 10)
Large_Health_Potion = Consumable("large_health_potion", "A large, red potion", 30, 15, 20)

Potions = (Small_Health_Potion,
           Medium_Health_Potion,
           Large_Health_Potion)

# Texture
# Dirt = pygame.image.load()

if __name__ == "__main__":
    pass