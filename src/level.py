import logging
import pytmx

import pygame

from src.player import Player
from src.components.support import import_folder
from src.constants import *
from src.components.surfaces import *

class Level(pygame.sprite.Sprite):
    def __init__(self):
        """
        initalize level
        makes the map and sprite
        """
        self.tiled_maps = import_folder("Assets/Resources/Maps", map=True)
        self.display_surface = pygame.display.get_surface()
        
        self.map = self.tiled_maps[0]
        self.surf = self.map.make_map()        
        self.all_sprites = CameraGroup()
        
        for x, y, surf in self.map.tmx_data.get_layer_by_name(layers).tiles():
            Other((x*32, y*32), surf, self.all_sprites)


        self.map_prop = MapInformation(str(self.tiled_maps[1])) # gotta save what map they're in

        self.setup()

    def setup(self) -> None:
        """
        return None
        setups up the player
        """
        self.player = Player(group=self.all_sprites)
        self.enemy = Entity("goblin", group=self.all_sprites)

    def save(self) -> None:
        """
        return None
        saves current player data
        """
        self.player.save()

    def run(self, dt: float, keys: dict, flags: dict) -> tuple:
        """
        return tuple (player flags, map properties -> teleport locations)
        secondary game function
        draws map and sprites

        dt: delta time
        keys: keys pressed
        flags: flags to check if other events are happening, ex: teleportation
        """

        a = [flag for flag in flags.values() if flag]
        if not a:
            self.all_sprites.custom_draw(self.player, self.map)
            flags = self.all_sprites.update(dt, keys, self.map_prop)            # check if player can move during it
        return (flags, self.map_prop)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player, map):
        self.offset.x = player.rect.centerx - screen_dim[0] / 2
        self.offset.y = player.rect.centery - screen_dim[1] / 2

        self.display_surface.fill((0, 0, 0))
        self.surf = map.make_map(self.offset)
        self.display_surface.blit(self.surf, (0, 0))
    
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
            

class MapInformation():


    def __init__(self, name: str) -> None:
        self.name = name
        self.teleports = {

                "test": {
                    "pnt1": Rect((200, 200), (300, 200)),
                    "pnt2": Rect((100, 100), (100, 100))# (far x?, far y?) (length?, width?)
                }

            }
        
    def __str__(self):
        return self.name