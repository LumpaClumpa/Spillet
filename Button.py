#En class der gør sådan at man kan lave knapper - der er taget inspiration fra nettet

import pygame

class Button():
    def __init__(self, display, x, y, imageIdle, imageHover):
        self.display = display
        self.x = x
        self.y = y
        self.imageIdle = imageIdle
        self.imageHover = imageHover

    def draw(self):
        pos = pygame.mouse.get_pos()

        if self.isOver(pos):
            image = self.imageHover
        else:
            image = self.imageIdle

        self.display.blit(image, (self.x, self.y))

    def isOver(self, pos):
        #Checker om musen er over knappen
        if pos[0] > self.x and pos[0] < self.x + self.imageIdle.get_width():
            if pos[1] > self.y and pos[1] < self.y + self.imageIdle.get_height():
                return True

        return False