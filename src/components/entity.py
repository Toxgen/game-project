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
                 specialEffect: Optional[str] | None = None) -> None:
        
        self.name = name
        self.drops = drops # dros (self explantory)
        self.stats = stats # name, health, r-attk1, r-attk2, defense, s-effect
        self.specialEffect = specialEffect

        self.group = pygame.sprite.Group()
        self.rect = pygame.Rect(center = (0, 0))
        
    def returnArmorBonus(self) -> tuple[int]:
       return 

    def foo(self, 
            heatlh: int = 0) -> tuple[int]:
        pass

    def update(self) -> None:
        return None

class Goblin(Mob):
    def __init__(self, 
                 name: str, 
                 drops: tuple, 
                 stats: tuple) -> None:
        super().__init__(name, drops, 
                         stats)

class Slime(Mob):
    def __init__(self, 
                name: str, 
                drops: tuple, 
                stats: tuple) -> None:
        super().__init__(name, drops, stats)