import pygame
from Player import PlayerClass
from random import randint as rando

pygame.init()
clock = pygame.time.Clock()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
surface = pygame.Surface((1920, 1080))
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

playerObject = PlayerClass(surface, xpos=100, ypos=100)
def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and\
                firstGameObject.x < secondGameObject.x + secondGameObject.width and\
                firstGameObject.y + firstGameObject.height > secondGameObject.y and\
                firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True
        return False

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    playerObject.update()

    surface.fill((0, 0, 0))
    playerObject.draw()

    clock.tick(60)

    display.blit(pygame.transform.scale(surface, (gameWindowWidth, gameWindowHeight)), (0, 0))
    pygame.display.flip()
