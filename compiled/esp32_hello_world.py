/*
Happy Frog - ESP32 Generated Code
Educational HID Emulation Script

Device: ESP32
Processor: Dual-core Xtensa LX6
Framework: Arduino (ESP32)

This code was automatically generated from a Happy Frog Script.
Optimized for ESP32 with WiFi/Bluetooth capabilities.

⚠️ IMPORTANT: Use only for educational purposes and authorized testing!
*/

#include <BleKeyboard.h>  // ESP32 Bluetooth HID
#include <WiFi.h>  // ESP32 WiFi
#include <WebServer.h>  // ESP32 Web Server

// ESP32-specific configuration
BleKeyboard bleKeyboard("Happy Frog ESP32", "Happy Frog Team", 100);
WebServer server(80);  // Web server for remote control

void setup() {
  // Initialize ESP32 for wireless HID emulation
  Serial.begin(115200);  // ESP32 serial communication
  
  // Initialize Bluetooth HID
  bleKeyboard.begin();
  
  // ESP32: Wait for Bluetooth connection
  Serial.println("Waiting for Bluetooth connection...");
  while(!bleKeyboard.isConnected()) {
    delay(500);
  }
  Serial.println("Bluetooth connected!");
  
  // ESP32: Additional startup delay
  delay(2000);  // Wait for system to recognize device
}

void loop() {
  // Main execution - runs once
  executePayload();
  
  // ESP32: Maintain Bluetooth connection
  while(true) {
    bleKeyboard.isConnected();  // Keep connection alive
    delay(1000);
  }
}

void executePayload() {
  // Generated Happy Frog payload for ESP32

  // ESP32 Command: # Happy Frog Script - Hello World
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: # Simple educational example demonstrating basic automation
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: #
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: # Educational Purpose: Shows how to create a simple automation script
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: # that types text and performs basic keyboard operations
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: # Wait for system to recognize the device
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: DELAY 1000
  delay(1000);  // ESP32 delay: 1000ms

  // ESP32 Command: # Type a greeting message
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: STRING Hello, World! This is Happy Frog Script in action!
  bleKeyboard.print("Hello, World! This is Happy Frog Script in action!");  // ESP32 Bluetooth string input

  // ESP32 Command: ENTER
  bleKeyboard.press(KEY_ENTER);  // ESP32 key press: ENTER
  bleKeyboard.release(KEY_ENTER);  // ESP32 key release: ENTER

  // ESP32 Command: # Wait a moment
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: DELAY 500
  delay(500);  // ESP32 delay: 500ms

  // ESP32 Command: # Type another message
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: STRING This demonstrates basic text input automation.
  bleKeyboard.print("This demonstrates basic text input automation.");  // ESP32 Bluetooth string input

  // ESP32 Command: ENTER
  bleKeyboard.press(KEY_ENTER);  // ESP32 key press: ENTER
  bleKeyboard.release(KEY_ENTER);  // ESP32 key release: ENTER

  // ESP32 Command: # Wait and type more
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: DELAY 500
  delay(500);  // ESP32 delay: 500ms

  // ESP32 Command: STRING Happy Frog Script makes automation simple and educational!
  bleKeyboard.print("Happy Frog Script makes automation simple and educational!");  // ESP32 Bluetooth string input

  // ESP32 Command: ENTER
  bleKeyboard.press(KEY_ENTER);  // ESP32 key press: ENTER
  bleKeyboard.release(KEY_ENTER);  // ESP32 key release: ENTER

  // ESP32 Command: # Final message
  bleKeyboard.press(KEY_COMMENT);  // ESP32 key press: COMMENT
  bleKeyboard.release(KEY_COMMENT);  // ESP32 key release: COMMENT

  // ESP32 Command: DELAY 500
  delay(500);  // ESP32 delay: 500ms

  // ESP32 Command: STRING Remember: Use automation responsibly and ethically!
  bleKeyboard.print("Remember: Use automation responsibly and ethically!");  // ESP32 Bluetooth string input

  // ESP32 Command: ENTER
  bleKeyboard.press(KEY_ENTER);  // ESP32 key press: ENTER
  bleKeyboard.release(KEY_ENTER);  // ESP32 key release: ENTER

  // End of Happy Frog payload
}

/*
End of Happy Frog Generated Code for ESP32

Educational Notes:
- ESP32 provides wireless HID emulation capabilities
- Dual-core processor enables complex automation scenarios
- WiFi and Bluetooth support IoT security research
- Ideal for wireless attack demonstrations and education

For more information, visit: https://github.com/ZeroDumb/happy-frog
*/