# Happy Frog - Installation Guide

## 🚀 Quick Installation

### From PyPI (when published)
```bash
pip install happy-frog
```

### From GitHub (development version)
```bash
pip install git+https://github.com/ZeroDumb/happy-frog.git
```

### From Local Source
```bash
# Clone the repository
git clone https://github.com/ZeroDumb/happy-frog.git
cd happy-frog

# Install in development mode
pip install -e .

# Or build and install
pip install build
python -m build
pip install dist/happy_frog-*.whl
```

## 📦 Package Contents

When installed via pip, Happy Frog provides:

### Core Modules
- `happy_frog_parser` - Script parsing and encoding
- `devices` - Device-specific code generation
- `payloads` - Example payload scripts

### Command Line Interface
```bash
happy-frog --help
```

### Python API
```python
from happy_frog_parser import HappyFrogParser, CircuitPythonEncoder
from devices import DeviceManager
from payloads import load_payload, list_payloads

# Parse a script
parser = HappyFrogParser()
script = parser.parse("STRING Hello World\nENTER")

# Generate device code
encoder = CircuitPythonEncoder()
code = encoder.encode(script)

# List available payloads
print(list_payloads())
```

## 🔧 Development Installation

For development and testing:

```bash
# Clone and install with development dependencies
git clone https://github.com/ZeroDumb/happy-frog.git
cd happy-frog
pip install -e ".[dev]"

# Run tests
pytest

# Format code
black .

# Lint code
flake8
```

## 📋 Requirements

- Python 3.8 or higher
- Dependencies: `click`, `colorama`
- Optional: `pytest`, `black`, `flake8` (for development)

## 🎯 Usage in Your Project

### As a Dependency
Add to your `requirements.txt`:
```
happy-frog>=0.1.0
```

### As a Git Submodule
```bash
git submodule add https://github.com/ZeroDumb/happy-frog.git external/happy-frog
```

### Direct Import
```python
# Import the core functionality
from happy_frog_parser import HappyFrogParser, CircuitPythonEncoder
from devices import DeviceManager

# Use in your Bash Bunny alternative
parser = HappyFrogParser()
encoder = CircuitPythonEncoder()
device_manager = DeviceManager()

# Parse and encode scripts
script_content = "STRING Hello World\nENTER"
parsed_script = parser.parse(script_content)
device_code = encoder.encode(parsed_script)
```

## 🐛 Troubleshooting

### Import Errors
If you get import errors, ensure the package is properly installed:
```bash
pip show happy-frog
```

### Version Conflicts
If you have version conflicts, use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install happy-frog
```

### Build Issues
If you encounter build issues:
```bash
pip install --upgrade pip setuptools wheel
pip install -e .
```

## 📄 License

This package is licensed under GNU GPLv3. See LICENSE file for details. 