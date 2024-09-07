/*
 *  This sketch demonstrates how to scan WiFi networks.
 *  The API is based on the Arduino WiFi Shield library, but has significant changes as newer WiFi functions are supported.
 *  E.g. the return value of `encryptionType()` different because more modern encryption is supported.
 */
#include "WiFi.h"

void setup() {
  Serial.begin(115200);
  delay(10);

  // Set WiFi to station mode and disconnect from an AP if it was previously connected.
  WiFi.begin("huawei", "sanjana123");

  while (WiFi.status() != WL_CONNECTED) 
  {
    delay(500);
    Serial.println(".");

  }

  Serial.println("Connected...!!!");
  Serial.println(WiFi.localIP());
}

void loop() {
  
}
