import pygame, sys, math

class Laser():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Laser.__init__(self, [0,0], startPos)
        self.image = [pygame.image.load("Images/Other/Laser.png")]
        self.rect = self.image.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "laser"
        self.kind = "player"
    def sound(self):
        end

def fire():
    end
    
def ballCollide(self, other):
        if other == Ball:
            self.remove
            ball.remove
