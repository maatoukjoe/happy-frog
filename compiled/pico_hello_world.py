"""
Happy Frog - Raspberry Pi Pico Generated Code
Educational HID Emulation Script

Device: Raspberry Pi Pico
Processor: RP2040
Framework: CircuitPython

This code was automatically generated from a Happy Frog Script.
Optimized for Raspberry Pi Pico with RP2040 processor.

⚠️ IMPORTANT: Use only for educational purposes and authorized testing!
"""

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

# Initialize HID devices for Raspberry Pi Pico
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
mouse = Mouse(usb_hid.devices)

# Pico-specific optimizations
# Fast startup - Pico boots in ~100ms
time.sleep(0.1)  # Minimal startup delay

    # Pico Command: # Happy Frog Script - Hello World
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: # Simple educational example demonstrating basic automation
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: #
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: # Educational Purpose: Shows how to create a simple automation script
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: # that types text and performs basic keyboard operations
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: # Wait for system to recognize the device
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: DELAY 1000
    time.sleep(1.0)  # Delay: 1000ms

    # Pico Command: # Type a greeting message
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: STRING Hello, World! This is Happy Frog Script in action!
    keyboard_layout.write("Hello, World! This is Happy Frog Script in action!")  # Pico string input: Hello, World! This is Happy Frog Script in action!

    # Pico Command: ENTER
    keyboard.press(Keycode.ENTER)  # Pico key press: ENTER
    keyboard.release(Keycode.ENTER)  # Pico key release: ENTER

    # Pico Command: # Wait a moment
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: DELAY 500
    time.sleep(0.5)  # Delay: 500ms

    # Pico Command: # Type another message
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: STRING This demonstrates basic text input automation.
    keyboard_layout.write("This demonstrates basic text input automation.")  # Pico string input: This demonstrates basic text input automation.

    # Pico Command: ENTER
    keyboard.press(Keycode.ENTER)  # Pico key press: ENTER
    keyboard.release(Keycode.ENTER)  # Pico key release: ENTER

    # Pico Command: # Wait and type more
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: DELAY 500
    time.sleep(0.5)  # Delay: 500ms

    # Pico Command: STRING Happy Frog Script makes automation simple and educational!
    keyboard_layout.write("Happy Frog Script makes automation simple and educational!")  # Pico string input: Happy Frog Script makes automation simple and educational!

    # Pico Command: ENTER
    keyboard.press(Keycode.ENTER)  # Pico key press: ENTER
    keyboard.release(Keycode.ENTER)  # Pico key release: ENTER

    # Pico Command: # Final message
    keyboard.press(Keycode.COMMENT)  # Pico key press: COMMENT
    keyboard.release(Keycode.COMMENT)  # Pico key release: COMMENT

    # Pico Command: DELAY 500
    time.sleep(0.5)  # Delay: 500ms

    # Pico Command: STRING Remember: Use automation responsibly and ethically!
    keyboard_layout.write("Remember: Use automation responsibly and ethically!")  # Pico string input: Remember: Use automation responsibly and ethically!

    # Pico Command: ENTER
    keyboard.press(Keycode.ENTER)  # Pico key press: ENTER
    keyboard.release(Keycode.ENTER)  # Pico key release: ENTER

"""
End of Happy Frog Generated Code for Raspberry Pi Pico

Educational Notes:
- Raspberry Pi Pico provides excellent HID emulation capabilities
- RP2040 processor offers dual-core performance
- CircuitPython makes development and testing easy
- Low cost makes it ideal for educational projects

For more information, visit: https://github.com/ZeroDumb/happy-frog
"""