import pygame, sys, math
from Ball import *
from Laser import *


class Player(Ball):
    def __init__(self, maxSpeed=4, startPos=[0,0]):
        Ball.__init__(self, [0,0], startPos)
        self.baseImage = pygame.image.load("Images/Player/Ship.png")
        self.imagedead = pygame.image.load("Images/Player/DestroyedShip6.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect(center=startPos)
        self.x = self.rect.centerx
        self.y = self.rect.centery
        
        self.explosionImages = [pygame.image.load("Images/Player/DestroyedShip1.png"),
                      pygame.image.load("Images/Player/DestroyedShip2.png"),
                      pygame.image.load("Images/Player/DestroyedShip3.png"),
                      pygame.image.load("Images/Player/DestroyedShip4.png"),
                      pygame.image.load("Images/Player/DestroyedShip5.png"),
                      pygame.image.load("Images/Player/DestroyedShip6.png"),
                      pygame.image.load("Images/Player/DestroyedShip7.png"),
                      pygame.image.load("Images/Player/DestroyedShip8.png"),
                      pygame.image.load("Images/Player/DestroyedShip9.png"),
                      pygame.image.load("Images/Player/DestroyedShip10.png"),
                      pygame.image.load("Images/Player/DestroyedShip11.png"),]
        
        self.frame = 0
        self.frameMax = len(self.images)-1 
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.animationTimer = 0
        self.animationTimerMax = 120/10
        self.maxSpeed = maxSpeed
        self.angle = 90
        self.speed = 0
        self.turnSpeed = 2
        self.accSpeed = .2
    
        self.kind = "player"
        
        self.fireSound=pygame.mixer.Sound("Sounds/PlayerSounds/laser.mp3")
        self.fireSound.set_volume(.075)
        self.dieSound=pygame.mixer.Sound("Sounds/PlayerSounds/player death.mp3")
        self.dieSound.set_volume(.25)
        

    def goKey(self, direction):
        if direction == "left":
            self.angle += self.turnSpeed
        elif direction == "right":
            self.angle -= self.turnSpeed
        elif direction == "up":
            self.speed += self.accSpeed
        elif direction == "down":
            self.speed -= self.accSpeed        
    
    def explode(self):
        if self.animationTimer >= self.animationTimerMax:
            self.animationTimer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]
                    
    def move(self):
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif self.speed < -self.maxSpeed:
            self.speed = -self.maxSpeed
        self.angle %= 360
        
        self.x += math.cos(math.radians(self.angle))*self.speed
        self.y += -math.sin(math.radians(self.angle))*self.speed
        
        self.rect.center = [round(self.x), round(self.y)]        
    
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
       
        if self.y > height:
            self.y = 0
        elif self.y < 0:
            self.y = height
        if self.x > width:
            self.x = 0
        elif self.x < 0:
            self.x = width
            

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
        self.explode()
        self.dieSound.play()
        self.maxSpeed = 0
        self.angle = 90
        self.speed = 0
        self.turnSpeed = 0
        self.accSpeed = 0
    
    def respawn(self):
        self.maxSpeed = 4
        self.angle = 90
        self.speed = 0
        self.turnSpeed = 2
        self.accSpeed = .2
        self.y = 350
        self.x = 450
    
    
    def fire(self):
        self.fireSound.play()
        return Laser(8,self.angle, self.rect.center)
