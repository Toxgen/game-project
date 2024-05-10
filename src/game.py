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
        self.flags = {
            "transition": False,
            "teleportation": False
        }

        #just have to check what map it is
    
    def evnt(self, plrFlags, mapInfo, dt) -> None:
        """
        return None
        loops through events that i made, not pygame
        """
        if plrFlags:
            self.flags["teleportation"]

        for event in self.events.items():

            if event.value == "teleportation" and self.flags["teleportation"]: # check if it collidrect with the thig
                pass
                # uhhh it has to transition than load the island
            if event.value == "transition":
                logging.info("transitioning rn")
                try:
                    if event.transition:
                        event.update(dt)
                        #should save after probably
                        # reset flags
                except Exception as e:
                    logging.log(logging.WARNING, f"transition fail msg: {e}")
                    raise Exception
        else:
            for flag in self.flags:
                self.flags[flag] = False
            

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

            plrInfo, mapInfo = self.level.run(dt, self.keys, self.flags)

            self.evnt(plrInfo, mapInfo, dt)
 
            pygame.display.update()
            
if __name__ == "__main__":
    pass
