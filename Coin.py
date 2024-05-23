import pygame

import gameFunctions
from Object import Object
class Coin(Object):
    def __init__(self, display, x, y, image):
        super().__init__(display, x, y, image)

    def update(self, x, y):
        return gameFunctions.collisionChecker((self.x, self.y), (35, 35), (x*10, y*10), (40, 40))