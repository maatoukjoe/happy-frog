# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Production-ready packaging configuration
- Clean dependency management
- Proper version control

### Changed
- Excluded development files from package distribution
- Updated development status to Beta
- Streamlined package structure

### Fixed
- Import issues with device modules
- Conditional CircuitPython imports for host compatibility

## [0.1.0] - 2024-01-XX

### Added
- Happy Frog Script parser and encoder
- Support for multiple microcontroller platforms:
  - Xiao RP2040 (CircuitPython)
  - ESP32 (Arduino)
  - Arduino Leonardo
  - Raspberry Pi Pico
  - Teensy 4
  - Digispark
  - Evil Crow Cable
- Educational payload examples
- Command-line interface
- Comprehensive test suite

### Features
- Script parsing and validation
- Device-specific code generation
- Educational HID emulation framework
- Cross-platform compatibility
- Ethical cybersecurity education tools

---

## Version History

- **0.1.0**: Initial release with core functionality
- **Unreleased**: Production packaging improvements

## Release Process

1. Update version in `happy_frog_parser/_version.py`
2. Update this CHANGELOG.md
3. Create git tag: `git tag v0.1.0`
4. Push tag: `git push origin v0.1.0`
5. Build package: `python -m build`
6. Upload to PyPI: `twine upload dist/*`

## Semantic Versioning

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in backward-compatible manner
- **PATCH**: Backward-compatible bug fixes 