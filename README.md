# 🐸 Happy Frog

**Educational HID Emulation Framework for Cybersecurity Learning**

Happy Frog is an open-source educational framework that demonstrates HID (Human Interface Device) emulation techniques using microcontrollers. It provides a simple scripting language similar to Ducky Script but with our own naming conventions, to avoid any legal concerns, as well as **Happy Frog Exclusive features** that go beyond traditional HID emulation tools.

## ⚠️ Important Disclaimer

**This project is for EDUCATIONAL PURPOSES ONLY!**

- ✅ **Legal Uses**: Educational cybersecurity labs, authorized penetration testing, red teaming with explicit permission, security research in controlled environments
- ❌ **Prohibited Uses**: Unauthorized access to systems, malicious attacks, testing without permission, any illegal activities

By using this tool, you agree to use it only for legal and ethical purposes.

## 🎯 Project Goals

Happy Frog aims to:

1. **Educate** about HID emulation and cybersecurity concepts
2. **Demonstrate** how automated input attacks work
3. **Provide** a safe learning environment for security testing
4. **Showcase** microcontroller programming and code generation
5. **Avoid** over complicated and proprietary binary code
6. **Enhance** traditional HID emulation with advanced features for education

## 🚀 Features

### Happy Frog Script Language
- **Simple Syntax**: Easy-to-learn scripting language
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Educational**: Rich comments and documentation
- **Safe**: Built-in validation and warnings
- **Advanced**: Conditional logic, loops, and human-like behavior
- **Use Your "Other" Strings**: Easy conversion from your other HID txt to Happy Frog 

### Supported Commands

#### Basic Input & Navigation
- **Basic Input**: `STRING`, `ENTER`, `SPACE`, `TAB`, `BACKSPACE`, `DELETE`
- **Navigation**: `UP`, `DOWN`, `LEFT`, `RIGHT`, `HOME`, `END`, `PAGE_UP`, `PAGE_DOWN`
- **Function Keys**: `F1` through `F12`
- **Modifiers**: `CTRL`, `SHIFT`, `ALT`, `MOD` (Windows/Command key)
- **Combos**: `MOD r`, `CTRL ALT DEL`, `SHIFT F1`

#### Timing & Control
- **Delays**: `DELAY` for precise timing control
- **Default Delays**: `DEFAULT_DELAY` or `DEFAULTDELAY` for global timing
- **Random Delays**: `RANDOM_DELAY min max` for human-like behavior
- **Pause**: `PAUSE` or `BREAK` for execution control
- **Repeat**: `REPEAT n` to repeat previous commands

#### Advanced Features (Happy Frog Exclusive)
- **Conditional Logic**: `IF condition`, `ELSE`, `ENDIF`
- **Loops**: `WHILE condition`, `ENDWHILE`
- **Logging**: `LOG message` for debugging and education
- **Validation**: `VALIDATE condition` for environment checks
- **Safe Mode**: `SAFE_MODE ON/OFF` for controlled execution

#### Documentation
- **Comments**: `#` and `REM` for documentation

### Ducky Script Compatibility
Happy Frog is **100% compatible** with Ducky Script and includes a built-in converter: (because change is hard)
- **Automatic Conversion**: Convert any Ducky Script to Happy Frog Script
- **Command Mapping**: `WINDOWS`/`GUI`/`COMMAND` → `MOD`
- **Educational Warnings**: Built-in safety checks and warnings
- **Validation**: Automatic detection of potentially dangerous commands

### Key Advantages Over Traditional Tools
- **Free and Open Source**: Anyone can use, modify, or contribute
- **Educational Focus**: Rich documentation and learning resources
- **Advanced Features**: Conditional logic, loops, and human-like behavior
- **Safety First**: Built-in validation, safe mode, and ethical guidelines
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Extensible**: Easy to add new commands and features

### Quick Links


## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Seeed Xiao RP2040 (or compatible CircuitPython device)

### Setup
```bash
# Clone the repository
git clone https://github.com/ZeroDumb/happy-frog.git
cd happy-frog

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

## 🛠️ Usage

### Command Line Interface

```bash
# Parse a Happy Frog Script file
python main.py parse payloads/demo_automation.txt

# Encode to CircuitPython
python main.py encode payloads/demo_automation.txt -o output.py

# Convert Ducky Script to Happy Frog Script
python main.py convert ducky_script.txt

# Validate a script
python main.py validate payloads/demo_automation.txt

# Verbose output
python main.py encode payloads/demo_automation.txt -o output.py --verbose
```

### Python API

```python
from happy_frog_parser import HappyFrogParser, CircuitPythonEncoder
from ducky_converter import DuckyConverter

# Parse a Happy Frog Script
parser = HappyFrogParser()
script = parser.parse_file("payloads/demo_automation.txt")

# Encode to CircuitPython
encoder = CircuitPythonEncoder()
code = encoder.encode(script, "output.py")

