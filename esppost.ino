//code by kishore for more code visit kishore.cc :)
#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include <ArduinoJson.h>

StaticJsonDocument<256> api;  //Declaring static JSON buffer named api
void setup() {

  Serial.begin(115200);                            //Serial connection
  WiFi.begin("K", "kingkise");   //WiFi connection

  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion

    delay(500);
    Serial.println("Waiting for connection");

  }
 

}

void loop() {

  if (WiFi.status() == WL_CONNECTED) { //Check WiFi connection status
    char device[10]="Kise";
    api["deviceid"] = device; // for dynamic values
    api["senval1"] = "89.34";
    api["lati"] = "1980.765";
    api["longi"] = "0.3823";
    api["uptime"] = "active";
    api["status"] = "online";

    char orgapi[300];//  for converting to json
    serializeJson(api, orgapi);   // serialize regular json to serialized json
    Serial.println(orgapi);

    HTTPClient http;    //Declare object of class HTTPClient

    http.begin("http://785a15ed.ngrok.io/api");      //Specify request destination
    http.addHeader("Content-Type", "application/json");  //Specify content-type header

    int httpCode = http.POST(orgapi);   //Send the request
    String payload = http.getString();          //Get the response payload

    Serial.println(httpCode);   //Print HTTP return code
    Serial.println(payload);    //Print request response payload

    http.end();  //Close connection

  } else {

    Serial.println("Error in WiFi connection");

  }

  delay(20000);  //Send a request every 20 seconds

}
