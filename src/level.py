import logging

import pygame

from src.player import Player
from src.components.support import import_folder
from src.constants import *

class Level(pygame.sprite.Sprite):
    def __init__(self):
        """
        initalize level
        makes the map and sprite
        """
        self.tiled_maps = import_folder("Assets/Resources/Maps", map=True)
        self.display_surface = pygame.display.get_surface()
        self.map = self.tiled_maps[0].make_map()


        self.map_prop = MapInformation(str(self.tiled_maps[0])) # gotta save what map they're in

        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self) -> None:
        """
        return None
        setups up the player
        """
        self.player = Player(group=self.all_sprites)
        Goblin_1.group = self.all_sprites
        
        self.enemy = Goblin_1

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
            self.display_surface.blit(self.map, (0, 0))
            self.all_sprites.custom_draw() 
            flags = self.all_sprites.update(dt, keys, self.map_prop)            # check if player can move during it
        return (flags, self.map_prop)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)

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