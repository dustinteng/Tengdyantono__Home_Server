#this code is meant to reset the server every 30 minutes, to prevent 
#the webpage to be 'freezed' this code let users to not have to deal with 
#coding / even resetting the server. 

#imports
import webpage 
import time
import os

#variable initalization
minutes = 10
seconds = minutes * 60
while True:
    os.system("clear")
    os.system("pm2 restart 1") #smart / lazy :)
    print("website is running")
    print("reset every " + str(minutes) + " minutes")
    time.sleep(seconds) #change the front to set minutes
    