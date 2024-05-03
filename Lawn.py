import pygame
import gameFunctions

def pos(i, j, shift):
    return [i * 10 - shift[0], j * 10 - shift[1]]

class Lawn:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.lawn = [[False for i in range(width)] for j in range(height)]

    def draw(self, shift):
        for i in range(self.width):
            for j in range(self.height):
                pygame.draw.rect(self.screen, (65, 152, 10) if self.lawn[j][i] == 0 else (19, 133, 16), pygame.Rect(pos(i, j, shift)[0], pos(i, j, shift)[1], 10, 10))

    def update(self, player, shift):
        for i in range(self.width):
            for j in range(self.height):
                if not self.lawn[j][i]:
                    self.lawn[j][i] = gameFunctions.collisionChecker([player.x, player.y], [player.width, player.height], pos(i, j, shift), [10, 10])