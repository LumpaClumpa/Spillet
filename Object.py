import pygame

# TODO rewrite to support rendering sprites instead of colours
class Object:
    def __init__(self, screenHeight, screenWidth, display, x, y, image, size):
        self.display = display
        self.x = x + (screenWidth/2 - 25) # 25 is half of player width
        self.y = y + (screenHeight/2 - 25) # 25 is half of player height
        self.image = image
        self.size = size

    def draw(self):
        self.display.blit(self.image, (self.x, self.y))