import pygame
from Object import Object

class Player(Object):
    def __init__(self, display):
        super().__init__(display, 2, 2, pygame.image.load('assets/player.png'))

    def draw(self):
        super().draw(0, 0)
        #self.display.blit(pygame.transform.scale(self.image, (40, 40)), (self.x + (self.display.get_width()/2 - 2), self.y + (self.display.get_height()/2 - 2)))