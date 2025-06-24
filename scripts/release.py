#!/usr/bin/env python3
"""
Happy Frog - Release Script

This script helps automate the release process for Happy Frog.
It updates version numbers, creates git tags, and prepares for PyPI upload.

Usage:
    python scripts/release.py [patch|minor|major]
"""

import sys
import subprocess
import re
from pathlib import Path

def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result

def get_current_version():
    """Get the current version from _version.py."""
    version_file = Path("happy_frog_parser/_version.py")
    if not version_file.exists():
        return "0.0.0"
    
    content = version_file.read_text()
    match = re.search(r'__version__ = "([^"]+)"', content)
    return match.group(1) if match else "0.0.0"

def update_version(version_type):
    """Update version based on semantic versioning."""
    current = get_current_version()
    major, minor, patch = map(int, current.split('.'))
    
    if version_type == "patch":
        patch += 1
    elif version_type == "minor":
        minor += 1
        patch = 0
    elif version_type == "major":
        major += 1
        minor = 0
        patch = 0
    else:
        print("Invalid version type. Use: patch, minor, or major")
        sys.exit(1)
    
    new_version = f"{major}.{minor}.{patch}"
    print(f"Updating version from {current} to {new_version}")
    
    # Update _version.py
    version_file = Path("happy_frog_parser/_version.py")
    content = version_file.read_text()
    content = re.sub(r'__version__ = "[^"]+"', f'__version__ = "{new_version}"', content)
    content = re.sub(r'__version_tuple__ = \([^)]+\)', f'__version_tuple__ = ({major}, {minor}, {patch})', content)
    version_file.write_text(content)
    
    return new_version

def main():
    if len(sys.argv) != 2:
        print("Usage: python scripts/release.py [patch|minor|major]")
        sys.exit(1)
    
    version_type = sys.argv[1]
    if version_type not in ["patch", "minor", "major"]:
        print("Invalid version type. Use: patch, minor, or major")
        sys.exit(1)
    
    print("Happy Frog Release Script")
    print("=" * 40)
    
    # Check if we're on main branch
    result = run_command("git branch --show-current", check=False)
    if "main" not in result.stdout:
        print("Warning: Not on main branch. Continue anyway? (y/N): ", end="")
        if input().lower() != 'y':
            sys.exit(0)
    
    # Check for uncommitted changes
    result = run_command("git status --porcelain", check=False)
    if result.stdout.strip():
        print("Warning: You have uncommitted changes. Continue anyway? (y/N): ", end="")
        if input().lower() != 'y':
            sys.exit(0)
    
    # Update version
    new_version = update_version(version_type)
    
    # Build package
    print("\nBuilding package...")
    run_command("python -m build")
    
    # Create git tag
    tag_name = f"v{new_version}"
    print(f"\nCreating git tag: {tag_name}")
    run_command(f'git add happy_frog_parser/_version.py')
    run_command(f'git commit -m "Bump version to {new_version}"')
    run_command(f'git tag {tag_name}')
    
    print(f"\nRelease {new_version} prepared successfully!")
    print("\nNext steps:")
    print(f"1. Push changes: git push origin main")
    print(f"2. Push tag: git push origin {tag_name}")
    print("3. Upload to PyPI: twine upload dist/*")
    print("4. Update CHANGELOG.md with release notes")

if __name__ == "__main__":
    main() 