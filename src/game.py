from sys import exit

import pygame
import logging

class Game:
    def __init__(self):
        """
        initalize game class
        sets screen
        the clock
        keys and level and events
        """
        pygame.init()
        self.screen = pygame.display.set_mode((1152, 704))
        self.clock = pygame.time.Clock()
        self.keys = {
            "mouse_down": False,
        }
        
        from src.level import Level
        self.level = Level()

        from src.components.transition import Transition
        self.events = {
            "transitioning": Transition(),
        }
        


        # the map props class gives me the props things
        # so like just check if the player is in the _map_props things
        # i think i meant by if the player is in the x and y cords?
    
    def evnt(self, plr, info) -> None:
        """
        return None
        loops through events that i made, not pygame
        """
        info = info.get()
        for event in self.events:

            if event.type() == "teleportation":
                pass
                # uhhh it has to transition than load the island
            if event.type() == "transition":
                while event.transition:
                    event.update()
                    #should save after probably
            

    def run(self) -> None:
        """
        returns none
        main running function that holds all components
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.level.save()
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.keys["mouse_down"] = True
                    logging.info(f"mouse is down")

                else:
                    for events in self.keys:
                        self.keys[events] = False

            dt = self.clock.tick(60) / 1000
            (player, info) = self.level.run(dt, self.keys)

            Game.evnt(player, info)
 
            pygame.display.update()
            
if __name__ == "__main__":
    pass
    # TODO test out the transitions along side with the map_props var, use the if in game.py
