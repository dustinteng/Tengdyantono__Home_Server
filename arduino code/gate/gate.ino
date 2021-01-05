// This file is intended to be a complimentary code to connect with the home server
// this file can open and close the front most gate by receiving serial data from python
// by Jan Dustin Tengdyantono
// 01/05/2020

#define gatePin 12 // to connect to relay
int num = 1;
int state; 
void setup() {
    
    
    pinMode(gatePin, OUTPUT);
    digitalWrite(gatePin, HIGH); //LOW IN RELAY = HIGH IN DIGITAL WRITE
    
    Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() { 
    if(Serial.available() > 0){
    // Checks whether data is comming from the serial port
    state = Serial.read(); // Reads the data from the serial port
    }

    if (state =='0'){
        
    }

    //one button press
    else if (state == '1') {
        digitalWrite(gatePin, LOW);
        delay(500);
        digitalWrite(gatePin, HIGH);
        delay(500);

    }

    // Opening gate 2 seconds wide (for people)
    else if (state == '2'){
        digitalWrite(gatePin, LOW);
        delay(500);
        digitalWrite(gatePin, HIGH);
        delay(2000);
        digitalWrite(gatePin, LOW);
        delay(500);
        digitalWrite(gatePin, HIGH);
    }

    }
