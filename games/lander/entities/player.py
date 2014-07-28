#!/usr/bin/python

class Player:
    'Class for players ship'
    rotationPos = 0
    fuelRemaining = 20000
    imgThrust = Image.open("\\images\\landerThrust.bmp")
    imgRest = Image.open("\\images\\lander.bmp")
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

    def __init__(self, rotationInit, fuelInit, gravitInit, unitsFuelPerTimeInit, accelPerUnitFuelInit):
        Player.rotationPos = rotationInit
        Player.fuelRemaining = fuelInit
        Player.unitsFuelPerTime = unitsFuelPerTimeInit
        Player.accelPerUnitFuel = accelPerUnitFuelInit
        Player.gravity = gravityInit
        
   
     def RotateRight (self)
     
     def RotateLeft (self)
     
     def Thrust (self)
     
     def UpdateVelocityY (self)
     
     def UpdateVelocityX (self)
     
     def UpdateFuel (self)
     
     

