import pygame, sys, math
from Ball import *

class PlayerBall():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.image = [pygame.image.load("Images/Player/Ship.png")]
        frame = self.image[self.frame]
        self.rect = frame.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "player"

    def goKey(self, direction):
        if direction == "left":
            self.speed = maxSpeed
        
        elif direction == "right":
             self.speed = maxSpeed
            
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
                
            if self.rect.top < 0:
                print("")
            
                
        if not self.didBounceY:
            if self.rect.right > width:
                print("")
                
                
            if self.rect.left < 0:
                print("")
                
                
            
    def ballCollide(self, other):
        if self != other:
            self.speed = 0
