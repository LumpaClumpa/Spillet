import pygame
from Object import Object

class Player(Object):
    def __init__(self, display):
        super().__init__(display, 25, 25, pygame.image.load('assets/player.png'))

    def draw(self):
        super().draw(0, 0)