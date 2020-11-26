import sys
import pygame
from pygame.locals import *
from Link import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
ICON = pygame.image.load("./Art/windowIcon.png")
pygame.display.set_icon(ICON)
pygame.display.set_caption("")
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN  = pygame.display.set_mode(SCREEN_SIZE)

# Background Image Drawn over the screenfill
BACKGROUND = pygame.image.load('./Art/backgroundSpr.png')

# Background Music
MUSICPATH = "./Art/songs/ost3.mp3"
pygame.mixer.init()
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.load(MUSICPATH)
pygame.mixer.music.play()


MaxX = SCREEN_WIDTH - 10
MinX = SCREEN_WIDTH - (SCREEN_WIDTH + 25)
MaxY = SCREEN_HEIGHT - 10
MinY = SCREEN_HEIGHT - (SCREEN_HEIGHT + 25)

CLOCK   = pygame.time.Clock()
FPS     = 60

BG = [0, 0, 0]

IS_RUNNING = True


playerSprite = pygame.image.load("./Art/spr_Player.png")
playerRect = playerSprite.get_rect()
playerStats = Link(3, 20, 5, 3)

vel_x = 10
vel_y = 10
jump = False



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
    if (KEYS_DOWN[K_UP]) or (KEYS_DOWN[K_w]):
        playerRect.y -= playerStats.playerSpeed
    elif (KEYS_DOWN[K_DOWN]) or (KEYS_DOWN[K_s]):
        playerRect.y += playerStats.playerSpeed

    if (KEYS_DOWN[K_LEFT]) or (KEYS_DOWN[K_a]):
        playerRect.x -= playerStats.playerSpeed
    elif (KEYS_DOWN[K_RIGHT]) or (KEYS_DOWN[K_d]):
        playerRect.x += playerStats.playerSpeed

    
    if playerRect.y > MaxY:
        playerRect.y = MaxY
    elif playerRect.y < MinY:
        playerRect.y = MinY

    if playerRect.x > MaxX:
        playerRect.x = MaxX
    elif playerRect.x < MinX:
        playerRect.x = MinX

    if jump is False and (KEYS_DOWN[K_SPACE]):
        jump = True

    if jump is True:
        playerRect.y -= vel_y
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    SCREEN.fill(BG)
    # Background Image
    SCREEN.blit(BACKGROUND,(0,0))
    # Then draw sprites on the current location:
    SCREEN.blit(playerSprite, playerRect)
    
    # Finally refresh the entire screen of this application window:
    pygame.display.flip()


    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
