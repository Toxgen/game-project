import logging
from sys import argv

import pygame

from src.player import Player
from src.components.support import import_folder
from src.constants import *
from src.components.surfaces import *

class Level:
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

        self.setup()

        # This is for debugging
        if (len(argv) > 1 and argv[1].lower() == "true"):
            self._debug = True
            logging.log(logging.info, "Debugging activated")
        else:
            self._debug = False

    def save(self):
        """
        Saves the player's data when escape happens
        """

        self.player.save()

    def setup(self) -> None:
        """
        return None
        setups up the player
        """
        self.player = Player(group=self.all_sprites)

    def run(self, dt: float, keys: dict) -> tuple:
        """
        return tuple (player flags, map properties -> teleport locations)
        secondary game function
        draws map and sprites

        dt: delta time
        keys: keys pressed
        """
        player_flags = self.player.update(dt, keys)
        self.all_sprites.custom_draw(self.player, self.map)
        # player flags are just the hitbox rect
        self.all_sprites.update(player_flags, keys=None)

class CameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        """
        Initalizes the camera for the player
        """
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player, map):
        self.offset.x = player.rect.centerx - screen_dim[0] / 2
        self.offset.y = player.rect.centery - screen_dim[1] / 2

        self.display_surface.fill((0, 0, 0))
        self.surf = map.make_map(self.offset) # ???
        self.display_surface.blit(self.surf, (0, 0))
    
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)
