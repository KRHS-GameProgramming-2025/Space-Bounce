import pygame, sys, math

class Player():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.image = [pygame.image.load("Images/Player/Laser.png")]
        self.rect = self.image.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "player"

def fire

def ballCollide(self, other):
        if other = Ball:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False      
