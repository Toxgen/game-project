from sys import exit

import pygame
import logging

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1152, 704))
        self.clock = pygame.time.Clock()
        self.events = {
            "mouse_down": False,
        }
        
        from src.level import Level
        self.level = Level

        from src.components.transition import Transition
        self.transition = Transition

        self.level.map_prop = None # ??

        # the map props class gives me the props things
        # so like just check if the player is in the _map_props things
        # i think i meant by if the player is in the x and y cords?
    
    @staticmethod
    def evnt(cls, info):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.level.save()
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.events["mouse_down"] = True
                    logging.info(f"mouse is down")

                else:
                    for events in self.events:
                        self.events[events] = False

            dt = self.clock.tick(60) / 1000
            (player, info) = self.level.run(dt, self.events)

            Game.evnt(player, info)
 
            pygame.display.update()
            
if __name__ == "__main__":
    pass
    # TODO test out the transitions along side with the map_props var, use the if in game.py
