from sys import exit

import pygame


from src.constants import screen_dim
from src.level import Level

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_dim)
        self.clock = pygame.time.Clock
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.level()
            dt = self.clock.tick() / 1000
            pygame.display.update()
            
if __name__ == "__main__":
    pass