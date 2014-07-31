#!/usr/bin/python
import sys
import pygame

class PlayerSprite:
    'Class for players ship'
    pygame.init()
    rotationPos = 0
    fuelRemaining = 20000
    imgThrust = pygame.image.load(".\\images\\landerThrust.png")
    imgRest = pygame.image.load(".\\images\\lander.png")
    velocityX = 0
    velocityY = 0
    positionX = 50
    positionY = 50
    gravity = 9.2 # 'Earth gravity, overridden at init'
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
        PlayerSprite.rotationPos +=1
        if PlayerSprite.rotationPos >359:
            PlayerSprite.rotationPos = 0
         
    def RotateLeft(self):
        PlayerSprite.rotationPos -=1
        if PlayerSprite.rotationPos < 0:
            PlayerSprite.rotationPos = 359       
 #   def Thrust(self)
         
 #   def UpdateVelocityY(self)
         
 #   def UpdateVelocityX(self)
         
 #   def UpdateFuel(self)
     
     

