import pygame, sys, math

self.hitSound=pygame.mixer.Sound("Sounds/Other/hit target explosion.mp3")

class Laser():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Laser.__init__(self, [0,0], startPos)
        self.image = [pygame.image.load("Images/Other/Laser.png")]
        self.rect = self.image.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "laser"
        self.kind = "player"

def hit(self):
    self.hitSound.play()



    
def ballCollide(self, other):
        if other == Ball:
            self.remove
            ball.remove
