# this file is the backbone of the automated sprater prototype 
# at Tengdyantono's residence.
# this file handles the input from the gui and output working automated apreayer


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QProgressBar, QPushButton,QApplication
import RPi.GPIO as GPIO
from tqdm import tqdm, trange
import time
import os

from dotenv import load_dotenv
load_dotenv()

from coolloading2 import Ui_Dialog

ui= Ui_Dialog()

#from guidialog import Ui_MainWindow

#from pymemcache.client.base import Client
#client = Client('localhost',11211)

#setting up GPIO pins
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
# GPIO.setup(21,GPIO.OUT, initial= 1) #for the pump relay
# GPIO.setup(2,GPIO.OUT, initial= 1) #for the pipe relay zone 1
# GPIO.setup(3,GPIO.OUT, initial= 1) #for the pipe relay zone 2
# GPIO.setup(4,GPIO.OUT, initial= 1) #for the pipe relay zone 3

class sprayer:

    def __init__(self):
        self.timespray = int(os.getenv("SPRAY_TIME"))
        self.pinZone1 = 2 # inside front 2 units || relay is not working properly
        self.pinZone2 = 3 # inside side 3 units
        self.t= self.timespray #seconds 
        GPIO.setup(self.pinZone1,GPIO.OUT, initial= 1) #for the pipe relay zone 1
        GPIO.setup(self.pinZone2,GPIO.OUT, initial= 1) #for the pipe relay zone 2

    def spray(self,zone):
        if zone == 1:
            #zone 1 on
            GPIO.output(self.pinZone1,0)
            
            #loading screen
            self.loading_clicked()

            #turning off both
            GPIO.output(self.pinZone1,1)

        elif zone == 2:
            #zone 2 on
            GPIO.output(self.pinZone2,0)

            #loading screen
            self.loading_clicked()

            #turning off both
            GPIO.output(self.pinZone2,1)

        print('turned off')
    
    def spray_all(self):
        #turning on        
        GPIO.output(self.pinZone1,0)

        #loading screen
        self.loading_clicked()

        GPIO.output(self.pinZone2,0)
        GPIO.output(self.pinZone1,1)

        #loading screen
        self.loading_clicked()

        GPIO.output(self.pinZone2,1)

        print('system off')

    def loading_clicked(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()


        


            



