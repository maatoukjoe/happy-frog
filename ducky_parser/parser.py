"""
Happy Frog - Happy Frog Script Parser

This module implements a parser for Happy Frog Script v1.0, converting script files
into an internal representation that can be processed by encoders.

Educational Purpose: This demonstrates lexical analysis, parsing, and abstract
syntax tree construction - fundamental concepts in compiler design and language processing.

Author: Happy Frog Team
License: MIT
"""

import re
from typing import List, Dict, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum


class HappyFrogScriptError(Exception):
    """Custom exception for Happy Frog Script parsing errors."""
    pass


class CommandType(Enum):
    """Enumeration of supported Happy Frog Script commands."""
    DELAY = "DELAY"
    STRING = "STRING"
    ENTER = "ENTER"
    SPACE = "SPACE"
    TAB = "TAB"
    BACKSPACE = "BACKSPACE"
    DELETE = "DELETE"
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    HOME = "HOME"
    END = "END"
    INSERT = "INSERT"
    PAGE_UP = "PAGE_UP"
    PAGE_DOWN = "PAGE_DOWN"
    ESCAPE = "ESCAPE"
    F1 = "F1"
    F2 = "F2"
    F3 = "F3"
    F4 = "F4"
    F5 = "F5"
    F6 = "F6"
    F7 = "F7"
    F8 = "F8"
    F9 = "F9"
    F10 = "F10"
    F11 = "F11"
    F12 = "F12"
    CTRL = "CTRL"
    SHIFT = "SHIFT"
    ALT = "ALT"
    MOD = "MOD"  # Modifier key (Windows/Command/Super)
    MODIFIER_COMBO = "MODIFIER_COMBO"  # For combos like MOD r
    PAUSE = "PAUSE"  # Pause execution
    SAFE_MODE = "SAFE_MODE"  # Enable/disable safe mode
    ATTACKMODE = "ATTACKMODE"  # BadUSB attack mode
    COMMENT = "COMMENT"
    REM = "REM"  # Alternative comment syntax


@dataclass
class HappyFrogCommand:
    """Represents a single Happy Frog Script command with its parameters."""
    command_type: CommandType
    line_number: int
    raw_text: str
    parameters: Optional[List[str]] = None
    
    def __post_init__(self):
        if self.parameters is None:
            self.parameters = []


@dataclass
class HappyFrogScript:
    """Represents a complete parsed Happy Frog Script."""
    commands: List[HappyFrogCommand]
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}


