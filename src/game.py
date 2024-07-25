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

        #just have to check what map it is       

    def run(self) -> None:
        """
        returns none
        main running function that holds all components
        """
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        self.level.save()
                        pygame.quit()
                        exit()
                    except Exception as e:
                        logging.log(logging.CRITICAL, f"ESCAPING ERROR {e}")

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
