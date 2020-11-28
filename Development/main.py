import sys, pygame, json
from pygame.locals import *

# Necessary setup before you can start using pygame functionalities:
pygame.init()



class Link:
  # Standaard waarders
    lives = 3
    y = 0
    x = 0
    points = 20
    strength = 5
    playerSpeed = 2.5
    playerSprite = None
    rect = None


  # In
    def __init__(self):
        self.playerSprite = pygame.image.load('./Art/spr_Player.png')
        self.rect = self.playerSprite.get_rect()

    def stats(self):
      return self.points, self.strength, self.playerSpeed

    def jump(self):
        # Instructie om te springen
        vel_x = 12
        vel_y = 12
        jump = False
        pass

    def Update(self):
      if (KEYS_DOWN[K_UP]) or (KEYS_DOWN[K_w]):
        self.rect.y -= self.playerSpeed
      elif (KEYS_DOWN[K_DOWN]) or (KEYS_DOWN[K_s]):
        self.rect.y += self.playerSpeed

      if (KEYS_DOWN[K_LEFT]) or (KEYS_DOWN[K_a]):
        self.rect.x -= self.playerSpeed
      elif (KEYS_DOWN[K_RIGHT]) or (KEYS_DOWN[K_d]):
        self.rect.x += self.playerSpeed

      if player.rect.y > MaxY:
          player.rect.y = MaxY
      elif player.rect.y < MinY:
          player.rect.y = MinY

      if player.rect.x > MaxX:
          player.rect.x = MaxX
      elif player.rect.x < MinX:
          player.rect.x = MinX




    
    def Draw(self, screenRef):
      screenRef.blit(self.playerSprite, self.rect)


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


player = Link()


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

    player.Update()

    # ------------------------------------------------
    # DRAWING INSTRUCTIONS
    # ------------------------------------------------
    # First clear the screen with a background color.
    # If you don't, you'll draw on top of what was previously drawn. See for yourself by removing/commenting this line... :)
    SCREEN.fill(BG)
    # Background Image
    SCREEN.blit(BACKGROUND,(0,0))


    player.Draw(SCREEN)
    
    # Finally refresh the entire screen of this application window:
    pygame.display.flip()

    # Prevent the game from running way too fast by restricting the amount of update cycles made per second.
    # The program basically waits a certain amount of time before it continues.
    # This function converts the desired result, which is expressed in "frames per second", into the exact nanoseconds wait time.
    CLOCK.tick(FPS)
