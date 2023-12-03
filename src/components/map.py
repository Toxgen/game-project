import pygame

pygame.init()

class Tile:
    def __init__(self,
                 sprite: pygame.sprite,
                 passable: bool,
                 terrain_type: str,
                 special: str = None):
        
        self.sprite = sprite
        self.passable = passable
        self.terrain_type = terrain_type
        self.special = special