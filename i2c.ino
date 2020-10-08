//#include <SoftwareSerial.h>

//SoftwareSerial mySerial(11,10); //(RX,TX)

//void setup() {
  // put your setup code here, to run once:
  //Serial.begin(9600);
  //mySerial.begin(9600);
//}

//void loop() {
  // put your main code here, to run repeatedly:
  //Serial.write("Dao");
  //Serial.print(mySerial.available());
  //delay(1000);
//}

#include <Wire.h>
 
// LED on pin 13

int k = 0;
 
void setup() {
  // Join I2C bus as slave with address 8
  Serial.begin(9600);
  Wire.begin(0x04);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  Wire.onRequest(send_data);
  
  // Setup pin 13 as output and turn LED off
}
 
// Function that executes whenever data is received from master
void receiveEvent() { // loop through all but the last
    k = Wire.read(); // receive byte as a character
}

void send_data(){
  int num[20] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};
  Wire.write(num[k]);
}
void loop() {
  delay(100);
}
