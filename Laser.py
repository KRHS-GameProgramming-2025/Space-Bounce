import pygame, sys, math
from Ball import *

class Laser(Ball):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.image = pygame.image.load("Images/Other/Laser.png")
        self.rect = self.image.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "laser"
        self.kind = "player"
        self.hitSound=pygame.mixer.Sound("Sounds/Other/hit target explosion.mp3")


    def hit(self):
        self.hitSound.play()
        
        
    def ballCollide(self, other):
            if other == Ball:
                if self.rect.right > other.rect.left:
                    if self.rect.left < other.rect.right:
                        if self.rect.bottom > other.rect.top:
                            if self.rect.top < other.rect.bottom:
                                if self.getDist(other) < self.rad + other.rad:
                                    self.remove
                                    other.remove
                                    return True
            return False       
