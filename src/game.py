from sys import exit

import pygame
import logging

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1152, 704))
        self.clock = pygame.time.Clock()
        self.events = {
            "mouse_down": False
        }
        
        from src.level import Level
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.level.save()
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.events["mouse_down"] == True
                    logging.info(f"mouse is down")
                    

                else:
                    self.events["mouse_down"] == False

            dt = self.clock.tick(60) / 1000
            self.level.run(dt, self.events)
            pygame.display.update()
            
if __name__ == "__main__":
    pass