class HappyFrogParser:
    """
    Parser for Happy Frog Script v1.0 files.
    
    This parser implements a simple line-by-line parsing approach that's easy
    to understand and extend. It demonstrates basic lexical analysis and
    command recognition patterns.
    """
    
    def __init__(self):
        """Initialize the parser with command patterns."""
        # Define regex patterns for different command types
        self.command_patterns = {
            # Modifier+key combos (e.g., MOD r, CTRL ALT DEL) - must have at least 2 parts
            CommandType.MODIFIER_COMBO: re.compile(r'^(MOD|CTRL|SHIFT|ALT)(?:\s+(MOD|CTRL|SHIFT|ALT|[A-Z0-9]+))+$', re.IGNORECASE),
            # Delay command: DELAY <value> - captures any value for validation
            CommandType.DELAY: re.compile(r'^DELAY\s+(.+)$', re.IGNORECASE),
            
            # String command: STRING <text>
            CommandType.STRING: re.compile(r'^STRING\s+(.+)$', re.IGNORECASE),
            
            # Simple commands with no parameters
            CommandType.ENTER: re.compile(r'^ENTER$', re.IGNORECASE),
            CommandType.SPACE: re.compile(r'^SPACE$', re.IGNORECASE),
            CommandType.TAB: re.compile(r'^TAB$', re.IGNORECASE),
            CommandType.BACKSPACE: re.compile(r'^BACKSPACE$', re.IGNORECASE),
            CommandType.DELETE: re.compile(r'^DELETE$', re.IGNORECASE),
            
            # Arrow keys
            CommandType.UP: re.compile(r'^UP$', re.IGNORECASE),
            CommandType.DOWN: re.compile(r'^DOWN$', re.IGNORECASE),
            CommandType.LEFT: re.compile(r'^LEFT$', re.IGNORECASE),
            CommandType.RIGHT: re.compile(r'^RIGHT$', re.IGNORECASE),
            
            # Navigation keys
            CommandType.HOME: re.compile(r'^HOME$', re.IGNORECASE),
            CommandType.END: re.compile(r'^END$', re.IGNORECASE),
            CommandType.INSERT: re.compile(r'^INSERT$', re.IGNORECASE),
            CommandType.PAGE_UP: re.compile(r'^PAGE_UP$', re.IGNORECASE),
            CommandType.PAGE_DOWN: re.compile(r'^PAGE_DOWN$', re.IGNORECASE),
            CommandType.ESCAPE: re.compile(r'^ESCAPE$', re.IGNORECASE),
            
            # Function keys
            CommandType.F1: re.compile(r'^F1$', re.IGNORECASE),
            CommandType.F2: re.compile(r'^F2$', re.IGNORECASE),
            CommandType.F3: re.compile(r'^F3$', re.IGNORECASE),
            CommandType.F4: re.compile(r'^F4$', re.IGNORECASE),
            CommandType.F5: re.compile(r'^F5$', re.IGNORECASE),
            CommandType.F6: re.compile(r'^F6$', re.IGNORECASE),
            CommandType.F7: re.compile(r'^F7$', re.IGNORECASE),
            CommandType.F8: re.compile(r'^F8$', re.IGNORECASE),
            CommandType.F9: re.compile(r'^F9$', re.IGNORECASE),
            CommandType.F10: re.compile(r'^F10$', re.IGNORECASE),
            CommandType.F11: re.compile(r'^F11$', re.IGNORECASE),
            CommandType.F12: re.compile(r'^F12$', re.IGNORECASE),
            
            # Modifier keys (single keys)
            CommandType.CTRL: re.compile(r'^CTRL$', re.IGNORECASE),
            CommandType.SHIFT: re.compile(r'^SHIFT$', re.IGNORECASE),
            CommandType.ALT: re.compile(r'^ALT$', re.IGNORECASE),
            CommandType.MOD: re.compile(r'^MOD$', re.IGNORECASE),  # Modifier key
            
            # Execution control
            CommandType.PAUSE: re.compile(r'^PAUSE$', re.IGNORECASE),  # Pause execution
            CommandType.SAFE_MODE: re.compile(r'^SAFE_MODE\s+(ON|OFF)$', re.IGNORECASE),  # SAFE_MODE ON/OFF
            CommandType.ATTACKMODE: re.compile(r'^ATTACKMODE\s+(HID|STORAGE|HID\s+STORAGE|ON|OFF)$', re.IGNORECASE),  # ATTACKMODE with parameters
            
            # Comments
            CommandType.COMMENT: re.compile(r'^#(.*)$', re.IGNORECASE),
            CommandType.REM: re.compile(r'^REM(?:\s+(.+))?$', re.IGNORECASE),  # REM with optional text
        }
    
    def parse_file(self, file_path: str) -> HappyFrogScript:
        """
        Parse a Happy Frog Script file and return a structured representation.
        
        Args:
            file_path: Path to the .txt file containing Happy Frog Script
            
        Returns:
            HappyFrogScript object containing parsed commands
            
        Raises:
            HappyFrogScriptError: If parsing fails
            FileNotFoundError: If the file doesn't exist
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            return self.parse_string(content, file_path)
        except FileNotFoundError:
            raise HappyFrogScriptError(f"File not found: {file_path}")
        except Exception as e:
            raise HappyFrogScriptError(f"Error reading file {file_path}: {str(e)}")
    
    def parse_string(self, content: str, source_name: str = "<string>") -> HappyFrogScript:
        """
        Parse Happy Frog Script content from a string.
        
        Args:
            content: String containing Happy Frog Script commands
            source_name: Name of the source (for error reporting)
            
        Returns:
            HappyFrogScript object containing parsed commands
        """
        commands = []
        lines = content.split('\n')
        
        for line_number, line in enumerate(lines, 1):
            # Skip empty lines
            if not line.strip():
                continue
                
            try:
                command = self._parse_line(line.strip(), line_number)
                if command:
                    commands.append(command)
            except HappyFrogScriptError as e:
                # Add context to the error
                raise HappyFrogScriptError(
                    f"Error in {source_name}, line {line_number}: {str(e)}"
                )
        
        metadata = {
            'source': source_name,
            'total_commands': len(commands),
            'total_lines': len(lines)
        }
        
        return HappyFrogScript(commands=commands, metadata=metadata)
    
    def _parse_line(self, line: str, line_number: int) -> Optional[HappyFrogCommand]:
        """
        Parse a single line of Happy Frog Script.
        
        Args:
            line: The line to parse
            line_number: Line number for error reporting
            
        Returns:
            HappyFrogCommand object or None if line should be ignored
            
        Raises:
            HappyFrogScriptError: If the line cannot be parsed
        """
        # Try to match each command pattern
        for command_type, pattern in self.command_patterns.items():
            match = pattern.match(line)
            if match:
                # Special handling for MODIFIER_COMBO
                if command_type == CommandType.MODIFIER_COMBO:
                    # Split the line into parts (e.g., MOD r -> [MOD, r])
                    parts = line.strip().split()
                    return HappyFrogCommand(
                        command_type=CommandType.MODIFIER_COMBO,
                        line_number=line_number,
                        raw_text=line,
                        parameters=parts
                    )
                return self._create_command(command_type, line, line_number, match)
        
        # If no pattern matches, it's an unknown command
        raise HappyFrogScriptError(f"Unknown command: {line}")
    
    def _create_command(self, command_type: CommandType, raw_text: str, 
                       line_number: int, match) -> HappyFrogCommand:
        """
        Create a HappyFrogCommand object from a regex match.
        
        Args:
            command_type: Type of command
            raw_text: Original text of the command
            line_number: Line number
            match: Regex match object
            
        Returns:
            HappyFrogCommand object
        """
        parameters = []
        
        # Extract parameters based on command type
        if command_type == CommandType.DELAY:
            # DELAY command has a parameter (validation happens in encoder)
            parameters = [match.group(1)]
                
        elif command_type in [CommandType.STRING, CommandType.REM]:
            # STRING and REM commands capture the rest of the line
            parameters = [match.group(1)] if match.group(1) else ['']
            
        elif command_type == CommandType.COMMENT:
            # COMMENT command captures everything after #
            parameters = [match.group(1)]
            
        elif command_type == CommandType.SAFE_MODE:
            # SAFE_MODE command captures ON/OFF parameter
            parameters = [match.group(1)]
            
        elif command_type == CommandType.ATTACKMODE:
            # ATTACKMODE command captures the mode parameter
            parameters = [match.group(1)]
            
        # For all other commands, no parameters are extracted
        
        return HappyFrogCommand(
            command_type=command_type,
            line_number=line_number,
            raw_text=raw_text,
            parameters=parameters
        )
    
    def validate_script(self, script: HappyFrogScript) -> List[str]:
        """
        Validate a parsed script for common issues.
        
        Args:
            script: Parsed HappyFrogScript object
            
        Returns:
            List of warning messages (empty if no issues)
        """
        warnings = []
        
        # Check for common issues
        if not script.commands:
            warnings.append("Script contains no commands")
            
        # Check for very long delays that might indicate errors
        for cmd in script.commands:
            if cmd.command_type == CommandType.DELAY:
                try:
                    delay_ms = int(cmd.parameters[0])
                    if delay_ms > 60000:  # More than 1 minute
                        warnings.append(
                            f"Line {cmd.line_number}: Very long delay ({delay_ms}ms) - "
                            "this might be an error"
                        )
                except (ValueError, IndexError):
                    pass
        
        return warnings 