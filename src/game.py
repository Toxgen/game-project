from sys import exit

import pygame
import logging

class EventHandler():
    def __init__(self):
        """
        Initalizes the Event Handler
        Handles Events duh

        notes: handle userInput and whatever is happening on map ig
        """
        pass

    def idk():
        pass
class Game(EventHandler):
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
        }

        #just have to check what map it is
    
    def evnt(self, plrFlags, dt) -> None:
        """
        return None
        loops through events that i made, not pygame
        """
        if plrFlags: # do we need len?
            self.flags["transition"] = True

        for event in self.events.values():
            if event.__name__ == "transition":

                logging.info("transitioning rn")
                try:
                    if self.flags["transition"] and not event.transitioning:
                        event.update(dt)
                        #should save after probably
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
                    logging.info("mouse is down")

                else:
                    for events in self.keys:
                        self.keys[events] = False

            dt = self.clock.tick(60) / 1000

            plrInfo = self.level.run(dt, self.keys, self.flags)

            self.evnt(plrInfo, dt)
 
            pygame.display.update()

if __name__ == "__main__":
    pass
