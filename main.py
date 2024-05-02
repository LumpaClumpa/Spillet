import pygame
from Player import Player

pygame.init()
pygame.font.init()
best_font = pygame.font.SysFont('Comic Sans MS', 24)
clock = pygame.time.Clock()

gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
surface = pygame.Surface((1920, 1080))
display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))

playerObject = Player(surface, 100, 100)
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
    text_surface = best_font.render('Highscore:', False, (255, 255, 255))


    clock.tick(60)

    display.blit(pygame.transform.scale(surface, (gameWindowWidth, gameWindowHeight)), (0, 0))
    display.blit(text_surface, (10, 10))
    pygame.display.flip()
