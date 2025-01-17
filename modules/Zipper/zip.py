"""
Zip Utility Module

This module provides utility functions for compressing files and directories 
into ZIP archives. It supports zipping individual files, entire directories, 
and generating default ZIP archive names if not provided by the user.

Functions:
- zip_file(file_path: str, zip_name: str) -> None:
    Adds a single file to a ZIP archive.
- zip_directory(dir_path: str, zip_name: str) -> None:
    Adds all files in a directory (recursively) to a ZIP archive.
- zip(path: str, zip_name: str = None) -> None:
    Determines whether the given path is a file or directory and compresses it 
    into a ZIP archive. Generates a default ZIP name if none is provided.

Usage:
    from modules.Zipper.zip import zip

    # Zip a single file
    zip("example.txt", "archive.zip")

    # Zip an entire directory
    zip("my_folder", "archive.zip")

    # Let the function generate the ZIP name
    zip("example.txt")
"""




import zipfile
import os

def zip_file(file_path: str, zip_name: str) -> None:
    """
    Add a single file to a ZIP archive.

    Args:
        file_path (str): Path to the file to be zipped.
        zip_name (str): Name of the ZIP archive to create or update.

    Returns:
        None
    """
    print(f"Zipping file: {file_path}")
    with zipfile.ZipFile(zip_name, "a") as zipped:
        zipped.write(file_path, arcname=os.path.basename(file_path))

def zip_directory(dir_path: str, zip_name: str) -> None:
    """
    Add all files in a directory (recursively) to a ZIP archive.

    Args:
        dir_path (str): Path to the directory to be zipped.
        zip_name (str): Name of the ZIP archive to create or update.

    Returns:
        None
    """
    with zipfile.ZipFile(zip_name, 'a', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Zipping file: {file_path}")
                zipf.write(file_path, arcname=os.path.relpath(file_path, dir_path))

def zip(path: str, zip_name: str = None) -> None:
    """
    Compress a file or directory into a ZIP archive.

    If no ZIP archive name is provided, it generates one based on the input path.

    Args:
        path (str): Path to the file or directory to be zipped.
        zip_name (str, optional): Name of the ZIP archive to create or update.
            If None, a default name is generated based on the input path.

    Returns:
        None
    """
    if zip_name is None:
        if os.path.isfile(path):
            zip_name = os.path.splitext(path)[0] + ".zip"
        elif os.path.isdir(path):
            zip_name = os.path.join(os.path.dirname(path), os.path.basename(path) + ".zip")

    if os.path.isfile(path):
        zip_file(path, zip_name)
    elif os.path.isdir(path):
        zip_directory(path, zip_name)
    else:
        raise ValueError(f"The specified path does not exist: {path}")
