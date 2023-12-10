import pygame

class Mob(pygame.sprite.Sprite):

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
                 drops: tuple, 
                 stats: tuple,
                 specialEffect: bool = None,
                 group = pygame.sprite.Group()) -> None:
        
        self.name = name
        self.drops = drops # dros (self explantory)
        self.stats = stats # name, health, r-attk1, r-attk2, defense, s-effect
        self.specialEffect = specialEffect

        self.group = group
        self.rect = pygame.Rect(center = (0, 0))

    @classmethod    
    def returnArmorBonus(cls) -> tuple[int]:
        raise NotImplementedError

    def update(self) -> None:
        return None

class Goblin(Mob):
    def __init__(self, 
                 name: str, 
                 drops: tuple, 
                 stats: tuple,
                 group) -> None:
        super().__init__(name, drops, 
                         stats, group)
        
    def update(self):
        pass
class Slime(Mob):
    def __init__(self, 
                name: str, 
                drops: tuple, 
                stats: tuple,
                group) -> None:
        super().__init__(name, drops, 
                         stats, group)
        
    def update(self):
        pass

    def removeSpriteGroup(self):
        pass