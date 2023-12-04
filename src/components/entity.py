import pygame
from typing import Optional

class Mob(pygame.sprite.Sprite):

    armorDefBonus = (
        "",
    )

    def __init__(self, 
                 name: str, 
                 drops: tuple, 
                 stats: tuple,
                 specialEffect: Optional[str] | None = None,
                 group = pygame.sprite.Group()) -> None:
        
        self.name = name
        self.drops = drops # dros (self explantory)
        self.stats = stats # name, health, r-attk1, r-attk2, defense, s-effect
        self.specialEffect = specialEffect

        self.group = group
        self.rect = pygame.Rect(center = (0, 0))

    @classmethod    
    def returnArmorBonus(cls) -> tuple[int]:
        pass
    @classmethod
    def addToClassGroup(self) -> None:
        pass

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