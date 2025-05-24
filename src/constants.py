import pathlib

# from .components.items import Item
# from .components.entity import Entity

from typing import Final

# pygame constants & other constants
screen_dim: Final = (1152, 704)  # 36 by 22 (x32)
scrx = screen_dim[0] / 100
scry = screen_dim[1] / 100

# constants
layers = {"grass": 1, 
          "water": 2}

path = pathlib.Path(__file__ + "/../../Assets/Resources/Maps").resolve()

if __name__ == "__main__":
    pass



# # enemies
# mob_stats: tuple = ( 
#     ("goblin", 8, 2, 3, 1,
#      None),  # name, health, r-attk1, r-attk2, defense, s-effect
# )

# mob_drops: dict = {
#     "goblin": ("goblin_hide", "goblin_leg", "goblin_sword", "goblin_staff",
#                "goblin_chestplate", "goblin_legging", "goblin_helmet"),
# }

# drop_data: dict = {
#     "goblin": (("goblin_hide", 25), ("goblin_leg", 12), ("goblin_sword", 8),
#                ("goblin_staff", 5), ("goblin_chestplate", 3),
#                ("goblin_legging", 2), ("goblin_helmet", 1))
# }

# goblin_1 = Entity("goblin", group=None)
# # weapons

# Fist = Item("fist", 
#             "Your Fist", 
#             "weapon", 
#             buy=-1, 
#             sell=-1, 
#             damage=2)

# Goblin_Sword = Item("goblin_sword",
#                     "A green, wooden sword",
#                     "weapon",
#                     buy=10,
#                     sell=5,
#                     damage=4)

# weapons = {"fist": Fist, "goblin_sword": Goblin_Sword}

# # Items
# Small_Health_Potion = Item("small_health_potion",
#                            "A small, red potion",
#                            "potion",
#                            sell=10,
#                            buy=5,
#                            effect=5)
# Medium_Health_Potion = Item("medium_health_potion",
#                             "A medium, red potion",
#                             "potion",
#                             buy=20,
#                             sell=10,
#                             effect=10)
# Large_Health_Potion = Item("large_health_potion",
#                            "A large, red potion",
#                            "potion",
#                            buy=30,
#                            sell=15,
#                            effect=20)