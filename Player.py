import pygame.surface
from Object import Object

class Player(Object):
    def __init__(self, display : pygame.Surface):
        super().__init__(display.get_width(), display.get_height(), display, 25, 25, pygame.image.load('assets/player.png'))

    def draw(self):
        super().draw(0, 0)