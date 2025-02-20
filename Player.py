import pygame, sys, math
from Ball import *

class Player(Ball):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.baseImage = pygame.image.load("Images/Player/Ship.png")
        self.imagedead = pygame.image.load("Images/Player/DestroyedShip.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect()
        self.x = self.rect.centerx
        self.y = self.rect.centery
        
        self.maxSpeed = maxSpeed
        self.angle = 90
        self.speed = 0
        self.turnSpeed = 2
        self.accSpeed = .1
        
        self.kind = "player"
        
        self.fireSound=pygame.mixer.Sound("Sounds/PlayerSounds/laser.mp3")
        self.dieSound=pygame.mixer.Sound("Sounds/PlayerSounds/player death.mp3")


    def goKey(self, direction):
        if direction == "left":
            self.angle += self.turnSpeed
        elif direction == "right":
            self.angle -= self.turnSpeed
        elif direction == "up":
            self.speed += self.accSpeed
        elif direction == "down":
            self.speed -= self.accSpeed
        
                    
                    
    def move(self):
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif self.speed < -self.maxSpeed:
            self.speed = -self.maxSpeed
        self.angle %= 360
        
        self.x += math.cos(math.radians(self.angle))*self.speed
        self.y += -math.sin(math.radians(self.angle))*self.speed
        
        self.rect.center = [round(self.x), round(self.y)]
        
        
        
    def animate(self):
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False  
        
    def death(self):
        self.dieSound.play()
    
    def fire(self):
        self.fireSound.play()
