import pygame, sys, math, random
from Player import *
from Ball import *


clock = pygame.time.Clock();
size = [900, 700]
screen = pygame.display.set_mode(size)
background = pygame.image.load("Images/Other/Background.png")
counter = 0;       
player = Player(4, [900/2, 700/2])
balls = [Ball()]



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("down")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKey("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKey("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKey("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKey("sdown")   
        
    
    
     
    counter += 1
    if counter >= 10:
        counter = 0;
        balls += [Ball([random.randint(-7,7), random.randint(-7,7)],
                [random.randint(100, 700), random.randint(100, 500)])
        ]
        for ball in balls:
            if balls[-1].ballCollide(ball):
                balls.remove(balls[-1])
                break
            
    for ball in balls:
        ball.update(size)
        
        
    for hittingBall in balls:
        for hitBall in balls:
            if hittingBall.ballCollide(hitBall):
                if hittingBall.kind == "player":
                    balls.remove(hitBall)
            
    
    screen.fill((64, 128, 255))
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(100)
    #print(clock.get_fps(), len(balls))
