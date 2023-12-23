import pygame

from src.components.support import import_folder

class Entity(pygame.sprite.Sprite):

    __mob_data = (
    # woods [0][0 - 2]
    ("goblin", 8, 2, 3, 1, None), # name, health, r-attk1, r-attk2, defense, s-effect
    ("slime", 12, 3, 4, 3, None),
    ("wolf", 7, 5, 7, 2, None)
    # plains [1][0 - ?]
    )

    __mob_drops = {
        "goblin": ("goblin_hide", "goblin_leg", "goblin_sword", "goblin_staff", 
                "goblin_chestplate", "goblin_legging", "goblin_helmet"),
        "slime": ("nothing u got scammed lol"),
        "wolf": ("You also got scammed lol")
    }


    __drop_data = {
        "goblin": (("goblin_hide", 25), ("goblin_leg", 12), 
            ("goblin_sword", 8), ("goblin_staff", 5), 
            ("goblin_chestplate", 3), ("goblin_legging", 2), 
            ("goblin_helmet", 1))
    }

    def __init__(self, 
                 name: str, 
                 drops: dict, 
                 stats: dict,
                 group = pygame.sprite.Group(),
                 pos: tuple[int, int] = (0, 0)) -> None:
        
        self.name = name
        self.drops = drops 
        self.stats = stats 

        self.group = group
        self.image = self.getImage()
        self.rect = pygame.Rect(center = pos)

    def getImage(self):
        _fullpath = "Assets/Mob/" + self.name
        return import_folder(_fullpath)

    def returnAttackDamage(self) -> int:
        from random import randint

        return (round(randint(self.stats["attk1"], self.stats["attk2"]) * 1.2)) 

    def update(self) -> None:
        return None
    
    