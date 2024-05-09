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

        self.map_prop = MapProperties((self.tiled_maps[0].__name__, teleports)) # gotta save what map they're in

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

    def run(self, dt, events, flags: dict) -> tuple:
        """
        return tuple (for the game function to utilize)
        secondary game function
        draws map and sprites
        """
        a = [flag for flag in flags.values() if flag]
        if a:
            self.display_surface.blit(self.map, (0, 0))
            self.all_sprites.custom_draw() # do a return statemne w/ rect
            self.all_sprites.update(dt, events)
            # detect if the player hit the rect for the map
        return (self.player, self.map_prop)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)

class MapProperties():
    def __init__(self, props: tuple) -> None:
        self.props = props

    def get(self) -> tuple:
        return self.props