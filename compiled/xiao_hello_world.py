"""
Happy Frog - Seeed Xiao RP2040 Generated Code
Educational HID Emulation Script

Device: Seeed Xiao RP2040
Processor: RP2040
Framework: CircuitPython

This code was automatically generated from a Happy Frog Script.
Optimized for Seeed Xiao RP2040 with CircuitPython.

⚠️ IMPORTANT: Use only for educational purposes and authorized testing!
"""

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

def main():
    # Wait for system to recognize the device
    time.sleep(2)
    # Xiao RP2040 Command: # Happy Frog Script - Hello World
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: # Simple educational example demonstrating basic automation
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: #
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: # Educational Purpose: Shows how to create a simple automation script
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: # that types text and performs basic keyboard operations
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: # Wait for system to recognize the device
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: DELAY 1000
    time.sleep(1.000)  # Delay 1000ms

    # Xiao RP2040 Command: # Type a greeting message
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: STRING Hello, World! This is Happy Frog Script in action!
    keyboard_layout.write("Hello, World! This is Happy Frog Script in action!")

    # Xiao RP2040 Command: ENTER
    keyboard.press(Keycode.ENTER)
    keyboard.release(Keycode.ENTER)

    # Xiao RP2040 Command: # Wait a moment
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: DELAY 500
    time.sleep(0.500)  # Delay 500ms

    # Xiao RP2040 Command: # Type another message
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: STRING This demonstrates basic text input automation.
    keyboard_layout.write("This demonstrates basic text input automation.")

    # Xiao RP2040 Command: ENTER
    keyboard.press(Keycode.ENTER)
    keyboard.release(Keycode.ENTER)

    # Xiao RP2040 Command: # Wait and type more
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: DELAY 500
    time.sleep(0.500)  # Delay 500ms

    # Xiao RP2040 Command: STRING Happy Frog Script makes automation simple and educational!
    keyboard_layout.write("Happy Frog Script makes automation simple and educational!")

    # Xiao RP2040 Command: ENTER
    keyboard.press(Keycode.ENTER)
    keyboard.release(Keycode.ENTER)

    # Xiao RP2040 Command: # Final message
    keyboard.press(Keycode.COMMENT)
    keyboard.release(Keycode.COMMENT)

    # Xiao RP2040 Command: DELAY 500
    time.sleep(0.500)  # Delay 500ms

    # Xiao RP2040 Command: STRING Remember: Use automation responsibly and ethically!
    keyboard_layout.write("Remember: Use automation responsibly and ethically!")

    # Xiao RP2040 Command: ENTER
    keyboard.press(Keycode.ENTER)
    keyboard.release(Keycode.ENTER)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'Error during execution: {e}')
        keyboard.release_all()
    finally:
        print('Happy Frog execution completed.')