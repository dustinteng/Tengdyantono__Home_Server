#this code is meant to reset the server every 30 minutes, to prevent 
#the webpage to be 'freezed' this code let users to not have to deal with 
#coding / even resetting the server. 

#imports
import webpage 
import time
import os
import datetime
#variable initalization
# hours = 12
# minutes = hours*60
# seconds = minutes * 60
timeReset = "12:00"
while True:
    os.system("clear")
    timenow= datetime.datetime.now().strftime("%H:%M")

    if timenow == timeReset:
        os.system("pm2 restart 1") #smart / lazy :)
        print("website is running")
        print("reset every " + str(minutes) + " minutes")

    time.sleep(5)
    