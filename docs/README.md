# SysTools

This project is designed for scanning and manipulating files.

## Table of Contents
1. [Description](#description)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Usage](#usage)


## Description

This project is a command-line tool that can scan all files and directories to search for file paths. It also allows users to zip files and folders given their paths. The tool is controlled via a simple CLI interface.

Currently, the available commands are:

- **scan**: Scans directories and lists all file paths.
- **zipit**: Zips the files and directories when given their paths.
- **exit**: Exits the application.

More features are planned in the future.

## Technologies

The project uses the following technologies:

- Python 3.x
- [Click](https://click.palletsprojects.com/) - For building the command-line interface.
- [zipfile](https://docs.python.org/3/library/zipfile.html) - For zipping files.
- [PyYaml](https://pyyaml.org/) - For managing configuration files.
- [colorama](https://pypi.org/project/colorama/) - For adding colors to terminal output.

## Installation

Follow these steps to get the project up and running:

1. Clone the repository:
    ```bash
    git clone https://github.com/NelexstarMain/SysTools.git
    ```

2. Navigate into the project directory:
    ```bash
    cd SysTools
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the project, start the CLI application using the following command:

```bash
python main.py

```

Once the application is running, you can use the following commands:

![scan](/assets/scan.png)

- **scan**: Scans the directories and lists all file paths.

- **zipit**: Zips the specified files and folders.

- **exit**: Exits the application.

- **copy**: Copy Folders and files structure and saves to json.

```json
{
    "main.py": null,
    "LICENSE": null,
    "requirements.txt": null,
    "setup.py": null,
    "config": {
        "settings.yaml": null,
        
    },
    "docs": {
        "INSTALL.md": null,
        "README.md": null,
        "USAGE.md": null
    },
    "modules": {
        "login": {
            "scanner.py": null,
            "__init__.py": null
        },
    },
    "tests": {
        "test1.py": null,
        "test2.py": null
    }
}

```



If you need help or a list of available commands, run:


```bash
python main.py --help
```

This will display all the available commands and options.


