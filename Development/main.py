import sys, pygame, json
from pygame.locals import *
from Link import *
from spritesheet import Spritesheet

# Necessary setup before you can start using pygame functionalities:
pygame.init()


KEYS_DOWN = []

# Pygame Window Settings
SCREEN_WIDTH, SCREEN_HEIGHT = 720, 720
ICON = pygame.image.load("./Art/windowIcon.png")
pygame.display.set_icon(ICON)
pygame.display.set_caption("Legend of Zelda in the making")
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

# Boundaries of the screen so the player can't go off screen
# Done with the width of the window, so it can be used flexibly and when the window size changes it doesn't have to be changed manually.
MaxX = SCREEN_WIDTH - 10
MinX = SCREEN_WIDTH - (SCREEN_WIDTH + 25)
MaxY = SCREEN_HEIGHT - 10
MinY = SCREEN_HEIGHT - (SCREEN_HEIGHT + 25)

CLOCK   = pygame.time.Clock()
FPS     = 60

BG = [0, 0, 0]

IS_RUNNING = True

my_spritesheet = Spritesheet('./Art/spritesheet.png')
playerSprite = my_spritesheet.getSprite(0,0,100,100)
playerRect = playerSprite.get_rect()
playerStats = Link(3, 20, 5, 2.5)

vel_x = 12
vel_y = 12
jump = False

#----------------------------------------------------------------------------------------------------------------------------------------
# Sprite Lists
walkRight = [my_spritesheet.parseSprite('tile000.png'), my_spritesheet.parseSprite('tile001.png'), my_spritesheet.parseSprite('tile002.png'), my_spritesheet.parseSprite('tile003.png'), my_spritesheet.parseSprite('tile004.png'), 
          my_spritesheet.parseSprite('tile005.png'), my_spritesheet.parseSprite('tile006.png'), my_spritesheet.parseSprite('tile007.png')]

walkDown = [my_spritesheet.parseSprite('tile008.png'), my_spritesheet.parseSprite('tile009.png'), my_spritesheet.parseSprite('tile010.png'), my_spritesheet.parseSprite('tile011.png'), my_spritesheet.parseSprite('tile012.png'), 
            my_spritesheet.parseSprite('tile013.png'), my_spritesheet.parseSprite('tile014.png'), my_spritesheet.parseSprite('tile015.png')]

walkLeft = [my_spritesheet.parseSprite('tile016.png'), my_spritesheet.parseSprite('tile017.png'), my_spritesheet.parseSprite('tile018.png'), my_spritesheet.parseSprite('tile019.png'), my_spritesheet.parseSprite('tile020.png'), 
            my_spritesheet.parseSprite('tile021.png'), my_spritesheet.parseSprite('tile022.png'), my_spritesheet.parseSprite('tile023.png')]

walkUp = [my_spritesheet.parseSprite('tile024.png'), my_spritesheet.parseSprite('tile025.png'), my_spritesheet.parseSprite('tile026.png'), my_spritesheet.parseSprite('tile027.png'), my_spritesheet.parseSprite('tile028.png'), 
          my_spritesheet.parseSprite('tile029.png'), my_spritesheet.parseSprite('tile030.png'), my_spritesheet.parseSprite('tile031.png')]

index = 0

#----------------------------------------------------------------------------------------------------------------------------------------


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
        index = (index + 1) % len(walkUp)
    elif (KEYS_DOWN[K_DOWN]) or (KEYS_DOWN[K_s]):
        playerRect.y += playerStats.playerSpeed
        index = (index + 1) % len(walkDown)

    if (KEYS_DOWN[K_LEFT]) or (KEYS_DOWN[K_a]):
        playerRect.x -= playerStats.playerSpeed
        index = (index + 1) % len(walkLeft)
    elif (KEYS_DOWN[K_RIGHT]) or (KEYS_DOWN[K_d]):
        playerRect.x += playerStats.playerSpeed
        index = (index + 1) % len(walkRight)

    
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
        vel_y -= 0.75
        if vel_y < -12:
            jump = False
            vel_y = 12

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
