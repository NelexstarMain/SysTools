
import yaml

def load_config(file_path: str) -> dict:
    """
    Loads the YAML configuration file.

    Args:
        file_path (str): Path to the YAML file.

    Returns:
        dict: Configuration data as a dictionary.
    """
    
    try:
        with open(file_path, 'r') as config_file:
            return yaml.safe_load(config_file)
    
    except FileNotFoundError:
        print("FileNotFoundError")

