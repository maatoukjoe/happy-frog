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
# Source: test_safe_mode.txt
# Total Commands: 9
# Total Lines: 10

# Main execution loop
def main():
    # Wait for system to recognize the device
    time.sleep(2)

    # Command 1: # Test Safe Mode Functionality
    #  Test Safe Mode Functionality

    # Command 2: SAFE_MODE ON
    # SAFE_MODE: Enabled safe mode restrictions
    safe_mode = true

    # Command 3: DELAY 1000
    time.sleep(1.0)  # Delay for 1000ms

    # Command 4: STRING Hello World
    keyboard_layout.write("Hello World")  # Type: Hello World

    # Command 5: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 6: SAFE_MODE OFF
    # SAFE_MODE: Disabled safe mode restrictions
    safe_mode = false

    # Command 7: STRING No comments
    keyboard_layout.write("No comments")  # Type: No comments

    # Command 8: SAFE_MODE ON
    # SAFE_MODE: Enabled safe mode restrictions
    safe_mode = true

    # Command 9: STRING Back to educational mode
    keyboard_layout.write("Back to educational mode")  # Type: Back to educational mode


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