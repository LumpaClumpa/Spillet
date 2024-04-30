import pygame

class Object:
    def __init__(self, screen, x, y, color, radiusOrWidth, height=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        if height == 0:
            self.radius = radiusOrWidth
        else:
            self.width = radiusOrWidth
            self.height = height

    def draw (self):
        if hasattr(self, 'radius'):
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        else:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))