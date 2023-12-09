import pygame
import pytmx
from src.player import Player

class Level(pygame.sprite.Sprite):
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player(group=self.all_sprites)

    def run(self, dt): 
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)