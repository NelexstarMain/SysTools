import os
import time
from typing import Optional

main = os.path.abspath(os.sep)
files_processed = 0
name: str = ""
dirs_processed = 0

files = 0
dirs = 0

status_interval = 100

def count_files_and_folders(path):
    file_count = 0
    folder_count = 0

    for root, dirs, files in os.walk(path):
        folder_count += len(dirs)
        file_count += len(files)
        
    return file_count, folder_count

def dir_scan(path: str) -> Optional[list]:
    global dirs_processed
    try:
        elements = os.listdir(path) or []
        dirs_processed += 1
        return elements
    except (FileNotFoundError, PermissionError):
        return None

def filter_elements(path: str) -> Optional[str]:
    global files_processed, dirs_processed, files, dirs
    step_count = 0  
    for element in dir_scan(path) or []:
        full_path = os.path.join(path, element)
        if element == name: 
            files_processed += 1
            return full_path
        if os.path.isdir(full_path): 
            result = filter_elements(full_path)
            if result: 
                return result

        if os.path.isfile(full_path):  
            files_processed += 1
        
        step_count += 1
        if step_count % status_interval == 0:
            print(f"\rSearching... {'|/-\\'[int(time.time() * 10) % 4]} | Files Processed: {files_processed} | Dirs Processed: {dirs_processed} | Progress: {files_processed / files * 100:.2f}% | Current file {full_path}" , end="")
            

    return None



if __name__ == "__main__":
    files, dirs = count_files_and_folders(main)
    result = filter_elements(main)
    print(f"\nZnaleziono: {result}" if result else f"'{name}' nie znaleziono w katalogu {main}")
