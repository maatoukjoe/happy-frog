# 🐸 Hello Happy Frog! - Complete Beginner's Guide

Welcome to Happy Frog! This guide will walk you through building your first HID (Human Interface Device) emulation device from scratch. Whether you're a cybersecurity student, hobbyist, or educator, this guide will get you up and running safely and legally.

## ⚠️ Important Legal and Ethical Notice

**Before you begin, you MUST understand:**

✅ **Permitted Uses:**
- Educational cybersecurity labs
- Authorized penetration testing with written permission
- Security research on systems you own
- Teaching cybersecurity concepts
- Red team exercises in controlled environments

❌ **Prohibited Uses:**
- Unauthorized access to any systems
- Malicious attacks or cybercrime
- Testing without explicit permission
- Any illegal activities

**By using Happy Frog, you accept full responsibility for ensuring your use is legal and ethical.**

---

## 🎯 What You'll Build

You'll create a device that can:
- Emulate a USB keyboard
- Automate typing and key presses
- Run educational cybersecurity scripts
- Demonstrate HID attack concepts (for defense)

**Think of it as a "smart USB keyboard" that can type automatically!**

---

## 📋 What You Need

### Hardware (Choose One)

#### 🥇 **Recommended: Seeed Xiao RP2040** (~$5-8)
- **Why**: Affordable, powerful, easy to use
- **Buy from**: [Seeed Studio](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html) | [Amazon](https://www.amazon.com/s?k=seeed+xiao+rp2040) | [Adafruit](https://www.adafruit.com/product/4864)
- **Specs**: Dual-core ARM, 264KB RAM, 2MB Flash, USB-C

#### 🥈 **Alternative: Raspberry Pi Pico** (~$4-6)
- **Why**: Official Raspberry Pi product, same chip as Xiao
- **Buy from**: [Raspberry Pi Store](https://www.raspberrypi.com/products/raspberry-pi-pico/) | [Amazon](https://www.amazon.com/s?k=raspberry+pi+pico)
- **Specs**: Same RP2040 chip, slightly larger form factor

#### 🥉 **Budget Option: DigiSpark** (~$2-4)
- **Why**: Ultra-cheap, very small
- **Buy from**: [Amazon](https://www.amazon.com/s?k=digispark+attiny85) | [eBay](https://www.ebay.com/sch/i.html?_nkw=digispark+attiny85)
- **Specs**: ATtiny85, 8KB flash, 512B RAM

#### 🔥 **Advanced Option: EvilCrow-Cable** (~$15-30)
- **Why**: Specialized BadUSB device with built-in USB-C connectors
- **Buy from**: [Rabbit-Labs](https://rabbit-labs.com/) | [DIY Build](https://github.com/joelsernamoreno/EvilCrow-Cable/blob/master/README.md)
- **Specs**: ATtiny85, 8KB flash, 512B RAM, built-in USB-C
- **Note**: Advanced users only - designed for cybersecurity research

### Software Requirements

- **Computer**: Windows, Mac, or Linux
- **Python**: Version 3.7 or higher
- **USB Cable**: USB-C (Xiao/Pico) or Micro-USB (DigiSpark)
- **Text Editor**: VS Code, Notepad++, or any text editor

---

## 🚀 Step-by-Step Setup

### Step 1: Install Happy Frog

1. **Open your terminal/command prompt**

2. **Clone the repository:**
   ```bash
   git clone https://github.com/ZeroDumb/happy-frog.git
   cd happy-frog
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   pip install -e .
   ```

4. **Verify installation:**
   ```bash
   python main.py --help
   ```
   You should see the Happy Frog banner and help information.

### Step 2: Prepare Your Microcontroller

#### For Seeed Xiao RP2040 (Recommended)

1. **Download CircuitPython:**
   - Go to [circuitpython.org](https://circuitpython.org/)
   - Find "Seeed XIAO RP2040" in the board list
   - Download the `.uf2` file

2. **Enter bootloader mode:**
   - Connect your Xiao RP2040 via USB-C
   - **Double-tap the reset button** (small button on the board)
   - Your computer should show a new USB drive named `RPI-RP2`

3. **Install CircuitPython:**
   - Copy the downloaded `.uf2` file to the `RPI-RP2` drive
   - The device will restart automatically
   - You should now see a `CIRCUITPY` drive

4. **Install required libraries:**
   - Go to [circuitpython.org/libraries](https://circuitpython.org/libraries)
   - Download the latest library bundle
   - Extract the bundle
   - Create a `lib` folder on your `CIRCUITPY` drive
   - Copy these folders to `lib`:
     - `adafruit_hid`
     - `adafruit_hid.keyboard`
     - `adafruit_hid.keyboard_layout_us`
     - `adafruit_hid.keycode`

#### For Raspberry Pi Pico
- Follow the same steps as Xiao RP2040 (same chip)
- Use the "Raspberry Pi Pico" firmware from circuitpython.org

#### For DigiSpark
- Requires different setup (Arduino IDE)
- See `docs/microcontrollers.md` for detailed instructions

### Step 3: Test Your Device

1. **Create a test script:**
   Create a file called `test.py` on your `CIRCUITPY` drive:

   ```python
   import time
   import usb_hid
   from adafruit_hid.keyboard import Keyboard
   from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
   from adafruit_hid.keycode import Keycode

   keyboard = Keyboard(usb_hid.devices)
   keyboard_layout = KeyboardLayoutUS(keyboard)

   def main():
       print("Testing HID functionality...")
       time.sleep(2)
       
       keyboard_layout.write("Hello from Happy Frog!")
       time.sleep(0.5)
       
       keyboard.press(Keycode.ENTER)
       keyboard.release(Keycode.ENTER)
       
       print("Test completed!")

   if __name__ == "__main__":
       main()
   ```

2. **Rename and test:**
   - Rename `test.py` to `code.py`
   - Connect to a test computer
   - You should see "Hello from Happy Frog!" typed automatically

---

## 🐸 Your First Happy Frog Script

### Step 1: Create a Simple Script

1. **Navigate to the payloads directory:**
   ```bash
   cd payloads
   ```

2. **Create your first script:**
   Create a file called `my_first_script.txt`:

   ```txt
   # My First Happy Frog Script
   # This is a simple greeting script
   
   DELAY 2000
   STRING Hello! This is my first Happy Frog device!
   ENTER
   DELAY 500
   STRING I'm learning about HID emulation for cybersecurity education.
   ENTER
   DELAY 500
   STRING Remember: Use responsibly and ethically!
   ENTER
   ```

### Step 2: Generate Device Code

1. **Generate CircuitPython code for your device:**
   ```bash
   # For Seeed Xiao RP2040 (recommended) - saves to compiled/hello_world.py
   python main.py encode my_first_script.txt -d xiao_rp2040
   
   # For other devices - saves to compiled/ directory with appropriate extensions
   python main.py encode my_first_script.txt -d raspberry_pi_pico
   python main.py encode my_first_script.txt -d arduino_leonardo
   python main.py encode my_first_script.txt -d teensy_4
   python main.py encode my_first_script.txt -d digispark
   python main.py encode my_first_script.txt -d esp32
   python main.py encode my_first_script.txt -d evilcrow_cable
   
   # Or use default CircuitPython (no device specified) - saves to compiled/hello_world.py
   python main.py encode my_first_script.txt
   
   # Specify custom output location (optional)
   python main.py encode my_first_script.txt -d xiao_rp2040 -o my_custom_location.py
   ```

   **Need help choosing a device?** You can see all available devices by running:
   ```bash
   python -c "from devices.device_manager import DeviceManager; dm = DeviceManager(); [print(f'- {device[\"name\"]} ({device[\"id\"]})') for device in dm.list_devices()]"
   ```

   **File Extensions:**
   - **CircuitPython devices** (Xiao RP2040, Raspberry Pi Pico, ESP32): `.py` files
   - **Arduino devices** (Arduino Leonardo, Teensy 4.0, DigiSpark, EvilCrow-Cable): `.ino` files
   - **Default**: `.py` files for CircuitPython

2. **Copy to your device:**
   - Copy the generated `my_device_code.py`
   - Paste it as `code.py` on your `CIRCUITPY` drive
   - The device will restart and run your script

### Step 3: Test Your Device

1. **Connect to a test computer**
2. **Wait 2 seconds** (the DELAY 2000 command)
3. **Watch your script execute automatically!**

---

## 📚 Understanding Happy Frog Scripts

### Basic Commands

| Command       | Description           | Example                      |
|---------------|-----------------------|------------------------------|
| `DELAY ms`    | Wait for milliseconds | `DELAY 1000` (wait 1 second) |
| `STRING text` | Type text             | `STRING Hello World!`        |
| `ENTER`       | Press Enter key       | `ENTER`                      |
| `SPACE`       | Press Space key       | `SPACE`                      |
| `TAB`         | Press Tab key         | `TAB`                        |
| `ESC`         | Press Escape key      | `ESC`                        |

### Modifier Keys

| Command | Description         | Example                    |
|---------|---------------------|----------------------------|
| `MOD`   | Windows/Command key | `MOD r` (Windows+R)        |
| `CTRL`  | Control key         | `CTRL c` (Copy)            |
| `SHIFT` | Shift key           | `SHIFT a` (Capital A)      |
| `ALT`   | Alt key             | `ALT TAB` (Switch windows) |

### Function Keys

| Command                       | Description     |
|-------------------------------|-----------------|
| `F1` through `F12`            | Function keys   |
| `UP`, `DOWN`, `LEFT`, `RIGHT` | Arrow keys      |
| `HOME`, `END`                 | Navigation keys |
| `PAGE_UP`, `PAGE_DOWN`        | Page navigation |

### Comments

```txt
# This is a comment
REM This is also a comment
```

---

## 🔧 Advanced Examples

### Example 1: Open Command Prompt (Windows)

```txt
# Open Windows Command Prompt
DELAY 2000
MOD r
DELAY 500
STRING cmd
ENTER
DELAY 1000
STRING echo Hello from Happy Frog!
ENTER
DELAY 500
STRING exit
ENTER
```

### Example 2: System Information

```txt
# Get system information
DELAY 2000
MOD r
DELAY 500
STRING cmd
ENTER
DELAY 1000
STRING systeminfo
ENTER
DELAY 3000
STRING exit
ENTER
```

### Example 3: Educational Demo

```txt
# Educational demonstration
DELAY 2000
STRING This is an educational demonstration of HID emulation.
ENTER
DELAY 500
STRING HID attacks can bypass many security measures.
ENTER
DELAY 500
STRING This is why physical security is crucial!
ENTER
DELAY 1000
STRING Thank you for learning about cybersecurity!
ENTER
```

---

## 🛡️ Safety and Best Practices

### Physical Security
- **Store devices securely** when not in use
- **Label your devices** clearly as educational tools
- **Keep inventory** of all your devices
- **Never leave devices** in public or unsecured areas

### Operational Security
- **Test only on systems you own** or have explicit permission
- **Use isolated test environments** when possible
- **Disconnect from networks** during testing
- **Monitor for unexpected behavior**

### Educational Best Practices
- **Document everything** you do
- **Get written permission** before testing on any system
- **Report vulnerabilities** responsibly if found
- **Share knowledge** with the cybersecurity community

---

## 🐛 Troubleshooting

### Common Issues

#### Device Not Recognized
- **Check USB cable** - try a different cable
- **Check USB port** - try a different port
- **Restart device** - unplug and reconnect
- **Check drivers** - may need to install drivers

#### Code Not Running
- **Check file name** - must be `code.py`
- **Check syntax** - look for Python errors
- **Check libraries** - ensure `adafruit_hid` is installed
- **Check CircuitPython** - ensure firmware is installed

#### Script Not Working
- **Check delays** - add longer delays if needed
- **Check target system** - ensure it's ready for input
- **Check permissions** - ensure you have permission to test
- **Check script syntax** - validate with `python main.py validate script.txt`

### Getting Help

1. **Check the documentation:**
   - `docs/usage.md` - Detailed usage guide
   - `docs/microcontrollers.md` - Hardware setup guide

2. **Look at examples:**
   - `payloads/` directory has example scripts
   - `devices/xiao_rp2040.py` has template code

3. **Use the CLI help:**
   ```bash
   python main.py --help
   python main.py encode --help
   python main.py validate --help
   ```

4. **Join the community:**
   - GitHub Issues: [Report bugs or ask questions](https://github.com/ZeroDumb/happy-frog/issues)
   - GitHub Discussions: [Share ideas and get help](https://github.com/ZeroDumb/happy-frog/discussions)

---

## 🎓 Next Steps

### Learn More
- **Read the full documentation** in the `docs/` directory
- **Experiment with different scripts** in the `payloads/` directory
- **Try different devices** - see `docs/microcontrollers.md`
- **Study cybersecurity concepts** - understand what you're demonstrating

### Advanced Topics
- **Custom device encoders** - create support for new devices
- **Advanced scripting** - use loops, conditions, and variables
- **Security research** - study HID attack vectors and defenses
- **Teaching others** - share your knowledge responsibly

### Educational Resources
- **Cybersecurity courses** - learn about penetration testing
- **Hardware hacking** - explore microcontroller programming
- **USB security** - understand USB attack vectors
- **Physical security** - learn about physical access controls

---

## 📁 File Structure Reference

```
happy-frog/
├── main.py                    # Main CLI interface
├── requirements.txt           # Python dependencies
├── setup.py                  # Package installation
├── payloads/                 # Example scripts
│   ├── hello_world.txt       # Simple greeting script
│   ├── demo_automation.txt   # Educational demo
│   └── my_first_script.txt   # Your first script
├── compiled/                 # Generated device code
│   ├── hello_world.py        # CircuitPython output
│   ├── hello_world.ino       # Arduino output
│   └── *_converted.txt       # Converted scripts
├── devices/                  # Device-specific code
│   ├── xiao_rp2040.py        # Template for Xiao RP2040
│   ├── xiao_rp2040_encoder.py # Code generator for Xiao RP2040
│   └── device_manager.py     # Device management
├── docs/                     # Documentation
│   ├── HELLO_HAPPY_FROG.md   # This guide
│   ├── usage.md              # Detailed usage guide
│   └── microcontrollers.md   # Hardware setup guide
└── tests/                    # Test files
    └── test_*.py            # Various test files
```

---

## 🎉 Congratulations!

You've successfully:
- ✅ Set up Happy Frog on your computer
- ✅ Prepared your microcontroller with CircuitPython
- ✅ Created and tested your first HID emulation script
- ✅ Learned about cybersecurity and ethical hacking

**Remember:** With great power comes great responsibility. Use Happy Frog to learn, teach, and improve cybersecurity - always ethically and legally!

---

## 📞 Support and Community

- **GitHub Repository**: [https://github.com/ZeroDumb/happy-frog](https://github.com/ZeroDumb/happy-frog)
- **Issues**: [https://github.com/ZeroDumb/happy-frog/issues](https://github.com/ZeroDumb/happy-frog/issues)
- **Discussions**: [https://github.com/ZeroDumb/happy-frog/discussions](https://github.com/ZeroDumb/happy-frog/discussions)
- **Documentation**: [https://github.com/ZeroDumb/happy-frog/tree/main/docs](https://github.com/ZeroDumb/happy-frog/tree/main/docs)

**Happy learning! 🐸** 