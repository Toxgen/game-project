import pygame
import logging
class Timer:
    def __init__(self, duration, 
                 first=False, func=None):
        
        self.duration = duration
        self.func = func
        self.first = first
        self.start_time = 0
        self.active = False


    def activate(self):
        if self.first:
            self.func()

        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.deactivate()   
            if self.func and not self.first:
                self.func()