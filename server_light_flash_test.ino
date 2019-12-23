#include <ESP8266WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

const char* ssid = "ThunderDome";
const char* password = "2MayEnter";
const uint16_t port = 8091;
const char* host = "192.168.1.23";
uint8_t LED1pin = D7;
bool LED1status = LOW;
uint8_t LED2pin = D6;
bool LED2status = LOW;
const long utcOffsetInSeconds = -18000;
//const long utcOffsetInSeconds = 0;
const int analogInPin = A0;
int sensorValue = 0;
int outputValue = 0;
long last_pressed = 0;
long epoch_time = 0;
int current_hour = 0;
int test_hour = 0;

WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP,"pool.ntp.org",utcOffsetInSeconds);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LED1pin,OUTPUT);
  pinMode(LED2pin,OUTPUT);

  WiFi.begin(ssid,password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(2000);
    Serial.print("Trying to connect to: ");
    Serial.println(ssid);
  }
  Serial.print("WiFi Connected with IP: ");
  Serial.println(WiFi.localIP());
  timeClient.begin();
  timeClient.update();
  Serial.print("Beginning the Time Client at: ");
  Serial.println(timeClient.getFormattedTime());
  current_hour = timeClient.getHours();
  epoch_time = timeClient.getEpochTime();
  if (last_pressed == 0) {
    last_pressed = epoch_time - 18000;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  WiFiClient client;
  int x = epoch_time % 20;
  if (x == 0) {
    if (!client.connect(host,port)) {
      Serial.print("Failed to connect to: ");
      Serial.println(host);
      delay(1000);
      return;
    }
     client.print("EpochCheck: ");
     client.println(timeClient.getEpochTime());
  }
  Serial.print("I'm going to pause for 2 seconds...Successful connection to: ");
  delay(2000);
  Serial.println(host);
  Serial.print("Last pressed: ");
  Serial.println(last_pressed);
  Serial.print("Epoch Time: ");
  Serial.println(epoch_time);
  epoch_time = timeClient.getEpochTime();
  test_hour = check_hour();
  Serial.print("Hour: ");
  Serial.println(test_hour);
  test_hour = epoch_time - last_pressed;
  Serial.print("last pressed delta: ");
  Serial.println(test_hour);
  
  //if (last_pressed < (epoch_time + 43600) || ((check_hour() == 1 && ((epoch_time - last_pressed) > 18000)))) {
//if (last_pressed > (epoch_time + 43600)) {
//if (((check_hour() == 0 && ((epoch_time - last_pressed) > 18000)))) {
if ((epoch_time > (last_pressed + 43200)) || check_hour() == 1 && ((epoch_time - last_pressed) > 18000)   ) {  
    flash_lights();
    Serial.print("Successful connection to: ");
    Serial.println(host);
    Serial.print("Last pressed: ");
    Serial.println(last_pressed);
    Serial.print("Epoch Time: ");
    Serial.println(epoch_time);
    epoch_time = timeClient.getEpochTime();
    delay(100);
    if (check_button() == 0) {
     //timeClient.update();
     if (!client.connect(host,port)) {
      Serial.print("Failed to connect to: ");
      Serial.println(host);
      delay(1000);
      return;
     }
     Serial.print("Button was pressed at: ");
     Serial.print(timeClient.getFormattedTime());
//     client.print("Button pressed at: ");
     client.println("");
     client.print(timeClient.getFormattedTime());
     client.print(" --- ");
     client.println(timeClient.getEpochTime());
     last_pressed = timeClient.getEpochTime();
     delay(1000);
    }
  //  else {

  //  }
  }

}

int check_button() {
  sensorValue = analogRead(analogInPin);
  outputValue = map(sensorValue,0,1024,0,255);
  if (outputValue < 100) {
   // Serial.println("value is less than 100");
    return 0;
  }
  else {
   // Serial.println("Value is more than 100");
    return 1;
  }
}

int check_hour() {
  int hour = timeClient.getHours();
  Serial.print("The hour is: ");
  Serial.println(hour);
  if ((hour > 5 && hour < 11) || (hour > 16 && hour < 2300)) {
    return 1;
  }
  else {
    return 0;
  }
}


void turn_lights_off() {
  LED1status = LOW;
  LED2status = LOW;
  digitalWrite(LED1pin,LED1status);  
  digitalWrite(LED2pin,LED2status);
}

void flash_lights() {
  while (check_button() == 1) {
    LED1status = HIGH;
    LED2status = HIGH;
    digitalWrite(LED1pin,LED1status);  
    digitalWrite(LED2pin,LED2status);
    delay(200);
    LED1status = LOW;
    LED2status = LOW;
    digitalWrite(LED1pin,LED1status);  
    digitalWrite(LED2pin,LED2status);
    delay(200);
  }
}
