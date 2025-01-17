"""
Module for loading and processing configuration for CurrentFileScanner.

This module contains the logic for loading a YAML configuration file, which specifies
the settings for scanning directories and managing file handling in the CurrentFileScanner
application. The configuration includes settings such as the default path, file name,
intervals for status updates, spinner messages, and whether exceptions should be handled.

Functions:
- load_config(file_path): Loads and parses the YAML configuration file, returning
  the configuration as a dictionary.

Configuration Example:
- The configuration is defined in a YAML file that includes fields such as 'default_path',
  'file_name', 'status_interval', 'spinner_messages', and 'handle_exceptions'.
"""
