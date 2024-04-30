from Object import Object
import pygame
import math

class Player(Object):
    speed=5

    def __init__(self, screen, x, y):
        super().__init__(screen, x, y, (0, 128, 255), 50, 50)

    def update(self):
        up = pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]
        down = pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]
        left = pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]
        right = pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]

        self.y += round((-self.speed if not left ^ right else (-math.sqrt(2) / 2) * self.speed) if up and not down else ((self.speed if not left ^ right else (math.sqrt(2) / 2) * self.speed) if not up and down else 0))
        self.x += round((-self.speed if not up ^ down else (-math.sqrt(2) / 2) * self.speed) if left and not right else ((self.speed if not up ^ down else (math.sqrt(2) / 2) * self.speed) if not left and right else 0))

        if self.x+self.width > self.screen.get_size()[0]:
            self.x = self.screen.get_size()[0]-self.width
        if self.y+self.height > self.screen.get_size()[1]:
            self.y = self.screen.get_size()[1]-self.height
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0