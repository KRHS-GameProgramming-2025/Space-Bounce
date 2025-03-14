#------------------Variables------------------

import pygame, sys, math, random
from Player import *
from Ball import *
from Laser import *


try:
    pygame.mixer.init()
    sound = True
except:
    sound = False

clock = pygame.time.Clock();
size = [900, 700]
screen = pygame.display.set_mode(size)

mode="start"

title = pygame.image.load("Images/Other/TitleScreen.png")


background = pygame.image.load("Images/Other/Background.png")
while mode =="start":
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                mode="play"

counter = 0;       
player = Player(4, [900/2, 700/2])
balls = [Ball()]

if sound: 
    pygame.mixer.music.load("Sounds/Music/SkyFire.mp3")
    pygame.mixer.music.set_volume(.25)
    pygame.mixer.music.play(-1)
else:
   print("No Sound")
    
keys = []
lasers=[]

#------------------Main Loop------------------

while True:
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
                player.goKey("space")
            elif event.key == pygame.K_p:
                balls[0].die()
            elif event.key == pygame.K_o:
                player.death()
            elif event.key == pygame.K_l:
                lasers+=[player.fire()]
            elif event.key == pygame.K_t:
                lasers[0].hit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys.remove("a")
            elif event.key == pygame.K_d:
                keys.remove("d")
            elif event.key == pygame.K_w:
                keys.remove("w") 
            elif event.key == pygame.K_s:
                keys.remove("s")
                
    if "a" in keys:
        player.goKey("left")
    elif "d" in keys:
        player.goKey("right")
    elif "w" in keys:
        player.goKey("up")
    elif "s" in keys:
        player.goKey("down")
    elif "space" in keys:
        player.fire()
        
     
    counter += 1
    if counter >= 250:  
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
        if player.ballCollide(ball):
            sys.exit()
        

    death = pygame.image.load("Images/Other/Deathscreen.png")
    
    screen.fill((64, 128, 255))
    screen.blit(background, (0, 0))
    screen.blit(title, (0, 0))
    screen.blit(death, (0, 0))
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    
    #FFFFF
    
    clock.tick(100)
    #print(clock.get_fps(), len(balls))
