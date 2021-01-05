import RPi.GPIO as GPIO
from tqdm import tqdm, trange
import time
import os
from dotenv import load_dotenv
load_dotenv()

#setting up GPIO pins
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)

class sprayer:

    def __init__(self):
        self.timespray = int(os.getenv("SPRAY_TIME"))
        self.pinZone1 = 2
        self.pinZone2 = 3
        self.t= self.timespray #seconds 
        GPIO.setup(self.pinZone1,GPIO.OUT, initial= 1) #for the pipe relay zone 1
        GPIO.setup(self.pinZone2,GPIO.OUT, initial= 1) #for the pipe relay zone 2

    def spray(self,zone):
        if zone == 1:
            #turning pump and zone 1 on
            GPIO.output(self.pinPump,0)
            GPIO.output(self.pinZone1,0)


            #countdown - nanti bisa masukin ke GUI
            for i in trange(100, desc='zone 1 '):
                time.sleep(self.t/100)

            GPIO.output(self.pinPump,1)
            GPIO.output(self.pinZone1,1)
            print('turned off')

        elif zone == 2:
            #turning pump and zone 2 on
            GPIO.output(self.pinPump,0)
            GPIO.output(self.pinZone2,0)

            #countdown - nanti bisa masukin ke GUI
            for i in trange(100, desc='zone 2 '):
                time.sleep(self.t/100)

            GPIO.output(self.pinPump,1)
            GPIO.output(self.pinZone2,1)
            print('turned off')
    
    def spray_all(self):
        #turning and zone 1
        
        GPIO.output(self.pinZone1,0)

        #zone 1 timer
        for i in trange(100, desc='zone 1' ):
            time.sleep(self.t/100)

        GPIO.output(self.pinZone2,0)
        GPIO.output(self.pinZone1,1)

        #zone 2 timer
        for i in trange(100, desc='zone 2'):
            time.sleep(self.t/100)

        GPIO.output(self.pinZone2,1)
        print('turned the system off')




        


            



