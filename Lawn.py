import pygame
import gameFunctions


def pos(i, j, playerObject):
    return [i * 10 + playerObject.x/2, j * 10 + playerObject.y/2]

class Lawn:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.lawn = [[0 for i in range(width)] for j in range(height)]

    def draw(self, player):
        for i in range(self.width):
            for j in range(self.height):
                if self.lawn[j][i] == 0:
                    pygame.draw.rect(self.screen, (65, 152, 10), pygame.Rect(pos(i, j, player)[0], pos(i, j, player)[1], 10, 10))
                else:
                    pygame.draw.rect(self.screen, (19, 133, 16), pygame.Rect(pos(i, j, player)[0], pos(i, j, player)[1], 10, 10))

    def update(self, player):
        for i in range(self.width):
            for j in range(self.height):
                if self.lawn[j][i] == 0:
                    if gameFunctions.collisionChecker(960 - player.width/2, 540 - player.height/2, player.width, player.height, pos(i, j, player)[0], pos(i, j, player)[1], 10, 10):
                        self.lawn[j][i] = 1