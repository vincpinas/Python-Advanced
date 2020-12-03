class Link:
  # Standaard waardes
    lives = 3
    y = 0
    x = 0
    points = 20
    strength = 5
    playerSpeed = 2.5
    playerSprite = None
    rect = None
    jumping = False

  # In
    def __init__(self):
        self.playerSprite = pygame.image.load('./Art/spr_Player.png')
        self.rect = self.playerSprite.get_rect()

    def stats(self):
      return self.points, self.strength, self.playerSpeed

    def jump(self, jumping):
        # Instructie om te springen
        vel_y = 10
        self.jumping = jumping
        if self.jumping is True:
          self.rect.y -= vel_y
          vel_y -= 1
          if vel_y < -10:
            self.jumping = False
            vel_y = 10

    def Update(self):
      if (KEYS_DOWN[K_UP]) or (KEYS_DOWN[K_w]):
        self.rect.y -= self.playerSpeed
      elif (KEYS_DOWN[K_DOWN]) or (KEYS_DOWN[K_s]):
        self.rect.y += self.playerSpeed

      if (KEYS_DOWN[K_LEFT]) or (KEYS_DOWN[K_a]):
        self.rect.x -= self.playerSpeed
      elif (KEYS_DOWN[K_RIGHT]) or (KEYS_DOWN[K_d]):
        self.rect.x += self.playerSpeed

      if self.rect.y > MaxY:
          self.rect.y = MaxY
      elif self.rect.y < MinY:
          self.rect.y = MinY

      if self.rect.x > MaxX:
          self.rect.x = MaxX
      elif self.rect.x < MinX:
          self.rect.x = MinX

      if self.jumping is False and (KEYS_DOWN[K_SPACE]):
        self.jump(True)

    def Draw(self, screenRef):
      screenRef.blit(self.playerSprite, self.rect)
