from src.components.items import Item
from src.components.entity import Entity

from typing import Final
import pygame

# pygame constants
screen_dim: Final = (1152, 704) # 36 by 22 (x32)

# constants
allowed_areas = (
    "placeholder",
)
# enemies
Goblin_1 = Entity("goblin")
# weapons
Fist = Item("fist", "Your Fist", "weapon",
            buy=-1, sell=-1, damage=2)
Goblin_Sword = Item("goblin_sword", "A green, wooden sword", "weapon",
                    buy=10, sell=5, damage=4)

# Items
Small_Health_Potion = Item("small_health_potion", "A small, red potion", "potion", 
                           sell=10, buy=5, effect=5)
Medium_Health_Potion = Item("medium_health_potion", "A medium, red potion", "potion",
                            buy=20, sell=10, effect=10)
Large_Health_Potion = Item("large_health_potion", "A large, red potion", "potion",
                           buy=30, sell=15, effect=20)

if __name__ == "__main__":
    pass