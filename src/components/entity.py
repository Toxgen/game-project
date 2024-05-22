import pygame
import math
import logging

from random import randint

from src.components.support import import_folder
from src.constants import *
from src.components.timer import Timer

class Entity(pygame.sprite.Sprite):

    def __init__(self, 
                 name: str, 
                #  drops: dict, 
                #  stats: dict, just gets these from the dictionaries or just use args for those
                #  hp: int,
                #  defense: int,
                 group,
                 pos: tuple[int, int] = (0, 0)) -> None:
        
        self.name = name

        self.group = group
        self.image = self.getImage()

        self.rect = self.image[0].get_rect(center = pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 150

        self.isAlive = False
        self.timer = {
            "dead": Timer(30000)
        }

    def getImage(self):
        _fullpath = "Assets/Resources/Mob/" + self.name
        return import_folder(_fullpath)

    def returnAttackDamage(self) -> int:
        return (round(randint(self.stats["attk1"], self.stats["attk2"]) * 1.2))
    
    def hit(self, hit: bool = False):
        if hit:
            self.hp -= 1
            if not self.hp:
                self.isAlive = False

    def update(self, player):
        # if not self.isAlive and self.timer["dead"].active:
        #     self.
        
        screen_size = pygame.display.get_surface().get_size()
        
        if ((0 <= self.rect.x <= screen_size[0]) and 
            (0 <= self.rect.y <= screen_size[1])):

            if self.hp < 0:
                self.isAlive = False

            dx = player.rect.centerx - self.rect.centerx
            dy = player.rect.centery - self.rect.centery
            distance = math.sqrt(dx**2 + dy**2) 

            if distance > 0: 
                dx /= distance
                dy /= distance

            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed