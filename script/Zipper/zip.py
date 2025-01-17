import zipfile
import os

def zip_file(file_path, zip_name) -> None:
    print(f"Zipping file: {file_path}")
    with zipfile.ZipFile(zip_name, "a") as zipped: 
        zipped.write(file_path, arcname=os.path.basename(file_path))

def zip_directory(dir_path, zip_name):
    with zipfile.ZipFile(zip_name, 'a', zipfile.ZIP_DEFLATED) as zipf: 
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                print(f"Zipping file: {file_path}")
                zipf.write(file_path, arcname=os.path.relpath(file_path, dir_path))

def zip(path, zip_name=None) -> None:
    if zip_name is None:
        if os.path.isfile(path):
            zip_name = os.path.splitext(path)[0] + ".zip"
        elif os.path.isdir(path):
        
            zip_name = os.path.join(os.path.dirname(path), os.path.basename(path) + ".zip")
    
    if os.path.isfile(path):
        zip_file(path, zip_name)
    elif os.path.isdir(path):
        zip_directory(path, zip_name)