import pygame

class Link:
    def __init__(self, lives, points, strength, playerSpeed):
        self.lives = lives
        self.points = points
        self.strength = strength
        self.playerSpeed = playerSpeed

    def stats(self):
      return self.lives, self.points, self.strength, self.playerSpeed
