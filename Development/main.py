import sys
import pygame
from pygame.locals import *
from Link import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

CLOCK   = pygame.time.Clock()
FPS     = 60

BG = [0, 0, 0]

IS_RUNNING = True


playerSprite = pygame.image.load("./Art/spr_Player.png")
playerRect = playerSprite.get_rect()
playerStats = Link(3, 20, 5, 3)



while IS_RUNNING:


    # ------------------------------------------------
    # INPUT REGISTRATION:
    # ------------------------------------------------
    KEYS_DOWN = pygame.key.get_pressed()


    # ------------------------------------------------
    # EVENT HANDLING:
    # ------------------------------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            IS_RUNNING = False


    # ------------------------------------------------
    # UPDATE GAME LOGIC:
    # ------------------------------------------------
    if (KEYS_DOWN[K_UP]):
        playerRect.y -= playerStats.playerSpeed
    elif (KEYS_DOWN[K_DOWN]):
        playerRect.y += playerStats.playerSpeed

    if (KEYS_DOWN[K_LEFT]):
        playerRect.x -= playerStats.playerSpeed
    elif (KEYS_DOWN[K_RIGHT]):
        playerRect.x += playerStats.playerSpeed

    if (KEYS_DOWN[K_9]):
        BG = [255, 255, 255]
    elif (KEYS_DOWN[K_8]):
        BG = [34, 34, 34]
    
    if playerRect.y > 590:
        playerRect.y = 590
    elif playerRect.y < -25:
        playerRect.y = -25

    if playerRect.x > 590:
        playerRect.x = 590
    elif playerRect.x < -25:
        playerRect.x = -25


    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    SCREEN.fill(BG)

    # Then draw sprites on the current location:
    SCREEN.blit(playerSprite, playerRect)
    
    # Finally refresh the entire screen of this application window:
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
