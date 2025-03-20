import pygame, sys, math

class Ball():
    def __init__(self, speed = [1,1], startPos=[350,250]):
        self.images = [pygame.image.load("Images/Ball/Ball1.png"),
                      pygame.image.load("Images/Ball/Ball2.png"),
                      pygame.image.load("Images/Ball/Ball3.png"),
                      pygame.image.load("Images/Ball/Ball4.png"),
                      pygame.image.load("Images/Ball/Ball3.png"),
                      pygame.image.load("Images/Ball/Ball2.png")]
        self.frame = 0
        self.frameMax = len(self.images)-1 
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.speedy = speed[0]
        self.speedx = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 +self.rect.width/2)/2
        
        self.explosionImages = [pygame.image.load("Images/Ball/BallExplode1.png"),
                      pygame.image.load("Images/Ball/BallExplode2.png"),
                      pygame.image.load("Images/Ball/BallExplode3.png"),
                      pygame.image.load("Images/Ball/BallExplode4.png"),
                      pygame.image.load("Images/Ball/BallExplode5.png"),
                      pygame.image.load("Images/Ball/BallExplode6.png"),
                      pygame.image.load("Images/Ball/BallExplode7.png"),]
        
        self.rect = self.rect.move(startPos)

        
        self.kind = "ball"
        self.animationTimer = 0
        self.animationTimerMax = 120/10
        
        self.deathSound=pygame.mixer.Sound("Sounds/Other/ball explosion.mp3")
        
    
    def update(self, size):
        self.move()
        
       
        self.animationTimer += 1
        self.animate()
        

    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
        
    def animate(self):
        if self.animationTimer >= self.animationTimerMax:
            self.animationTimer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]
            
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False       
        
        
    def die(self):
        self.deathSound.play()
        

    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)


