import pygame
import math

class PlayerClass:
    maxSpeed=5
    width=50
    height=50
    color=(0, 128, 255)
    points=0




    def __init__(self,screen,xpos,ypos):#,terrainCollection):
        self.x=xpos
        self.y=ypos
        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0] #
        self.screenHeight = self.theScreen.get_size()[1]

    def update(self):
        up = pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]
        down = pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]
        left = pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]
        right = pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]

        self.y += round((-self.maxSpeed if not left ^ right else (-math.sqrt(2)/2) * self.maxSpeed) if up and not down else ((self.maxSpeed if not left ^ right else (math.sqrt(2)/2) * self.maxSpeed) if not up and down else 0))
        self.x += round((-self.maxSpeed if not up ^ down else (-math.sqrt(2)/2) * self.maxSpeed) if left and not right else ((self.maxSpeed if not up ^ down else (math.sqrt(2)/2) * self.maxSpeed) if not left and right else 0))


        if self.x+self.width > self.screenWidth:
            self.x = self.screenWidth-self.width
        if self.y+self.height > self.screenHeight:
            self.y = self.screenHeight-self.height
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
