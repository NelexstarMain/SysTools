import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from spintread import Spinner
from typing import Optional, List


class CurrentFileScanner:
    """
    Class for scanning a directory tree and finding files with a specified name.
    """

    def __init__(self, path: str = "", name: str = "sample.py") -> None:
        """
        Initializes the scanner with a path and target file name.

        Args:
            path (str, optional): The path to start the scan from. Defaults to the root directory.
            name (str): The name of the file to search for. Defaults to "sample.py".
        """
        self.name = name
        self.__main = os.path.abspath(os.sep) if path == "" else path
        self.__matching_elements: list = []

        self.files_processed = 0
        self.dirs_processed = 0
        self.files = 0
        self.dirs = 0
        self.status_interval = 100

    def count_files_and_folders(self, path, spinner: Spinner) -> None:
        """
        Counts the number of files and folders within a given path.

        Args:
            path (str): The path to the directory to count files and folders in.
        """
        file_count = 0
        folder_count = 0

        for root, dirs, files in os.walk(path):
            folder_count += len(dirs)
            file_count += len(files)
            spinner.update_status(
                    f" Files Counted: {file_count} | Dirs Counted: {folder_count}"
                )

        
        self.files = file_count
        self.dirs = folder_count

    def dir_scan(self, path: str) -> Optional[list]:
        """
        Scans a directory for its contents.

        Args:
            path (str): The path to the directory to scan.

        Returns:
            list: A list of elements (files and subdirectories) within the directory, 
                 or None if the directory cannot be accessed.
        """
        try:
            elements = os.listdir(path) or []
            self.dirs_processed += 1
            return elements
        except (FileNotFoundError, PermissionError):
            return None

    def filter_elements(self, path: str, spinner: Spinner) -> None:
        """
        Recursively searches for files with the specified name within a directory tree 
        and appends their full paths to the internal '__matching_elements' list.

        Args:
            path (str): The path to the root directory to start the search.
        """
        step_count = 0

        for element in self.dir_scan(path) or []:
            full_path = os.path.join(path, element)

            if element == self.name:
                self.files_processed += 1
                self.__matching_elements.append(full_path)

            if os.path.isdir(full_path):
                self.filter_elements(full_path, spinner)

            if os.path.isfile(full_path):
                self.files_processed += 1

            step_count += 1

            if step_count % self.status_interval == 0:
                progress = (self.files_processed / self.files * 100) if self.files > 0 else 0
                spinner.update_status(
                    f" Files Processed: {self.files_processed} | Dirs Processed: {self.dirs_processed} | Progress: {progress:.2f}%"
                )
    def run(self) -> List[str]:
        """
        Starts the file search process.

        Returns:
            List[str]: A list of file paths matching the specified name.
        """
        spinner = Spinner(message="Counting directories")
        spinner.start()

        self.count_files_and_folders(self.__main, spinner)

        spinner.stop()


        spinner = Spinner(message="Scanning directories")
        spinner.start()

        self.filter_elements(self.__main, spinner)

        spinner.stop()

        if not self.__matching_elements:
            print(f"File '{self.name}' not found in {self.__main}")

        return self.__matching_elements

if __name__ == "__main__":
    c = CurrentFileScanner(name="__init__.py")
    c.run()