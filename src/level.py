import pygame

from src.constants import all_Enemies
from src.player import Player

class Level(pygame.sprite.Sprite):
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = CameraGroup()
        self.enemies = OutsideCameraGroup() 

        self.setup()

    def setup(self):
        self.player = Player(group=self.all_sprites)
        for enemies in all_Enemies:
            enemies.setup()
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


class OutsideCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def custom_draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)