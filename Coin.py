import pygame

import gameFunctions
from Object import Object
class Coin(Object):
    def __init__(self, display, x, y):
        super().__init__(display, x, y, pygame.image.load('assets/coin.png'))

    def update(self, x, y):
        return gameFunctions.collisionChecker((self.x, self.y), (35, 35), (x, y), (50, 50))