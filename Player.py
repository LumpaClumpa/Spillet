import pygame.surface

from Object import Object

img2 = pygame.image.load('assets/player.png')

class Player(Object):
    def __init__(self, display : pygame.Surface):
        super().__init__(display.get_width(), display.get_height(), display, 25, 25, img2)

    def draw(self):
        super().draw(0, 0)