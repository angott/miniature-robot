#!/usr/bin/python 
import sys
import pygame
import collisionModel
import playerSprite
import math
import mutable


from collections import namedtuple

 
# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pt1 = mutable.MutableNamedTuple()
pt2 = mutable.MutableNamedTuple()
pt3 = mutable.MutableNamedTuple()
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([1100, 900])

pygame.key.set_repeat(50, 30)

pt1.x = 50
pt1.y = 50
pt2.x = 200
pt2.y = 50
pt3.x = 100
pt3.y = 45

r = 6
 
# This sets the name of the window
pygame.display.set_caption('Lunar Lander')
 
clock = pygame.time.Clock()
 
# Before the loop, load the sounds:
# click_sound = pygame.mixer.Sound("laser5.ogg")
 
rotRight = False
rotLeft = False
isThrustOn = False
 
mainChar = playerSprite.PlayerSprite(90,20000,1.62,1,0.5)

colDet = collisionModel.CollisionModel()
 
player_image = mainChar.__GetRestImg__()
 
done = False
    
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True       
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_image = mainChar.__GetThrustImg__()
                isThrustOn = True
            if event.key == pygame.K_RIGHT:
                rotRight = True
            if event.key == pygame.K_LEFT:
                rotLeft = True	
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player_image = mainChar.__GetRestImg__()
                isThrustOn = False
            if event.key == pygame.K_RIGHT:
                rotRight = False
            if event.key == pygame.K_LEFT:
                rotLeft = False	
            
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            click_sound.play() 
   
    y = mainChar.positionY
    
    x = mainChar.positionX

   
    if (x < 0):
        mainChar.ResetXHigh()
        
    if (x > 1000):
        mainChar.ResetXLow()
        
    if (y < 0):
        mainChar.ResetYHigh()

        
    if (y > 800):
        mainChar.ResetYLow()
   
             
    if rotRight:
        mainChar.RotateRight()
    if rotLeft:
        mainChar.RotateLeft()

    display_image=pygame.transform.rotate(player_image,mainChar.imgRotationPos)
    
    mainChar.UpdateVelocityY()
    mainChar.UpdateThrust(isThrustOn)
    mainChar.UpdatePositionY()
    mainChar.UpdatePositionX()
    
    y = mainChar.positionY
    
    x = mainChar.positionX
    
    print (colDet.CircleTouchesLine(pt1,pt2,pt3,r))
        
             
    # Copy image to screen:
    screen.fill(BLACK)
    screen.blit(display_image, [x, y])
    print (' X : {0}  Y: {1} Rot Position : {2}'.format (x,y,mainChar.rotationPos))
    pygame.display.flip()
 
    clock.tick(30)
     
 
pygame.quit ()
