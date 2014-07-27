#!/usr/bin/python

class Player:
    'Class for players ship'
    rotationPos = 0
    fuelRemaining = 20000
    imgThrust = Image.open("\\images\\landerthrust.jpg")
    imgRest = Image.open("\\images\\lander.jpg")
    velocityX = 0
    velocityY = 0
    positionX = 50
    positionY = 50
    gravity = 9.2 # 'Earth gravity, overridden at init'
    unitsFuelPerTime = 100
    accelPerUnitFuel = .5
    cellx = 13
    celly = 13

    def __init__(self, rotationInit, fuelInit, gravitInit, unitsFuelPerTimeInit, accelPerUnitFuelInit):
        Player.rotationPos = rotationInit
        Player.fuelRemaining = fuelInit
        Player.unitsFuelPerTime = unitsFuelPerTimeInit
        Player.accelPerUnitFuel = accelPerUnitFuelInit
        Player.gravity = gravityInit
        
   
 

