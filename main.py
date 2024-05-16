import math
import pygame
from Player import Player
from Button import Button
from Coin import Coin

pygame.init()
pygame.font.init()
best_font = pygame.font.SysFont('MinecraftRegular', 35)
clock = pygame.time.Clock()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

button_surface = pygame.Surface((120, 92))
background = pygame.Surface((1920, 1080))
lawn = pygame.Surface((800, 800))
lawn.fill((65, 152, 10))

playerObject = Player(display)
coin = Coin(display, 100, 100)

imageIdle = pygame.transform.scale(pygame.image.load('assets/shop_icon1.png'), (70, 60))
imageHover = pygame.transform.scale(pygame.image.load('assets/shop_icon2.png'), (70, 60))

shopbutton = Button(display, 0, 0, imageIdle, imageHover)

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

    y += round((-speed if not left ^ right else (-math.sqrt(0.5)) * speed) if up and not down else ((speed if not left ^ right else (math.sqrt(0.5)) * speed) if not up and down else 0))
    x += round((-speed if not up ^ down else (-math.sqrt(0.5)) * speed) if left and not right else ((speed if not up ^ down else (math.sqrt(0.5)) * speed) if not left and right else 0))

    if x < -200:
        x = -200

    if x + 50 > lawn.get_width() + 200:
        x = lawn.get_width() + 200 - 50

    if y < -200:
        y = -200

    if y + 50 > lawn.get_height() + 200:
        y = lawn.get_height() + 200 - 50

    text_surface = best_font.render('Coins: ', False, (255, 255, 255))

    clock.tick(60)

    display.blit(background, (0, 0))

    pygame.draw.rect(lawn, (19, 133, 16), pygame.Rect(x, y, 50, 50))
    region = ((x - pygame.display.get_window_size()[0] / 2, y - pygame.display.get_window_size()[1] / 2), pygame.display.get_window_size())
    lawn.set_clip(region)
    display.blit(lawn, (0, 0), region)

    coin.update(x, y)

    coin.draw(x, y)
    playerObject.draw()

    shopbutton.draw()

    display.blit(text_surface, (70, 10))
    pygame.display.update()
