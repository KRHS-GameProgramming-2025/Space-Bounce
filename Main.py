#------------------Variables------------------

import pygame, sys, math, random, time
from Player import *
from Ball import *
from Laser import *
from HUD import *

pygame.init()

try:
    pygame.mixer.init()
    sound = True
except:
    sound = False
    
if not pygame.font: print("Warning, fonts disabled")

clock = pygame.time.Clock();
size = [900, 700]
screen = pygame.display.set_mode(size)

mode="start" 

if sound: 
    pygame.mixer.music.load("Sounds/Music/SkyFire.mp3")
    pygame.mixer.music.set_volume(.25)
    pygame.mixer.music.play(-1)
else:
   print("No Sound")
    

mode="start"

#------------------Main Loop------------------

while True:
    background = pygame.image.load("Images/Other/TitleScreen.png")
    while mode =="start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mode="play"
        screen.fill((64, 128, 255))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        
        clock.tick(100)
        
    background = pygame.image.load("Images/Other/Background.png")
    lifeImage = pygame.image.load("Images/Other/ShipLife.png")
    missingLifeImage = pygame.image.load("Images/Other/ShipLifeMissing.png")
    
    counter = 0;  
    player = Player(4, [900/2, 700/2])
    balls = [Ball()]
    canShoot = True
    shootTimer = 0
    shootTimerMax = 1 * 100
    deathTimer = 150
    laserTimer = 100
    alive = True
    lives = 3
    
    score = Hud("",0,[0,0])
    points = 0
    
    keys = []
    lasers=[]
    bombIsExploding = False
    
    while mode == "play":
        if lives > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit();
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        keys += ["a"]
                    elif event.key == pygame.K_d:
                        keys += ["d"]
                    elif event.key == pygame.K_w:
                        keys += ["w"]
                    elif event.key == pygame.K_s:
                        keys += ["s"]
                        
                    elif event.key == pygame.K_SPACE:
                        if canShoot:
                            lasers+=[player.fire()]
                            canShoot = False
                            shootTimer = shootTimerMax
                    elif event.key == pygame.K_o:
                        player.death()
                    
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        if ("a") in keys:
                            keys.remove("a")
                        else:
                            keys += ["a"]
                            keys.remove("a")
                    elif event.key == pygame.K_d:
                        if ("d") in keys:
                            keys.remove("d")
                        else:
                            keys += ["d"]
                            keys.remove("d")
                    elif event.key == pygame.K_w:
                        if ("w") in keys:
                            keys.remove("w")
                        else:
                            keys += ["w"]
                            keys.remove("w")
                    elif event.key == pygame.K_s:
                        if ("s") in keys:
                            keys.remove("s")
                        else:
                            keys += ["s"]
                            keys.remove("s")
                        
            if "a" in keys:
                player.goKey("left")
            elif "d" in keys:
                player.goKey("right")
            elif "w" in keys:
                player.goKey("up")
            elif "s" in keys:
                player.goKey("down")
                
            if bombIsExploding:
            if bomb.explode():
                bombIsExploding = False
                
                goodSpawn = False
                while not goodSpawn:
                    print("Respawning")
                    bomb.respawn(size, tileSize)
                    goodSpawn = not checkSpawn(bomb)
                player.die(bomb.damage)
            
            if not canShoot and shootTimer != 0:
                shootTimer -= 1
            elif not canShoot and shootTimer <= 0:
                shootTimer = 0
                canShoot = True

            
            counter += 1
            if counter >= 300:  
                balls += [Ball([random.randint(-4,4), random.randint(-4,4)],
                        [random.randint(0, 700), random.randint(0, 500)])
                ]
                counter = 0
                for ball in balls:
                    if balls[-1].ballCollide(ball):
                        balls.remove(balls[-1])
                        break
                        
            player.update(size)
                 
            for ball in balls:
                ball.update(size)
                for laser in lasers:
                    laserTimer -= 1
                    if ball.ballCollide(laser):
                        lasers.remove(laser)
                        laserTimer = 100
                        points += 50
                        balls.remove(ball)
                        laser.hit()
                        score.update(points)
                    elif laserTimer <= 0 and canShoot == True:
                        laser.update(size)
                        lasers.remove(laser)
                        laserTimer = 100
                   
            
                if player.ballCollide(ball):
                    if alive == True:
                        alive = False
                        player.death()
                if alive == False:
                    canShoot = False
                    deathTimer -= 1
                    if deathTimer <= 0:
                        deathTimer = 150
                        alive = True
                        canShoot = True
                        lives -= 1
                        player.respawn()
                        
                        
            if lives == 0:
                mode="end"
              
                        
            for laser in lasers:
                laser.update(size)
                
        
            
        
            screen.fill((64, 128, 255))
            screen.blit(background, (0, 0))
            
            
        
            for laser in lasers:
                screen.blit(laser.image, laser.rect)
                
            if lives == 3:    
                screen.blit(lifeImage, (840, 10))
                screen.blit(lifeImage, (780, 10))
                screen.blit(lifeImage, (720, 10))
            if lives == 2:    
                screen.blit(lifeImage, (840, 10))
                screen.blit(lifeImage, (780, 10))
                screen.blit(missingLifeImage, (720, 10))
            if lives == 1:    
                screen.blit(lifeImage, (840, 10))
                screen.blit(missingLifeImage, (780, 10))
                screen.blit(missingLifeImage, (720, 10))
                
            for ball in balls:
                screen.blit(ball.image, ball.rect)
            screen.blit(player.image, player.rect)
            screen.blit(score.image, score.rect)
            pygame.display.flip()
        
        #FFFFF
        
        clock.tick(100)
        #print(clock.get_fps(), len(balls))
    
    background = pygame.image.load("Images/Other/Deathscreen.png")
    while mode =="end":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit();
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    mode="start"
                    
                    
        screen.fill((64, 128, 255))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        
        clock.tick(100)
