# Tengdyantono__Home_Server
IoT based home server

This is an IoT project for individual smart home application.
functions: 
 - Control house's main gate
 - Control the self built 5 outputs sprinkler system. (The sprinkler system is also fully automated with soil moisture sensor)

the project will be divided into two parts
1. Arduino - as a supporting device to control the gate
2. Raspberry - as a main device that acts as brain / server

Arduino 
you just need to compile the code to your arduino, while making sure the Arduino output jumper is connected to the signal input in the gate motor PCB. 

Raspberry 
control the local web server, GUI, Arduino, and automated sprinkler
- Preferable to use a virtual environment - using miniconda in this case
- Using PM2 for threading and to keep the server and daily routine running, even after a power failure
- Control the arduino through bluetooth
- Local web-server using WiFi
- Allows users to turn on and off the sprinkler system via the local website.
- Allows users to open and close the gate through any types of smart devices as long as it is connected to the WiFi.


