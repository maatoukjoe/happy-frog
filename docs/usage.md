# Happy Frog Usage Guide

This guide explains how to use Happy Frog for educational cybersecurity purposes. **Remember: This tool is for authorized testing and education only.**

## ⚠️ Legal and Ethical Guidelines

Before using Happy Frog, you **MUST** understand and agree to these guidelines:

### ✅ Permitted Uses
- Educational cybersecurity labs
- Authorized penetration testing with written permission
- Red team exercises in controlled environments
- Security research on systems you own
- Teaching cybersecurity concepts

### ❌ Prohibited Uses
- Unauthorized access to any systems
- Malicious attacks or cybercrime
- Testing without explicit permission
- Any illegal activities

**By using this tool, you accept full responsibility for ensuring your use is legal and ethical.**

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone https://github.com/ZeroDumb/happy-frog.git
cd happy-frog

# Install dependencies
pip install -r requirements.txt

# Install the package
pip install -e .
```

### 2. Basic Usage

```bash
# Convert a Ducky Script to CircuitPython
happy-frog payloads/hello_world.txt -o output.py

# Validate a script without generating output
happy-frog payloads/hello_world.txt --validate

# Get verbose output
happy-frog payloads/hello_world.txt -o output.py --verbose
```

## 📝 Writing Ducky Scripts

Ducky Script is a simple scripting language for automating keyboard input. Here's how to write your own scripts:

### Basic Commands

#### DELAY
Wait for a specified number of milliseconds:
```
DELAY 1000  # Wait for 1 second
```

#### STRING
Type text as if it was typed on a keyboard:
```
STRING Hello World!
```

#### ENTER
Press the Enter key:
```
ENTER
```

#### Special Keys
Press special keys:
```
SPACE
TAB
BACKSPACE
DELETE
UP
DOWN
LEFT
RIGHT
HOME
END
INSERT
PAGE_UP
PAGE_DOWN
ESCAPE
```

#### Function Keys
Press function keys:
```
F1
F2
F3
F4
F5
F6
F7
F8
F9
F10
F11
F12
```

#### Modifier Keys
Press modifier keys (use with other keys):
```
CTRL
SHIFT
ALT
GUI  # Windows/Command key
```

#### Comments
Add comments to your scripts:
```
# This is a comment
REM This is also a comment
```

### Example Scripts

#### Simple Greeting
```txt
# Simple greeting script
DELAY 2000
STRING Hello from Happy Frog!
ENTER
STRING This is for educational purposes only!
ENTER
```

#### Open Command Prompt (Windows)
```txt
# Open command prompt
DELAY 2000
GUI r
DELAY 500
STRING cmd
ENTER
DELAY 1000
STRING echo Hello World!
ENTER
```

#### System Information
```txt
# Get system information
DELAY 2000
GUI r
DELAY 500
STRING cmd
ENTER
DELAY 1000
STRING systeminfo
ENTER
DELAY 2000
STRING exit
ENTER
```

## 🔧 CLI Reference

### Basic Commands

```bash
# Convert script to CircuitPython
happy-frog <input_file> -o <output_file>

# Validate script
happy-frog <input_file> --validate

# Show help
happy-frog --help

# List supported commands
happy-frog --list-commands

# Show educational information
happy-frog --educational
```

### Command Line Options

| Option | Description |
|--------|-------------|
| `input_file` | Path to Ducky Script file (.txt) |
| `-o, --output` | Output file path for generated code |
| `--verbose, -v` | Enable verbose output |
| `--validate` | Validate script without generating output |
| `--list-commands` | List all supported commands |
| `--educational` | Show educational information |
| `--version` | Show version information |

### Examples

```bash
# Basic conversion
happy-frog my_script.txt -o output.py

# Verbose output with validation
happy-frog my_script.txt -o output.py --verbose --validate

# Just validate a script
happy-frog my_script.txt --validate

