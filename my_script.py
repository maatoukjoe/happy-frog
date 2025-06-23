"""
Happy Frog - Generated CircuitPython Code
Educational HID Emulation Script

This code was automatically generated from a Happy Frog Script.
It demonstrates how to use CircuitPython for HID emulation.

⚠️ IMPORTANT: Use only for educational purposes and authorized testing!
"""

import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# Initialize HID devices
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# Educational note: This creates a virtual keyboard that the computer
# will recognize as a USB HID device. The keyboard can send keystrokes
# just like a physical keyboard would.

# Script Information:
# Source: C:/Users/bccha/projects/happy-frog/payloads/my_first_script.txt
# Total Commands: 15
# Total Lines: 16

# Main execution loop
def main():
    # Wait for system to recognize the device
    time.sleep(2)

    # Command 1: # My First Happy Frog Script
    #  My First Happy Frog Script

    # Command 2: # Educational example - opens Notepad and types a message
    #  Educational example - opens Notepad and types a message

    # Command 3: DELAY 2000
    time.sleep(2.0)  # Delay for 2000ms

    # Command 4: MOD r
    keyboard.press(Keycode.GUI)  # Press MOD
    keyboard.press(Keycode.R)  # Press r
    keyboard.release(Keycode.R)  # Release r
    keyboard.release(Keycode.GUI)  # Release MOD

    # Command 5: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 6: STRING notepad
    keyboard_layout.write("notepad")  # Type: notepad

    # Command 7: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 8: DELAY 1000
    time.sleep(1.0)  # Delay for 1000ms

    # Command 9: STRING Hello from Happy Frog Script!
    keyboard_layout.write("Hello from Happy Frog Script!")  # Type: Hello from Happy Frog Script!

    # Command 10: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 11: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 12: STRING This is my first automation script with Happy Frog 🐸.
    keyboard_layout.write("This is my first automation script with Happy Frog 🐸.")  # Type: This is my first automation script with Happy Frog 🐸.

    # Command 13: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 14: DELAY 1000
    time.sleep(1.0)  # Delay for 1000ms

    # Command 15: ALT F4
    keyboard.press(Keycode.ALT)  # Press ALT
    keyboard.press(Keycode.F4)  # Press F4
    keyboard.release(Keycode.F4)  # Release F4
    keyboard.release(Keycode.ALT)  # Release ALT


# Run the main function
if __name__ == '__main__':
    main()

"""
End of Happy Frog Generated Code

Educational Notes:
- This script demonstrates basic HID emulation techniques
- Always test in controlled environments
- Use responsibly and ethically
- Consider the security implications of automated input

For more information, visit: https://github.com/ZeroDumb/happy-frog
"""