# Convert Ducky Script
converter = DuckyConverter()
converted_content, warnings = converter.convert_file("ducky_script.txt")
```

### Example Happy Frog Scripts

#### Basic Example
```txt
# Happy Frog Script - Hello World
# Educational example demonstrating basic automation

DELAY 1000
STRING Hello, World! This is Happy Frog Script in action!
ENTER
DELAY 500
STRING This demonstrates basic text input automation.
ENTER
```

#### Advanced Example with Conditional Logic
```txt
# Advanced Happy Frog Script - Demonstrating exclusive features

# Set default delay for all commands
DEFAULT_DELAY 500

# Enable safe mode for educational use
SAFE_MODE ON

# Log our actions for debugging
LOG Starting advanced automation sequence

# Human-like random delays
RANDOM_DELAY 200 800

# Conditional execution
IF system_windows
STRING Windows system detected
ELSE
STRING Non-Windows system detected
ENDIF

# Loop execution
WHILE counter < 3
STRING Loop iteration
ENTER
RANDOM_DELAY 100 300
ENDWHILE

# Advanced modifier combo
MOD r
DELAY 500
STRING notepad
ENTER

# Log completion
LOG Advanced automation sequence completed
```

#### Ducky Script Conversion Example
```txt
# Original Ducky Script
REM Open Run dialog
WINDOWS r
DELAY 1000
STRING cmd
ENTER

# Converts to Happy Frog Script:
# Open Run dialog
MOD r
DELAY 1000
STRING cmd
ENTER
```

## 🎓 Educational Content

### Learning Objectives
- Understand how automated input attacks work
- Learn to recognize and defend against HID attacks
- Practice ethical security testing techniques
- Develop skills in microcontroller programming
- Master advanced automation concepts

### Key Concepts Demonstrated
- **HID Emulation**: How devices can emulate human input
- **Script Parsing**: Converting text commands to executable code
- **Code Generation**: Creating microcontroller-compatible code
- **Security Awareness**: Understanding attack vectors and defenses
- **Conditional Logic**: Advanced automation with decision-making
- **Human-like Behavior**: Realistic timing and interaction patterns

### Advanced Features for Education
- **Safe Mode**: Controlled execution environment
- **Logging**: Real-time feedback and debugging
- **Validation**: Environment checks before execution
- **Random Delays**: Understanding human behavior patterns
- **Conditional Logic**: Learning programming concepts

## 🔧 Hardware Setup

### Seeed Xiao RP2040
1. Install CircuitPython on your Xiao RP2040
2. Install required libraries:
   ```bash
   adafruit_hid
   ```
3. Copy generated CircuitPython code to your device
4. Test in a controlled environment

### Safety Best Practices
- Always test in virtual machines first
- Use dedicated test systems
- Never test on production systems
- Keep physical access secure
- Document all testing activities
- Use safe mode for educational purposes

## 📁 Project Structure

```
happy-frog/
├── happy_frog_parser/          # Core parsing and encoding
│   ├── parser.py              # Script parser
│   ├── encoder.py             # CircuitPython code generator
│   └── __init__.py
├── devices/                   # Device-specific templates
│   └── xiao_rp2040.py        # Xiao RP2040 specific code
├── payloads/                  # Example Happy Frog Scripts
├── tests/                     # Unit tests
├── docs/                      # Documentation
├── ducky_converter.py         # Ducky Script converter
├── main.py                    # CLI interface
└── requirements.txt           # Python dependencies
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_parser.py -v

# Run with coverage
python -m pytest tests/ --cov=happy_frog_parser

# Test Ducky Script conversion
python main.py convert test_hak5_examples.txt

# Test advanced features
python main.py parse test_advanced_features.txt
```

## 📚 Documentation

- [Usage Guide](docs/usage.md) - Detailed usage instructions
- [Microcontroller Setup](docs/microcontrollers.md) - Hardware setup guide
- [Educational Examples](payloads/) - Sample scripts with explanations
- [Why We Are Different](docs/How_We_Are_Different.md) - What sets Happy Frog appart from that other script

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run pre-commit hooks
pre-commit install

# Run tests before committing
python -m pytest tests/
```

## 📄 License

This project is licensed under the GNU GPL3 License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by educational cybersecurity concepts
- Built with CircuitPython and Adafruit libraries
- Designed for learning and ethical use only
- Enhanced with advanced features for comprehensive education

## ⚖️ Legal Notice

This project is designed for educational purposes only. Users are responsible for ensuring they have proper authorization before testing any systems. The authors are not responsible for any misuse of this software.

---

**Remember: Knowledge is power, but with great power comes great responsibility! 🐸**

**Happy Frog: Where Education Meets Innovation in HID Emulation**

## Other Things
- [Blog](https://zerodumb.dev)
- [X - @zerodumb_dev](https://x.com/zerodumb_dev)
- [Store - Coming Soon](https://store.zerodumb.dev)
- [Buy Me Coffee](https://buymeacoffee.com/iamnotaskid)

