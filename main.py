import math
import pygame
from Player import Player
from buttonClass import button

pygame.init()
pygame.font.init()
best_font = pygame.font.SysFont('MinecraftRegular', 35)
clock = pygame.time.Clock()
img = pygame.image.load('assets/shoppingcart_icon.png')

default_image_size = (70, 60)
img = pygame.transform.scale(img, default_image_size)

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

button_surface = pygame.Surface((120, 92))
player_surface = pygame.Surface((50, 50))
background = pygame.Surface((1920, 1080))
lawn = pygame.Surface((800, 800))
lawn.fill((65, 152, 10))

playerObject = Player(player_surface)

shopbutton = button((50, 50, 50), 0, 0, 120, 92, '')

speed, x, y = 7, 0, 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if shopbutton.isOver(pygame.mouse.get_pos()):
                print('clicked the button')

    up = pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]
    down = pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]
    left = pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]
    right = pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]

    playerObject.y += round((-speed if not left ^ right else (-math.sqrt(0.5)) * speed) if up and not down else ((speed if not left ^ right else (math.sqrt(0.5)) * speed) if not up and down else 0))
    playerObject.x += round((-speed if not up ^ down else (-math.sqrt(0.5)) * speed) if left and not right else ((speed if not up ^ down else (math.sqrt(0.5)) * speed) if not left and right else 0))

    if playerObject.x < -200:
        playerObject.x = -200

    if playerObject.x + playerObject.width > lawn.get_width() + 200:
        playerObject.x = lawn.get_width() + 200 - playerObject.width

    if playerObject.y < -200:
        playerObject.y = -200

    if playerObject.y + playerObject.height > lawn.get_height() + 200:
        playerObject.y = lawn.get_height() + 200 - playerObject.height

    playerObject.draw()
    shopbutton.draw(button_surface)

    text_surface = best_font.render('Coins: ', False, (255, 255, 255))

    clock.tick(60)

    clock.tick(30)

    display.blit(background, (0, 0))

    pygame.draw.rect(lawn, (19, 133, 16), pygame.Rect(playerObject.x, playerObject.y, 50, 50))
    region = ((playerObject.x - pygame.display.get_window_size()[0] / 2, playerObject.y - pygame.display.get_window_size()[1] / 2), pygame.display.get_window_size())
    lawn.set_clip(region)
    display.blit(lawn, (0, 0), region)

    display.blit(player_surface, (pygame.display.get_window_size()[0] / 2, pygame.display.get_window_size()[1] / 2))
    display.blit(button_surface, (0, 0))

    display.blit(text_surface, (70, 10))
    display.blit(img, (2, 2))
    pygame.display.update()
