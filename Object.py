import pygame

# TODO rewrite to support rendering sprites instead of colours
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

    def draw(self):
        if hasattr(self, 'radius'):
            pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)
        else:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))