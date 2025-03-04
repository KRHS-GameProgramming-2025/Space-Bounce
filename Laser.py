import pygame, sys, math


class Laser():
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        self.image = pygame.image.load("Images/Other/Laser.png")
        self.rect = self.image.get_rect()
        self.maxSpeed = maxSpeed
        self.kind = "laser"
        self.kind = "player"
        self.hitSound=pygame.mixer.Sound("Sounds/Other/hit target explosion.mp3")
        self.hitSound.set_volume(.25)


    def hit(self):
        self.hitSound.play()

    def ballCollide(self, other):
            if other == Ball:
                self.remove
                ball.remove
