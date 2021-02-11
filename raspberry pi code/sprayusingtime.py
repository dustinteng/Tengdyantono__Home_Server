""" This file is intended to automate the garden sprinkler """
__author__ = "Jan Dustin Tengdyantono"
__copyright__ = "none"

#!/usr/bin/python
from sprayerNoGui import sprayer
import os
import time
import datetime
import RPi.GPIO as GPIO

#setting up GPIO pins
#GPIO.setwarnings(False)
pinSoil = 21
pinZone1 = 2
pinZone2 = 3
GPIO.setmode (GPIO.BCM)

#setting up GPIO pins just in case if bug happens, so we can restart
GPIO.setup(pinSoil,GPIO.IN) # soil mosture sensor
GPIO.setup(pinZone1,GPIO.OUT, initial= 1) # sprayer relay zone 1
GPIO.setup(pinZone2,GPIO.OUT, initial= 1) # sprayer relay zone 2

#initialization
sprayer = sprayer()
condition = False

#global variable
sprayTime = "17:00"
canSpray = "17:10"

while True:
    os.system('clear')
    #GPIO.output(pinZone1,1)
    #GPIO.output(pinZone2,1)
    # checking time
    timenow= datetime.datetime.now().strftime("%H:%M")
    # checking soil condition
    soil = GPIO.input(pinSoil)

    # logic
    if timenow == sprayTime and condition == False and soil == 1:
        condition = True #currently spraying 
        sprayer.spray_all()
        print('setting system mode to: STANDBY')

    # this if statement is meant to prevent multiple program run during the sprayTime
    elif timenow == canSpray:
        condition = False

    # print lines
    print("Current Time: " + timenow)
    print("Scheduled at :" + sprayTime)
    if soil == 1:
        print("soil condition: dry")
    else:
        print("soil condition: wet")

    time.sleep(5)
