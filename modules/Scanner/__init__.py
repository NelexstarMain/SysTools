"""
Scanner Module

This module provides functionality for scanning directories and managing files. 
It includes the `CurrentFileScanner` class, which is designed to perform file 
search operations within a specified directory tree based on user-defined 
configurations.

The module supports dynamic configuration using YAML files, spinner animations 
for real-time feedback during operations, and optional exception handling.

Key Features:
- Scan directory trees for specific files.
- Display progress updates using spinner animations.
- Flexible configuration via a YAML file.

Classes:
- CurrentFileScanner: Scans directories and handles file operations.

Usage:
    from modules.Scanner import CurrentFileScanner

    config = load_config("config/settings.yaml")
    scanner = CurrentFileScanner(config=config, name="Example Scan", print=True)
    scanner.run()
"""
