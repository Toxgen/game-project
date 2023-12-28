import pygame
import pytmx

from src.player import Player
from src.components.support import import_folder

class Level(pygame.sprite.Sprite):
    def __init__(self):
        self.tiled_maps = import_folder("Assets/Resources/Maps", map=True)
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()

        self.setup()

    def setup(self):

        self.player = Player(group=self.all_sprites)
        self.player.load()

    def save(self):
        self.player.save()

    def run(self, dt): 
        self.display_surface.fill('blue')
        self.all_sprites.custom_draw()
        self.all_sprites.update(dt)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)