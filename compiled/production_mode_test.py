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
# Source: test_production_mode.txt
# Total Commands: 8
# Total Lines: 9

# Main execution loop
def main():
    # Wait for system to recognize the device
    time.sleep(2)

    # Command 1: SAFE_MODE OFF
    # SAFE_MODE: Disabled safe mode restrictions
    safe_mode = false

    # Command 2: DELAY 1000
    time.sleep(1.0)  # Delay for 1000ms

    # Command 3: STRING Clean production code
    keyboard_layout.write("Clean production code")  # Type: Clean production code

    # Command 4: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 5: MOD r
    keyboard.press(Keycode.GUI)  # Press MOD
    keyboard.press(Keycode.R)  # Press r
    keyboard.release(Keycode.R)  # Release r
    keyboard.release(Keycode.GUI)  # Release MOD

    # Command 6: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 7: STRING notepad
    keyboard_layout.write("notepad")  # Type: notepad

    # Command 8: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER


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