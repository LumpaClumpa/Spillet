import pygame

class Object:
    def __init__(self, screen : pygame.surface.SurfaceType, x, y, color, radiusOrWidth, height=0):
        self.screen = screen
        self.x = x + (screen.get_width()/2 - 25) # 25 is half of player width
        self.y = y + (screen.get_height()/2 - 25) # 25 is half of player height
        self.color = color
        if height == 0:
            self.radius = radiusOrWidth
        else:
            self.width = radiusOrWidth
            self.height = height

    def draw(self, shift):
        if hasattr(self, 'radius'):
            pygame.draw.circle(self.screen, self.color, (self.x - shift[0], self.y - shift[1]), self.radius)
        else:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x - shift[0], self.y - shift[1], self.width, self.height))