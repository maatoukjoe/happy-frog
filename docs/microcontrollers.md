# Microcontroller Setup Guide

This guide covers the setup and configuration of microcontrollers for use with Happy Frog. The focus is on affordable, educational-friendly devices.

## 🎯 Recommended Hardware

### Seeed Xiao RP2040 (Primary Recommendation)

**Why Choose the Xiao RP2040:**
- ✅ **Affordable**: ~$5-8 USD
- ✅ **Powerful**: Dual-core ARM Cortex-M0+ at 133MHz
- ✅ **CircuitPython Support**: Excellent compatibility
- ✅ **USB-C**: Modern connectivity
- ✅ **Small Form Factor**: Easy to work with
- ✅ **Educational**: Great for learning

**Specifications:**
- **Processor**: Raspberry Pi RP2040 (Dual-core ARM Cortex-M0+)
- **Clock Speed**: 133MHz
- **Memory**: 264KB SRAM, 2MB Flash
- **USB**: USB-C connector
- **GPIO**: 11 digital pins, 4 analog pins
- **Size**: 21 x 17.5mm
- **Price**: ~$5-8 USD

**Where to Buy:**
- [Seeed Studio](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html)
- [Amazon](https://www.amazon.com/s?k=seeed+xiao+rp2040)
- [Adafruit](https://www.adafruit.com/product/4864)

## 🔧 Setup Instructions

### Step 1: Install CircuitPython

1. **Download CircuitPython Firmware**
   - Visit [circuitpython.org](https://circuitpython.org/)
   - Find your board in the list
   - Download the appropriate `.uf2` file

2. **Enter Bootloader Mode**
   - Connect your Xiao RP2040 via USB-C
   - Double-tap the reset button
   - The device should appear as a USB drive named `RPI-RP2`

3. **Flash CircuitPython**
   - Copy the downloaded `.uf2` file to the `RPI-RP2` drive
   - The device will automatically restart
   - You should now see a `CIRCUITPY` drive

4. **Verify Installation**
   - Open the `CIRCUITPY` drive
   - You should see `boot_out.txt` and `code.py` files
   - The `code.py` file is where your Happy Frog code will go

### Step 2: Install Required Libraries

1. **Download CircuitPython Library Bundle**
   - Go to [circuitpython.org/libraries](https://circuitpython.org/libraries)
   - Download the latest library bundle

2. **Extract and Copy Libraries**
   - Extract the downloaded bundle
   - Create a `lib` folder on your `CIRCUITPY` drive
   - Copy the following folders to `lib`:
     - `adafruit_hid`
     - `adafruit_hid.keyboard`
     - `adafruit_hid.keyboard_layout_us`
     - `adafruit_hid.keycode`

3. **Verify Library Installation**
   - Your `CIRCUITPY` drive should now have:
     ```
     CIRCUITPY/
     ├── lib/
     │   ├── adafruit_hid/
     │   ├── adafruit_hid.keyboard/
     │   ├── adafruit_hid.keyboard_layout_us/
     │   └── adafruit_hid.keycode/
     ├── boot_out.txt
     └── code.py
     ```

### Step 3: Test Basic Functionality

1. **Create a Test Script**
   Create a file called `test.py` on your `CIRCUITPY` drive:

   ```python
   import time
   import usb_hid
   from adafruit_hid.keyboard import Keyboard
   from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
   from adafruit_hid.keycode import Keycode

   # Initialize HID devices
   keyboard = Keyboard(usb_hid.devices)
   keyboard_layout = KeyboardLayoutUS(keyboard)

   def main():
       print("Testing HID functionality...")
       time.sleep(2)
       
       # Type a test message
       keyboard_layout.write("HID Test - Hello World!")
       time.sleep(0.5)
       
       # Press Enter
       keyboard.press(Keycode.ENTER)
       keyboard.release(Keycode.ENTER)
       
       print("Test completed!")

   if __name__ == "__main__":
       main()
   ```

2. **Rename and Test**
   - Rename `test.py` to `code.py`
   - The device will automatically run the code
   - Connect to a test computer and observe the output

## 🐸 Using Happy Frog with Your Device

### Step 1: Generate CircuitPython Code

```bash
# Generate code from a Ducky Script
happy-frog payloads/hello_world.txt -o output.py
```

### Step 2: Upload to Device

1. **Copy Generated Code**
   - Copy the generated `output.py` file
   - Paste it as `code.py` on your `CIRCUITPY` drive
   - The device will automatically restart and run the code

2. **Test in Controlled Environment**
   - Connect to a test computer
   - Wait for device recognition
   - Observe the automated behavior
   - **Always test safely!**

### Step 3: Customize and Experiment

1. **Modify the Code**
   - Edit `code.py` directly on the device
   - Changes take effect immediately
   - No need to recompile or reflash

2. **Add Safety Features**
   - Implement startup delays
   - Add confirmation prompts
   - Include error handling

## 🔌 Alternative Microcontrollers

### Raspberry Pi Pico
- **Pros**: Same RP2040 chip, official Raspberry Pi product
- **Cons**: Slightly larger, more expensive
- **Setup**: Similar to Xiao RP2040

### Adafruit ItsyBitsy RP2040
- **Pros**: High-quality, good documentation
- **Cons**: More expensive (~$9-12)
- **Setup**: Same CircuitPython process

### ESP32-S2/S3 Boards
- **Pros**: WiFi capability, more features
- **Cons**: More complex setup, larger size
- **Setup**: Requires different firmware

### Arduino Pro Micro (ATmega32U4)
- **Pros**: Very small, widely available
- **Cons**: Limited memory, different programming
- **Setup**: Requires Arduino IDE and custom libraries

## 🛡️ Security Considerations

### Physical Security
- **Device Storage**: Keep devices in secure locations
- **Access Control**: Limit who can access your devices
- **Inventory**: Keep track of all devices

### Operational Security
- **Testing Environment**: Use isolated test systems
- **Network Isolation**: Disconnect from networks during testing
- **Monitoring**: Watch for unexpected behavior

### Educational Best Practices
- **Documentation**: Keep detailed records of all activities
- **Authorization**: Always get proper permission
- **Responsible Disclosure**: Report any vulnerabilities found

## 🐛 Troubleshooting

### Common Issues

#### Device Not Recognized
- **Check USB Cable**: Try different cables
- **Driver Issues**: Install appropriate drivers
- **Bootloader Mode**: Double-tap reset button
- **CircuitPython**: Verify firmware installation

#### Code Not Running
- **File Name**: Ensure file is named `code.py`
- **Syntax Errors**: Check for Python syntax issues
- **Library Issues**: Verify all libraries are installed
- **Memory**: Check available memory

#### HID Not Working
- **Library Installation**: Verify `adafruit_hid` is installed
- **Device Recognition**: Wait for system to recognize device
- **Permissions**: Check system permissions
- **Timing**: Add appropriate delays

### Debugging Tips

1. **Serial Output**: Connect to serial monitor for debug output
2. **LED Indicators**: Watch onboard LEDs for status
3. **File System**: Check files on `CIRCUITPY` drive
4. **Library Versions**: Ensure compatible library versions

## 📚 Educational Resources

### CircuitPython Learning
- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Adafruit Learning System](https://learn.adafruit.com/)
- [CircuitPython Examples](https://github.com/adafruit/Adafruit_Learning_System_Guides)

### Microcontroller Basics
- [MicroPython Documentation](https://docs.micropython.org/)
- [Raspberry Pi Pico Guide](https://www.raspberrypi.org/documentation/pico/)
- [Embedded Systems Tutorials](https://www.embedded.com/)

### HID and USB
- [USB HID Specification](https://www.usb.org/document-library/device-class-definition-hid-111)
- [HID Usage Tables](https://www.usb.org/document-library/hid-usage-tables-122)
- [USB Device Classes](https://www.usb.org/defined-class-codes)

## 🔮 Future Enhancements

### Planned Features
- **WiFi Capability**: Remote triggering via network
- **Bluetooth Support**: Wireless HID emulation
- **Advanced Scripting**: More complex automation
- **GUI Interface**: Visual script editor

### Community Contributions
- **New Device Support**: Additional microcontrollers
- **Enhanced Libraries**: More HID capabilities
- **Educational Content**: Tutorials and examples
- **Security Tools**: Defensive applications

## ⚖️ Legal and Ethical Reminders

**Remember:**
- Use only for educational purposes
- Test only on systems you own or have permission to test
- Follow all applicable laws and regulations
- Report vulnerabilities responsibly
- Share knowledge ethically

**This tool is designed for learning and authorized testing. Misuse is not supported and may be illegal.**

---

**Happy coding and learning! 🐸✨** 