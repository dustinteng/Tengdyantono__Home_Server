# Tengdyantono__Home_Server
IoT based home server

This is an IoT project for individual smart home application

the project will be divided into two parts
1. Arduino Part 
2. Raspberry Part 

Arduino part - to bypass the gate
you just need to compile the code to your arduino

Raspberry part - as a main brain
control the local web server, GUI, Arduino, etc
- Preferable to use a virtual environment - using miniconda in this case
- Use PM2 for threading and to keep the server and daily routine running, even after a power failure
- Control the arduino through bluetooth
- Local web-server using WiFi
- Private VPN for updates
