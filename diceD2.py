import random
import pygame


DICE_WIDTH = 120
DICE_LENGTH = 120

def dice_roll():
    return random.randint(1,6)

diceroll = dice_roll()


def  dice_animations(diceroll, images, windowSurface, dice_coordinates):
    for i in range(20):
        pygame.time.delay(100)
        windowSurface.blit(images[i % 6], dice_coordinates)
        pygame.display.update()
    windowSurface.blit(images[diceroll-1], dice_coordinates)
    pygame.display.update()

images = [1] * 6

images[0] = pygame.image.load('assets/dot1.png')
images[1] = pygame.image.load('assets/dot2.png')
images[2] = pygame.image.load('assets/dot3.png')
images[3] = pygame.image.load('assets/dot4.png')
images[4] = pygame.image.load('assets/dot5.png')
images[5] = pygame.image.load('assets/dot6.png')

images[0] = pygame.transform.scale(images[0], (DICE_WIDTH, DICE_LENGTH))
images[1] = pygame.transform.scale(images[1], (DICE_WIDTH, DICE_LENGTH))
images[2] = pygame.transform.scale(images[2], (DICE_WIDTH, DICE_LENGTH))
images[3] = pygame.transform.scale(images[3], (DICE_WIDTH, DICE_LENGTH))
images[4] = pygame.transform.scale(images[4], (DICE_WIDTH, DICE_LENGTH))
images[5] = pygame.transform.scale(images[5], (DICE_WIDTH, DICE_LENGTH))




