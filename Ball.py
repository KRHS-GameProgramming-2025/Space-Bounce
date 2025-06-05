import pygame, sys, math

class Ball():
    def __init__(self, speed = [1,1], startPos=[1000,1000]):
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
        
        self.exploding = False
        self.explosionImages = [pygame.image.load("Images/Ball/BallExplode1.png"),
                      pygame.image.load("Images/Ball/BallExplode2.png"),
                      pygame.image.load("Images/Ball/BallExplode3.png"),
                      pygame.image.load("Images/Ball/BallExplode4.png"),
                      pygame.image.load("Images/Ball/BallExplode5.png"),
                      pygame.image.load("Images/Ball/BallExplode6.png"),
                      pygame.image.load("Images/Ball/BallExplode7.png"),
                      pygame.image.load("Images/Ball/BallExplode8.png"),]
                      
        self.explosionFrameMax = len(self.explosionImages)-1 
        self.explosionFrame = 0
        self.explosionImage = self.explosionImages[self.explosionFrame]
        self.rect = self.rect.move(startPos)

        
        self.kind = "ball"
        self.animationTimer = 0
        self.explosionAnimationTimer = 0
        self.animationTimerMax = 100/8
        
        self.deathSound=pygame.mixer.Sound("Sounds/Other/ball explosion.mp3")
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.living = True
    
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
       
        if self.rect.bottom > height:
            self.rect.top = 1
            
        elif self.rect.top < 0:
            self.rect.bottom = height
    
        if self.rect.right > width:
            self.rect.left = 1
            
        elif self.rect.left < 0:
            self.rect.right = width
    
    def update(self, size):
        self.move()
        self.wallCollide(size)
        self.animationTimer += 1
        if self.exploding:
            self.explode()
        else:
            self.animate()
        self.didBounceX = False
        self.didBounceY = False
        
        

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
            
    def explode(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationTimerMax:
            self.animationTimer = 0
            self.explosionFrame += 1
            if self.explosionFrame >= self.explosionFrameMax:
                self.exploding = False
                self.explosionFrame = 0
                self.living = False
            else:
                self.image = self.explosionImages[self.explosionFrame]
            
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
        self.exploding = True
        
        

    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)


