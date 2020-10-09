#include <Wire.h>

#include <HX711.h>
#include "DHT.h"

#define dhtPin 8     
#define dhtType DHT11 
// HX711
const int DT_PIN = 6;
const int SCK_PIN = 5;
const int SWITCH_PIN = 2;

const int scale_factor = -200;

bool isOpen = 0;

int k = 999;

int current_data[6] = {0};

HX711 scale;
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
  Serial.println("Before setting up the scale:"); 
  Serial.println(scale.get_units(5), 0);  //未設定比例參數前的數值
  scale.set_scale(scale_factor);       // 設定比例參數
  scale.tare();               // 歸零
  Serial.println("After setting up the scale:"); 
  Serial.println(scale.get_units(5), 0);  //設定比例參數後的數值
  Serial.println("Readings:"); 

  dht.begin();//啟動DHT
  pinMode(SWITCH_PIN, INPUT);
  
}

void receiveEvent() {
  k = Wire.read();
}

void send_data(){
  Wire.write(current_data[k]);

  Serial.println("------send------");
  Serial.println(k);
  Serial.println(current_data[k]);

  Serial.println("-----current----");
  for(int i=0;i<6;i++) Serial.println(current_data[i]);
  Serial.println("------end-------");

  if(k==4 || k==5) {
    current_data[4] = 0;
    current_data[5] = 0;
  }


  
}

void dht_update(){
  char* data;
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  if (isnan(h) || isnan(t)) {
  Serial.println("無法從DHT傳感器讀取！");
  return;
  }
  Serial.print("濕度: ");
  Serial.print(h);
  Serial.print("%\t");
  Serial.print("攝氏溫度: ");
  Serial.print(t);
  Serial.println("*C\t");

  current_data[0] = int(h);
  current_data[1] = 100*h-100*int(h);
  current_data[2] = int(t);
  current_data[3] = 100*t-100*int(t);
  send_data();
}

void weight_update(){
  float current_weight = scale.get_units(10);
  Serial.println("----weight------");
  Serial.println(current_weight);
  Serial.println("----------------");

  current_data[4] = int(current_weight);
  current_data[5] = 100*current_weight - 100*int(current_weight);
  /*float weight_10 = 0;  
    for(int i=0;i<10;i++){
    float w = scale.Get_Weight();
    Serial.println(w);
    weight_10 += w;
    delay(100);
  }
  weight_10 /= 10.0;
  Serial.print("Scale number:  ");
  Serial.println(weight_10*(-1));

  current_data[4] = int(abs(weight_10));
  current_data[5] = abs(int(abs(weight_10))*100 - abs(weight_10)*100);*/

  

  send_data();
}

void loop() {
  //int switchStatus = Serial.read();
  int switchStatus = digitalRead(SWITCH_PIN);
  Serial.println(switchStatus);
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
  if(switchStatus==0) //opening
  {
    isOpen = 1;
  }
  if(switchStatus==1 && isOpen==1) //closing
  {
    isOpen = 0;
    weight_update();
    delay(1000);
  }
}