# Get help
happy-frog --help
```

## 🐸 Flashing to Microcontrollers

### Prerequisites

1. **CircuitPython Firmware**: Install CircuitPython on your microcontroller
2. **Required Libraries**: Install `adafruit_hid` library
3. **USB Cable**: Connect your device to your computer

### Supported Devices

- **Seeed Xiao RP2040** (Recommended)
- Other CircuitPython-compatible boards

### Step-by-Step Instructions

#### 1. Install CircuitPython

1. Download CircuitPython for your board from [circuitpython.org](https://circuitpython.org/)
2. Follow the installation instructions for your specific board
3. Verify installation by seeing a `CIRCUITPY` drive when connected

#### 2. Install Required Libraries

1. Download the CircuitPython Library Bundle
2. Copy the `adafruit_hid` folder to the `lib` folder on your device
3. Verify the libraries are installed correctly

#### 3. Upload Generated Code

1. Generate CircuitPython code using Happy Frog:
   ```bash
   happy-frog payloads/hello_world.txt -o output.py
   ```

2. Copy the generated `output.py` to your device as `code.py`
3. The device will automatically run the code when powered on

#### 4. Testing

1. Connect your device to a test computer
2. Wait for the device to be recognized
3. Observe the automated input behavior
4. **Always test in controlled environments**

### Safety Features

The generated code includes several safety features:

- **Startup Delay**: Waits for system recognition
- **Error Handling**: Graceful error recovery
- **Emergency Stop**: Can be interrupted safely
- **Educational Comments**: Explains what each command does

## 🛡️ Security Best Practices

### For Testing

1. **Use Virtual Machines**: Test in isolated environments
2. **Disconnect Networks**: Prevent unintended network access
3. **Monitor Activity**: Watch for unexpected behavior
4. **Document Everything**: Keep records of all testing

### For Defense

1. **Physical Security**: Control access to USB ports
2. **Device Monitoring**: Watch for unexpected input devices
3. **Input Validation**: Implement rate limiting and validation
4. **User Awareness**: Train users about HID attack risks

## 🎓 Educational Concepts

Happy Frog demonstrates several important cybersecurity concepts:

### HID Attacks
- **What**: Devices that emulate human input
- **How**: Bypass software security at the input level
- **Defense**: Physical security and device monitoring

### Code Generation
- **What**: Converting high-level scripts to executable code
- **How**: Parsing and translation techniques
- **Application**: Understanding how automation works

### Microcontroller Security
- **What**: Security implications of embedded devices
- **How**: Devices can be programmed for various purposes
- **Defense**: Secure development and deployment practices

## 🐛 Troubleshooting

### Common Issues

#### Device Not Recognized
- Ensure CircuitPython is properly installed
- Check USB cable and connections
- Verify device drivers are installed

#### Script Not Working
- Check for syntax errors in Ducky Script
- Verify timing and delays are appropriate
- Test in a controlled environment first

#### Permission Errors
- Run CLI with appropriate permissions
- Check file paths and permissions
- Ensure output directory is writable

### Getting Help

1. Check the [GitHub Issues](https://github.com/ZeroDumb/happy-frog/issues)
2. Review the documentation
3. Test with sample payloads first
4. Use the `--verbose` flag for detailed output

## 📚 Additional Resources

- [CircuitPython Documentation](https://docs.circuitpython.org/)
- [Adafruit HID Library](https://github.com/adafruit/Adafruit_CircuitPython_HID)
- [USB HID Specification](https://www.usb.org/document-library/device-class-definition-hid-111)
- [Cybersecurity Education Resources](https://www.sans.org/cyber-security-courses/)

## ⚖️ Legal Notice

This software is provided "as is" without warranty. Users are responsible for ensuring their use complies with applicable laws and regulations. The authors disclaim all liability for misuse of this software.

**Remember: With great power comes great responsibility. Use Happy Frog wisely and ethically! 🐸** 