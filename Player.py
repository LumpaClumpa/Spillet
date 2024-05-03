import pygame
from Object import Object

class Player(Object):
    def __init__(self, screen):
        super().__init__(screen, 0, 0, (0, 128, 255), 50, 50)

    def draw(self, shift):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))