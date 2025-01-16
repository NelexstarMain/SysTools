from config.config_loader import load_config
from script.Scanner.system_scanner import CurrentFileScanner

if __name__ == "__main__":
    config = load_config("config/config.yaml")  
    scanner = CurrentFileScanner(config=config)
    scanner.run()