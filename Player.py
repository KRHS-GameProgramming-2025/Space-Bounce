import pygame, sys, math
from Main import *

class PlayerBall():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.image = [pygame.image.load("Images/Player/Ship.png")]
        self.rect = self.image.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "player"

    def goKey(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeed
        elif direction == "right":
            self.speedx = self.maxSpeed
        elif direction == "up":
            self.speedy = -self.maxSpeed
            self.images = self.imagesUp
        elif direction == "down":
            self.speedy = self.maxSpeed
        elif direction == "sleft":
            self.speedx = 0
        elif direction == "sright":
            self.speedx = 0
        elif direction == "sup":
            self.speedy = 0
        elif direction == "sdown":
            self.speedy = 0 
            
               
    def wallcollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.Rect.bottom > height:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
            if self.Rect.top < 0:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
        if not self.didBounceX:
            if self.Rect.right > width:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
            if self.Rect.left < 0:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
                
                
            
    def ballCollide(self, other):
        if self != other:
            print("e")
