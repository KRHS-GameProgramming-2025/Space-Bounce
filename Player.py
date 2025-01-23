import pygame, sys, math
from Ball import *

class Player():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.image = [pygame.image.load("Images/Player/Ship.png")]
        self.frame = self.image[self.frame]
        self.rect = self.frame.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "player"

    def goKey(self, direction):
        if direction == "left":
            self.speed = self.maxSpeed
        
        elif direction == "right":
             self.speed = self.maxSpeed
            
        elif direction == "up":
            self.speedy = -self.maxSpeed
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
                    
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False      
