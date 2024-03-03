import pygame

class Transition:
    def __init__(self):
        self.width, self.height = pygame.display.get_window_size()
        self.display = pygame.display.get_surface()
        self.transitioning = True
        self.touched = False

        self.size = 32
        self.amount = 22

        self.rects = []

        for i in range(self.amount):
            self.rects.append(pygame.Rect(0, i*32), 32, 32)

        self.speed = 300

        self.move_r = 0
        self.move_l = 0

    def update(self, dt):

        self.move_r += self.speed * dt
        self.move_l -= -self.speed * dt

        for rect in self.rects:
            pygame.rect.draw(self.display, (255, 255, 255), 0)

            rect.move_ip(self.move_r, 0)

        self.finished()

    def finished(self):
        if self.rects[0].left > self.width:
            self.touched = True

        if self.rects[-1].left() > self.width and self.touched:
            self.transitioning = False

if __name__ == "__main__":
    pass