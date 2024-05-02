import pygame

class Lawn:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.lawn = [[0 for i in range(width)] for j in range(height)]

    def draw(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.lawn[j][i] == 0:
                    pygame.draw.rect(self.screen, (34, 97, 0), pygame.Rect(i*10, j*10, 10, 10))
                else:
                    pygame.draw.rect(self.screen, (89, 255, 0), pygame.Rect(i*10, j*10, 10, 10))

    def update(self, playerObject):
        for i in range(self.width):
            for j in range(self.height):
                if self.lawn[j][i] == 0:
                    if playerObject.x + playerObject.width > i * 10 and playerObject.x < i * 10 + 10 and playerObject.y + playerObject.height > j * 10 and playerObject.y < j * 10 + 10:
                        self.lawn[j][i] = 1