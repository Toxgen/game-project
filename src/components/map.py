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
    
class Render:
    def __init__(self, map):
        self.map = map

    def render(self, 
               tile_size = 30):
        
        for x, row in enumerate(self.map):
            for y, tile in enumerate(row):
                pygame.blit(tile, (x * tile_size, y * tile_size))