#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "Rakshak v3";
const char* password = "Rakshak@123";
const char* serverUrl = "http://localhost:5050";

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  Serial.println("Connected to WiFi");
}

void loop() {
  // Fetch ECU information
  float rpm = ...;  // Replace with actual ECU data
  float vehicleSpeed = ...;
  float coolantTemp = ...;
  float throttlePos = ...;
  float engineLoad = ...;

  String licensePlate = "../finder.py"; 
  
  float distance = ...; 

  // Create JSON object
  StaticJsonDocument<200> doc;
  doc["RPM"] = rpm;
  doc["VehicleSpeed"] = vehicleSpeed;
  doc["CoolantTemp"] = coolantTemp;
  doc["ThrottlePos"] = throttlePos;
  doc["EngineLoad"] = engineLoad;
  doc["LicensePlate"] = licensePlate;
  doc["Distance"] = distance;

  // Serialize JSON to string
  String jsonString;
  serializeJson(doc, jsonString);

  // Send data to server
  HTTPClient http;
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(jsonString);

  if (httpResponseCode > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);
    String payload = http.getString();
    Serial.println(payload);
  } else {
    Serial.print("Error sending POST request. HTTP Error code: ");
    Serial.println(httpResponseCode);
  }

  http.end();

  delay(5000); 
}
