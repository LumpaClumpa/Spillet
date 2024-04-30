import pygame
import os

pygame.init()

from Player import PlayerClass

from Enemy import EnemyClass


from random import randint as rando
clock = pygame.time.Clock()




enemies=[]

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

enemyMaxSpeed = 15
number_of_enemies = 5
def spawnEnemy():
    enemies.append(EnemyClass(surface,
                              spawnPosX=rando(0, gameWindowWidth),
                              spawnPosY=rando(0, gameWindowHeight),
                              speedX=rando(-enemyMaxSpeed, enemyMaxSpeed),
                              speedY=rando(-enemyMaxSpeed, enemyMaxSpeed))
                   )


for i in range(number_of_enemies):
    spawnEnemy()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    playerObject.update()

    for enemy in enemies:
        enemyIsDead = False
        enemy.update()
        if enemy.x>gameWindowWidth or enemy.y>gameWindowHeight or enemy.x<0 or enemy.y<0:
            enemyIsDead=True

        if enemyIsDead:
            enemies.remove(enemy)
            spawnEnemy()

    surface.fill((0, 0, 0))
    playerObject.draw()

    for enemy in enemies:
        enemy.draw()

    clock.tick(60)

    display.blit(pygame.transform.scale(surface, (gameWindowWidth, gameWindowHeight)), (0, 0))
    pygame.display.flip()
