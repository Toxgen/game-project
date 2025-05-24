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
        self.tiled_maps = import_folder(path, map=True)
        self.display_surface = pygame.display.get_surface()
        
        self.map = self.tiled_maps[0]
        self.surf = self.map.make_map()        
        self.all_sprites = CameraGroup()
        self.gui = GUI()

        self.setup()
        self._cls_args = {
            "dt": 0.0,
            "keys": {},
            "player_flags": {},
            "first": False
        }

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

    def run(self, dt: float, keys: dict) -> None:
        """
        secondary game function
        draws map and sprites

        dt: delta time
        keys: keys pressed
        """
        # assign cls_args to be used to update
        for item in self._cls_args:
            try:
                self._cls_args[item] = locals()[f"{item}"]
            except KeyError as ke:
               continue

        self._cls_args["first"] = False
        self._cls_args["player_flags"] = self.player.update(self._cls_args)
        self._cls_args["first"] = True

        self.all_sprites.custom_draw(self.player, self.map)
        self.gui.text_render(self._cls_args)

        self.all_sprites.update(self._cls_args)

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
        self.surf = map.make_map(self.offset) # ??? (idk but it works)
        self.display_surface.blit(self.surf, (0, 0))
    
        for sprite in self.sprites():
            offset_rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.image, offset_rect)

class GUI(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        pygame.font.init()

        # {'dt': 0.008, 'keys': {'mouse_down': False}, 'player_flags': {'speed': ('200', 23.04, 21.12)}, 'first': True}

        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.SysFont("arial", 20, pygame.font.Font.bold)
        self.successful_renders = 0

    def text_render(self, cls_args: dict):
        """
        renders text to the display
        cls_args[text, info] = [text, x, y]
        """
        if cls_args is None:
            return

        for i, (text, info) in enumerate(cls_args.items()):
            if i not in [0, 1, 2]:
                continue

            if isinstance(info, tuple):
                if isinstance(info[1], bool):
                    return
                elif not isinstance(info[0], str):
                    info[0] = str(info)
                text_surface = self.font.render(text + ': ' + info, True, (255, 255, 255))

            else:
                info = (str(info))
                text_surface = self.font.render(text + ': ' + info, True, (255, 255, 255))

            self.display_surface.blit(text_surface, (scrx * 2, scry * 3 * (self.successful_renders + 1)))
            self.successful_renders += 1

        self.successful_renders = 0
