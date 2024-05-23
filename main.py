import math
import pygame
from Player import Player
from Button import Button
from Coin import Coin
import random

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('', 42)
clock = pygame.time.Clock()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

button_surface = pygame.Surface((120, 92))
background = pygame.Surface((1920, 1080))

lawnSize = (120, 120)
lawn = pygame.Surface(lawnSize)
lawn.fill((65, 152, 10))

playerObject = Player(display)

coins = []
coinCount = 0


def spawnCoin(amount=1):
    coinImage = pygame.image.load('assets/coin.png')
    for x in range(amount):
        coins.append(Coin(display, random.randint(1, lawn.get_width()*10 - coinImage.get_width()), random.randint(1, lawn.get_height()*10 - coinImage.get_height()), coinImage))


def removeCoin(i):
    coins.pop(i)


spawnCoin(math.ceil(lawnSize[0] * lawnSize[1] / 1000))

imageIdleShop = pygame.transform.scale(pygame.image.load('assets/shop_icon1.png'), (70, 60))
imageHoverShop = pygame.transform.scale(pygame.image.load('assets/shop_icon2.png'), (70, 60))
imageGrass = pygame.transform.scale(pygame.image.load('assets/grass_image.jpg'), (160, 50))

imageShopmenu = pygame.transform.scale(pygame.image.load('assets/MOWER_SHOP.png'), (700, 550))

shopbutton = Button(display, 0, 0, imageIdleShop, imageHoverShop)
lawnupgrade = Button(display, display.get_width()/2 - 303, display.get_height()/2 - 100, imageGrass, imageGrass)

shop_open = False
def draw_shop(surface):
    surface.blit(imageShopmenu, (display.get_width()/2 - imageShopmenu.get_width()/2, display.get_height()/2 - imageShopmenu.get_height()/2))
    lawnupgrade.draw()

speed, x, y = 1, 0, 0

frameCount = 0
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if shopbutton.isOver(pygame.mouse.get_pos()):
                shop_open = not shop_open

            if lawnupgrade.isOver(pygame.mouse.get_pos()) and shop_open:
                lawnSize = (25, 25) #this is a test

    if frameCount % 2 == 0 and not shop_open:
        up = pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_w]
        down = pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_s]
        left = pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_a]
        right = pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_d]

        y += round((-speed if not left ^ right else (-math.sqrt(0.5)) * speed) if up and not down else ((speed if not left ^ right else (math.sqrt(0.5)) * speed) if not up and down else 0))
        x += round((-speed if not up ^ down else (-math.sqrt(0.5)) * speed) if left and not right else ((speed if not up ^ down else (math.sqrt(0.5)) * speed) if not left and right else 0))

    if x < -10:
        x = -10

    if x + 4 > lawn.get_width() + 10:
        x = lawn.get_width() + 10 - 4

    if y < -10:
        y = -10

    if y + 4 > lawn.get_height() + 10:
        y = lawn.get_height() + 10 - 4

    coinsText = font.render('Coins: ' + str(coinCount), False, (255, 255, 255))

    clock.tick(60)
    frameCount += 1

    display.blit(background, (0, 0))

    pygame.draw.rect(lawn, (19, 133, 16), pygame.Rect(x, y, 4, 4))
    region = ((x*10 - pygame.display.get_window_size()[0] / 2, y*10 - pygame.display.get_window_size()[1] / 2), pygame.display.get_window_size())
    lawn = pygame.transform.scale(lawn, (lawnSize[0]*10, lawnSize[1]*10))
    lawn.set_clip(region)
    display.blit(lawn, (0, 0), region)
    lawn = pygame.transform.scale(lawn, lawnSize)

    playerObject.draw()

    for coin in coins:
        if coin.update(x, y):
            coinCount += 1
            removeCoin(coins.index(coin))
        coin.draw(x, y)

    shopbutton.draw()

    if shop_open:
        draw_shop(pygame.display.get_surface())

    display.blit(coinsText, (75, 18))
    pygame.display.update()
