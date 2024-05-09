import pygame
import logging
import os
class Transition:
    def __init__(self) -> None:
        """
        init for transition
        """
        self.screen = None

        self.overlay = pygame.Surface((pygame.display.get_window_size()))
        self.display = pygame.display.get_surface()
        self.transitioning = True

        self.size = 16
        self.rects = []

        self.speed = 1
        self.width = 4
        self.height = 4
        self.final = False

        for x in range(36):
            for y in range(22):
                self.rects.append(pygame.Rect((x*32 - 10, y*32 - 10), (4, 4)))

    def type(self) -> str:
        """
        returns class type
        depracted, whats the point??
        """
        return "transition"


    def update(self, dt) -> None:
        """
        updates screen periodically
        """
        self.overlay.fill((0, 0, 0))
        self.display.blit(self.overlay, (0, 0))

        if self.final:
            self.width += (self.width * -dt - 0.1)
            self.height += (self.width * -dt - 0.1)

        else:
            self.width += (self.width * self.speed * dt)
            self.height += (self.width * self.speed * dt)

        # logging.log(50, f"speed: {self.speed}, width: {self.width}")
        # logging.log(50, f"after: {self.width}")
        # logging.log(logging.INFO, msg="transitioning")

        for rect in self.rects:
            rect.width = self.width
            rect.height = self.height
            self.display.fill("red", rect)

        if self.width < 44:
            self.speed += 0.0001 
        else:
            self.final = True            

        self.finished()

    def finished(self):
        """
        checks if transition has finished
        restarts it back to original setting
        """
        if self.width < 0 and self.final:
            self.transitioning = False
            self.final = False
            self.speed = 0
            self.width = 0
            self.height = 0
            logging.log(logging.INFO, msg="finished transitioning")

if __name__ == "__main__":
    # testing
    try:  
        path = r"C:\Users\yao\OneDrive\Documents/vscode-src\game-project"
        handler = logging.FileHandler(os.path.join(path, '_logging/_logs.log'))

    except Exception:
        logging.log(level=40, msg="Logging defining went wrong")

    finally:
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)

    Transition.screen = pygame.display.set_mode((1152, 704))
    test = Transition()
    clock = pygame.time.Clock()

    while test.transitioning:
        dt = clock.tick(60) / 1000
        test.update(dt)
        pygame.display.update()
else:
    Transition.screen = pygame.display.get_surface()
