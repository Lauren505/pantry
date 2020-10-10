#include <Wire.h>

#include <HX711.h>
#include "DHT.h"

#define dhtPin 9     
#define dhtType DHT11 
// HX711
const int DT_PIN = 6;
const int SCK_PIN = 5;

const int DT_PIN2 = 10;
const int SCK_PIN2 = 11;

const int SWITCH_PIN = 2;

const int scale_factor = -368;
const int scale_factor2 = -382;


bool isOpen = 0;

int current_data[8] = {0};

int k = 9;

float previous_weight = 0;


HX711 scale;
HX711 scale2;

DHT dht(dhtPin, dhtType); // Initialize DHT sensor

void setup() {
  Serial.begin(9600);
  
  Wire.begin(0x04);
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  Wire.onRequest(send_data);

  //scale.begin();
  //delay(3000);
  //scale.begin();
  scale.begin(DT_PIN, SCK_PIN);
  scale2.begin(DT_PIN2, SCK_PIN2);

 // Serial.println("Before setting up the scale:"); 
 // Serial.println(scale.get_units(5), 0);  //未設定比例參數前的數值
  //Serial.println(scale2.get_units(5), 0);  //未設定比例參數前的數值

  scale.set_scale(scale_factor);       // 設定比例參數
  scale2.set_scale(scale_factor2);       // 設定比例參數

  scale.tare();               // 歸零
  scale2.tare();               // 歸零

 // Serial.println("After setting up the scale:"); 
 // Serial.println(scale.get_units(5), 0);  //設定比例參數後的數值
 // Serial.println(scale2.get_units(5), 0);  //設定比例參數後的數值

  //Serial.println("Readings:"); 

  dht.begin();//啟動DHT
  pinMode(SWITCH_PIN, INPUT);

}

void receiveEvent() {
  k = Wire.read();
}

void send_data(){
  Wire.write(current_data[k]);

  //Serial.println("--------------send----------------");
  //Serial.println(k);
  //Serial.println(current_data[k]);
  //Serial.println("--------------send----------------");

  if(k>3 && k<8) {
    current_data[k] = 0;
  }
}

void dht_update(){
  char* data;
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
  //Serial.println("無法從DHT傳感器讀取！");
  return;
  }
  /*Serial.print("濕度: ");
  Serial.print(h);
  Serial.print("%\t");
  Serial.print("攝氏溫度: ");
  Serial.print(t);
  Serial.println("*C\t");*/

  current_data[0] = int(h);
  current_data[1] = 100*h-100*int(h);
  current_data[2] = int(t);
  current_data[3] = 100*t-100*int(t);
}

void weight_update(){
  float current_weight = scale.get_units(10)+scale2.get_units(10);
  //Serial.print("current_weight: ");
  //Serial.println(current_weight);
  //Serial.print("previous_weight: ");
  //Serial.println(previous_weight);
  float weight_diff = current_weight-previous_weight;
  //Serial.print("diff: ");
  //Serial.println(weight_diff);
  if(weight_diff<0) current_data[4] = 1;
  else current_data[4] = 2;
  weight_diff = abs(weight_diff);
  current_data[5] = int(weight_diff);
  current_data[6] = 100*weight_diff - 100*int(weight_diff);

  previous_weight = current_weight;
}

void loop() {
  //int switchStatus = Serial.read();
  digitalWrite(12,HIGH);
  digitalWrite(13,LOW);

  int switchStatus = digitalRead(SWITCH_PIN);
  //Serial.print("switchStatus:");
  //Serial.println(switchStatus);
  bool refresh = 1;
  /*char mode;
  if(Serial.available()>0) mode = Serial.read();
  else mode = '0';
  Serial.print("mode:");
  Serial.println(mode);*/
  if(refresh==1)
  {
    dht_update();
    delay(1000);
  }
  if (switchStatus==1) {
    //Serial.println("opening");
    isOpen = 1;
  }

  if (switchStatus==0 && isOpen==1){
    //Serial.println(">>>>>>>>closing");
    isOpen = 0;
    current_data[7] = 1;
    weight_update();
  }
  /*if(switchStatus==0) //opening
  {
    isOpen = 1;
  }
  if(switchStatus==1 && isOpen==1) //closing
  {
    isOpen = 0;
    weight_update();
    delay(1000);
  }*/
  //delay(1000);

  //Serial.println("-----current----");
  //for(int i=0;i<8;i++) Serial.println(current_data[i]);
  //Serial.println("------end-------");
}
