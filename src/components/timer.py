import pygame
import logging

class Timer:
    def __init__(self, duration: int):
        
        """
        init for timer class
        duration: how long
        func: what function to execute
        first: if you want to execute it before the timer
        """
        
        self.duration = duration
        self.start_time = 0
        self.active = False


    def activate(self):
        self.active = True
        self.start_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start_time = 0

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= self.duration:
            self.deactivate()   
