# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prototype_1_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QWidget, QProgressBar, QPushButton,QApplication
from sprayer import sprayer
#from dialogloading import Ui_loading
#from coolloading import Ui_loading
# from coolloading2 import Ui_Dialog
import os

#from showloading import ProgressBar
import time
import datetime
sprayer = sprayer()
class Ui_MainWindow(object):
    # def open_window(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui= ProgressBar()
    #     self.ui.__init__()
    #     self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 801, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("blueprint.JPG"))
        self.label.setObjectName("label")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(300, 160, 93, 28))
        self.button1.setObjectName("button1")
        #self.button1.clicked.connect(self.open_window)
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(510, 170, 93, 28))
        self.button2.setObjectName("button2")
        # self.button3 = QtWidgets.QPushButton(self.centralwidget)
        # self.button3.setGeometry(QtCore.QRect(670, 310, 93, 31))
        # self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(380, 300, 121, 51))
        self.button4.setObjectName("button4") #all zone 
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.progress = QtWidgets.QProgressBar(self.centralwidget)
        # self.progress.setGeometry(QtCore.QRect(380, 110, 311, 61))

        # self.btnStart = QPushButton ('Start', self)
        # self.btnStart.move(30,80)
        # self.btnStart.clicked.connect(self.startProgress) #nanti isi

        # self.btnReset = QPushButton('Reset', self)
        # self.btnReset.move(120,80)
        # self.btnReset.clicked.connect(self.resetBar) #nanit isi

        # self.timer = QBasicTimer()
        # self.step = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    # def loading_clicked(self):
    #     Dialog = QtWidgets.QDialog()
    #     #ui = Ui_Dialog() #use this if using coolloading2.py
    #     ui = Ui_loading() #use this if using coolloading.py
    #     ui.setupUi(Dialog)
    #     Dialog.show()
    #     Dialog.exec_()

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "Zone 1"))
        self.button2.setText(_translate("MainWindow", "Zone 2"))
        self.button4.setText(_translate("MainWindow", "All Zone"))

        self.button1.clicked.connect(self.zone1)
        #self.button1.clicked.connect(self.loading_clicked)
        
        self.button2.clicked.connect(self.zone2)
        #self.button2.clicked.connect(self.loading_clicked)

        # self.button3.clicked.connect(self.zone3)
        #self.button3.clicked.connect(self.loading_clicked)

        self.button4.clicked.connect(self.zone4)
        #self.button4.clicked.connect(self.loading_clicked)

    def zone1 (self):
        sprayer.spray(1)
        os.system('clear')

    def zone2 (self):
        sprayer.spray(2)
        os.system('clear')

    # def zone3 (self):
    #     sprayer.spray(3)
    #     os.system('clear')

    def zone4 (self):
        sprayer.spray_all()
        os.system('clear')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


    # def resetBar(self):
    #     self.step=0
    #     self.progress.setValue(0)

    # def startProgress(self):
    #     if self.timer.isActive():
    #         self.timer.stop()
    #         self.btnStart.setText('Start')
    #     else:
    #         self.timer.start(100, self)
    #         self.btnStart.setText('Stop')

    # def timerEvent(self,event):
    #     if self.step >= 100:
    #         self.timer.stop()
    #         self.btnStart.setText('Start')
    #         return
        
    #     self.step +=1
    #     self.progress.setValue(self.step)

        # def show_popup (self):
    #     msg = QMessageBox()
    #     msg.setWindowTitle("Notification")
    #     msg.setText("Springkler Zone 1: ON")
    #     msg.setIcon(QMessageBox.Information)
    #     #msg.setStandardButtons(QMessageBox.Ok) #|QMessageBox.Cancel
    #     #msg.setDefaultButton(QMessageBox.Ok)
    #     x = msg.exec_()
    #     for i in range(5,0,-1):
    #         msg.setInformativeText("countdown: " +str(i))
    #         time.sleep(1)
    #         #msg.setDetailedText("detail")

    #         #msg.buttonClicked.connect(self.popup_button)