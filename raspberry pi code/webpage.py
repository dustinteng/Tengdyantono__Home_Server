# !/usr/bin/env python3
# this code is meant to be the webpage for Tengdyantono House Tech
# this code created a website to control 1. gate and 2. garden sprinklers
# by Jan Dustin Tengdyantono
# 01/05/2021

#imports
import RPi.GPIO as GPIO
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import serial
import time

#initialization
port = serial.Serial("/dev/rfcomm0", baudrate=9600) # you need to connect to arduino bluetooth dongle first
host_name = '192.168.1.64'  # IP Address of Raspberry Pi - check using ifconfig
host_port = 8000 # enter port number that you want

#functions
def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)

def getTemperature():
    temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
    return temp

#class
class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _redirect(self, path):
        self.send_response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers()

    def do_GET(self):
        html = '''
           <html>
           <meta name="viewport" content="width=500">
           <body style="width:480; margin: 20px auto; background-color:lightgray;">
           <p><br></p>
           <h1>Tengdyantono's Home Server</h1>
           <font size="5">
           <p><br></p>
                Please click the buttons ONCE.
           <form action="/" method="POST">
               <input type="submit" name="submit" value="Click here to refresh" style="font-size : 20px;height:50px; width:460px" />
               
           </form>
           
           <form action="/" method="POST">
               <p> Gate : </p>
               <input type="submit" name="submit" value="Car" style="font-size : 20px; height:50px; width:150px" />
               <input type="submit" name="submit" value="People" style="font-size : 20px; height:50px; width:150px" />
               <input type="submit" name="submit" value="Close" style="font-size : 20px; height:50px; width:150px" />
           </form>



           <form action="/" method="POST">
               <p> Sprinkler System : </p>
               <input type="submit" name="submit" value="Front Lawn ON" style="font-size : 20px; height:50px ; width:229px" />
               <input type="submit" name="submit" value="Front Lawn OFF" style="font-size : 20px; height:50px ; width:229px" />
           </form>



           <form action="/" method="POST">
               <input type="submit" name="submit" value="Side Lawn ON" style="font-size : 20px;height:50px ; width:229px" />
               <input type="submit" name="submit" value="Side Lawn OFF" style="font-size : 20px;height:50px ; width:229px" />
           </form>
           <p><br></p>
            <p style="color:blue;font-size:11px;"> GPU temperature: {}</p>
            <p style="color:blue;font-size:11px;"> PT. Terang Empat Nusantara Gelora </p>
           </font>
           </body>
           </html>
        '''
        temp = getTemperature()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        post_data = post_data.split("=")[1]

        setupGPIO()

        if post_data == 'Front Lawn ON':
            GPIO.output(2, GPIO.LOW)
        elif post_data == 'Front Lawn OFF':
            GPIO.output(2, GPIO.HIGH)
        elif post_data == 'Side Lawn ON':
            GPIO.output(3, GPIO.LOW)
        elif post_data == 'Side Lawn OFF':
            GPIO.output(3, GPIO.HIGH)
        
        elif post_data == 'Car' or post_data == 'Close':
            port.write("1".encode())
            port.write("0".encode())

        elif post_data == 'People':
            port.write("2".encode())
            port.write("0".encode())

        elif post_data == 'Click here to refresh':
            pass 


        print("{} is pressed".format(post_data))
        self._redirect('/')  # Redirect back to the root url


# # # # # Main # # # # #

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()