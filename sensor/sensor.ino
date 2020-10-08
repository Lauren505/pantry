#include "HX711.h"
#include "DHT.h"

#define dhtPin 8     
#define dhtType DHT11 
// HX711 接線設定
const int DT_PIN = 6;
const int SCK_PIN = 5;
const int SWITCH_PIN = 2;
const int sample_weight = 150;  //基準物品的真實重量(公克)

HX711 scale;
DHT dht(dhtPin, dhtType); // Initialize DHT sensor

void setup() {
  Serial.begin(9600);
  scale.begin(DT_PIN, SCK_PIN);
  scale.set_scale();  // 開始取得比例參數
  scale.tare();
  Serial.println("Nothing on it.");
  Serial.println(scale.get_units(10));
  Serial.println("Please put sapmple object on it..."); //提示放上基準物品

  dht.begin();//啟動DHT
  pinMode(SWITCH_PIN, INPUT);
  
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
}

void weight_update(){
  float current_weight=scale.get_units(10);  // 取得10次數值的平均
  float scale_factor=(current_weight/sample_weight);  
  Serial.print("Scale number:  ");
  Serial.println(scale_factor,0);  // 顯示比例參數，記起來，以便用在正式的程式中
}

void loop() {
  //int switchStatus = digitalRead(SWITCH_PIN);
  int switchStatus = Serial.read();
  Serial.println(switchStatus);
  bool isOpen = 0;
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
  if(switchStatus=='0') //opening
  {
    isOpen = 1;
  }
  if(switchStatus=='1' && isOpen==1) //closing
  {
    isOpen = 0;
    weight_update();
  }
}
