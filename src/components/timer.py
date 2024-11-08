import pygame
import logging

class Timer:
    def __init__(self, duration: int):
        
        """
        init for timer class
        duration: how long
        func: what function to execute
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

class Stopwatch(Timer):
    def __init__(self, duration):
        super().__init__(duration)
        
class UntilTimer(Timer):

    def __init__(self, until: bool = True):
        """
        Init for UntilTimer
        """
        super().__init__(duration=0)
        self.until = until

    def activate(self):
        self.active = True

    def update(self, finished: bool = False):
        if finished:
            self.active = False