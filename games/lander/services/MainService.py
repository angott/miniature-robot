#!/usr/bin/python 
import sys
import pygame
import playerSprite
import math
 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

pygame.key.set_repeat(50, 30)
 
# This sets the name of the window
pygame.display.set_caption('Lunar Lander')
 
clock = pygame.time.Clock()
 
# Before the loop, load the sounds:
# click_sound = pygame.mixer.Sound("laser5.ogg")
 
rotRight=False
rotLeft=False
 
mainChar = playerSprite.PlayerSprite(0,20000,9.2,1,0.5)
 
player_image = mainChar.__GetRestImg__()
 
done = False
 
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_image = mainChar.__GetThrustImg__()
            if event.key == pygame.K_RIGHT:
                rotRight = True
            if event.key == pygame.K_LEFT:
                rotLeft = True	
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_image = mainChar.__GetRestImg__()
            if event.key == pygame.K_RIGHT:
                rotRight = False
            if event.key == pygame.K_LEFT:
                rotLeft = False	
            
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            click_sound.play() 
             
    if rotRight:
        mainChar.RotateRight()
    if rotLeft:
        mainChar.RotateLeft()

    display_image=pygame.transform.rotate(player_image,mainChar.rotationPos)
    
    #if (mainChar.rotationPos>0):
    #    player_image.Transformer.RotateRight(degrees)
    #else:
    #    player_image.Transformer.RotateLeft(degrees)  
    
    #player_position = pygame.mouse.get_pos()
    #x = player_position[0]
    #y = player_position[1]
    
    x =100
    y = 200
     
    # Copy image to screen:
    screen.fill(BLACK)
    screen.blit(display_image, [x, y])
     
    pygame.display.flip()
 
    clock.tick(60)
     
 
pygame.quit ()
