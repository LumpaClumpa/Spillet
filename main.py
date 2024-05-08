from Player import Player
from Lawn import Lawn
import pygame
import math
import pygame
from Lawn import Lawn
from Player import Player

pygame.init()
pygame.font.init()
best_font = pygame.font.SysFont('MinecraftRegular', 35)
clock = pygame.time.Clock()
img = pygame.image.load('assets/shoppingcart_icon.png')

default_image_size = (70, 60)
img = pygame.transform.scale(img, default_image_size)

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
surface = pygame.Surface((1920, 1080))
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

playerObject = Player(surface)
lawn = Lawn(surface, 192, 108)

speed, x, y = 7, 0, 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    up = pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]
    down = pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]
    left = pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]
    right = pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]

    y += round((-speed if not left ^ right else (-math.sqrt(0.5)) * speed) if up and not down else ((speed if not left ^ right else (math.sqrt(0.5)) * speed) if not up and down else 0))
    x += round((-speed if not up ^ down else (-math.sqrt(0.5)) * speed) if left and not right else ((speed if not up ^ down else (math.sqrt(0.5)) * speed) if not left and right else 0))

    lawn.update(playerObject, [x, y])

    surface.fill((0, 0, 0))
    lawn.draw([x, y])
    playerObject.draw([x, y])

    text_surface = best_font.render('Coins:', False, (255, 255, 255))

    clock.tick(60)

    display.blit(pygame.transform.scale(surface, (gameWindowWidth, gameWindowHeight)), (0, 0))
    display.blit(text_surface, (70, 10))
    display.blit(img, (2, 2))
    pygame.display.flip()
