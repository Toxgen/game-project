from sys import exit

import pygame


from constants import screen_x, screen_y

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_x, screen_y)
        self.clock = pygame.time.Clock
        #self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            dt = self.clock.tick() / 1000
            pygame.display.update()
if __name__ == "__main__":
    pygame.init()

