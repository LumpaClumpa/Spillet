import pygame
from Player import Player
from Lawn import Lawn

pygame.init()
pygame.font.init()
best_font = pygame.font.SysFont('Comic Sans MS', 24)
clock = pygame.time.Clock()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
surface = pygame.Surface((1920, 1080))
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

playerObject = Player(surface, 0, 0)
lawn = Lawn(surface, 192, 108)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    playerObject.update()
    lawn.update(playerObject)

    surface.fill((0, 0, 0))
    lawn.draw(playerObject)
    playerObject.draw()

    text_surface = best_font.render('Highscore:', False, (255, 255, 255))

    clock.tick(60)

    display.blit(pygame.transform.scale(surface, (gameWindowWidth, gameWindowHeight)), (0, 0))
    display.blit(text_surface, (10, 10))
    pygame.display.flip()
