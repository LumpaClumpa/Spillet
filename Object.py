import pygame

# TODO rewrite to support rendering sprites instead of colours
class Object:
    def __init__(self, screenWidth, screenHeight, display, x, y, image):
        self.display = display
        self.x = x + (screenWidth/2 - 25) # 25 is half of player width
        self.y = y + (screenHeight/2 - 25) # 25 is half of player height
        self.image = image

    def draw(self, x, y):
        self.display.blit(self.image, (self.x - x, self.y - y))