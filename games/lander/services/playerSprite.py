#!/usr/bin/python
import sys
import pygame
import math

class PlayerSprite:
    'Class for players ship'
    pygame.init()
    imgRotationPos = 0
    rotationPos = 90
    fuelRemaining = 20000
    imgThrust = pygame.image.load(".\\images\\landerThrust.png")
    imgRest = pygame.image.load(".\\images\\lander.png")
    velocityX = 0
    velocityY = 0
    positionX = 50
    positionY = 50
    gravity = 9.2 # 'Earth gravity, overridden at init'
    thrustForce = 20
    unitsFuelPerTime = 100
    accelPerUnitFuel = .5
    cellx = 13
    celly = 13
    frameRate = 30
    degreeRotationPerFrame = 1

    def __init__( self,rotationInit, fuelInit, gravityInit, unitsFuelPerTimeInit, accelPerUnitFuelInit):
        PlayerSprite.rotationPos = rotationInit
        PlayerSprite.fuelRemaining = fuelInit
        PlayerSprite.unitsFuelPerTime = unitsFuelPerTimeInit
        PlayerSprite.accelPerUnitFuel = accelPerUnitFuelInit
        PlayerSprite.gravity = gravityInit
    
    def __GetRestImg__ (self):
        return PlayerSprite.imgRest
        
    def __GetThrustImg__(self):
        return PlayerSprite.imgThrust
   
    def RotateRight(self):
        PlayerSprite.imgRotationPos -=5
        if PlayerSprite.imgRotationPos < 0:
            PlayerSprite.imgRotationPos = 359 
        PlayerSprite.rotationPos -=5
        if PlayerSprite.rotationPos < 0:
            PlayerSprite.rotationPos = 359 
        
    def RotateLeft(self):
        PlayerSprite.imgRotationPos +=5
        if PlayerSprite.imgRotationPos >359:
            PlayerSprite.imgRotationPos = 0
        PlayerSprite.rotationPos +=5
        if PlayerSprite.rotationPos >359:
            PlayerSprite.rotationPos = 0   
                          
    def UpdateThrust(self, isThrust):
        if isThrust == True:
            totThrust = 0
            totThrust = PlayerSprite.thrustForce * 1/PlayerSprite.frameRate 
            print (totThrust)
            velY = 0
            velX = 0
            correctedAngle = 0
            
            if (PlayerSprite.rotationPos == 0 or PlayerSprite.rotationPos == 90 or PlayerSprite.rotationPos == 180 or PlayerSprite.rotationPos == 270 or PlayerSprite.rotationPos == 360):
                if (PlayerSprite.rotationPos == 0 or PlayerSprite.rotationPos == 360):
                    velY = 0
                    velX = totThrust
                elif (PlayerSprite.rotationPos == 90):
                    velY = totThrust * -1
                    velX = 0               
                elif (PlayerSprite.rotationPos == 180):
                    velY = 0
                    velX = totThrust * -1               
                elif (PlayerSprite.rotationPos == 270):
                    velY = totThrust
                    velX = 0              
            else:
                correctedAngle = PlayerSprite.rotationPos 
                velY = abs(math.sin(correctedAngle))*totThrust
                velX = abs(math.cos(correctedAngle))*totThrust
                if (PlayerSprite.rotationPos < 90): 
                    velX = abs(velX)
                    velY = abs(velY) * (-1)
                elif (90 < PlayerSprite.rotationPos < 180):		
                    velX = abs(velX) * (-1)
                    velY = abs(velY) * (-1)
                elif (180 < PlayerSprite.rotationPos < 270):		
                    velX = abs(velX) * (-1)
                    velY = abs(velY)
                elif (270 < PlayerSprite.rotationPos < 360):		
                    velX = abs(velX) 
                    velY = abs(velY)
                   
            print('velX : {0} , velY : {1} , rotation : {2} correctedAngle : {3}'.format(velX,velY,PlayerSprite.rotationPos, correctedAngle))
                    
            PlayerSprite.velocityY += velY
            PlayerSprite.velocityX += velX
         
    def UpdateVelocityY(self):
        velY = 0
        velY += PlayerSprite.gravity * 1/PlayerSprite.frameRate
        PlayerSprite.velocityY += abs(velY)
        
    def UpdatePositionY(self):
        PlayerSprite.positionY += PlayerSprite.velocityY

    def UpdatePositionX(self):
        PlayerSprite.positionX += PlayerSprite.velocityX
        
    def ResetYLow (self):
        PlayerSprite.positionY = 1
		
    def ResetYHigh (self):
        PlayerSprite.positionY = 800
		
    def ResetXLow (self):
        PlayerSprite.positionX = 1
		
    def ResetXHigh (self):
        PlayerSprite.positionX = 974
            
     

