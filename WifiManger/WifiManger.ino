#include <WiFiManager.h>

void setup() 
{
  Serial.begin(115200);

  WiFiManager wm;

  bool res = wm.autoConnect("My ESP32", "12345678");  //this will check is there any Accesspoint with this credential or it try to make this access point
  if (!res)   //if you haven't a name (Like My ESP32) or password is wrong. This will give boolean of 0 and print failed
  {
    Serial.println("Failed");
    ESP.restart();
  }
  else
  {
    Serial.println("Done!!!");
  }

}

void loop() 
{
  
}
