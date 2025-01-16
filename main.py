import click
from config.config_loader import load_config
from script.Scanner.system_scanner import CurrentFileScanner

@click.command()
@click.option('--scan', type=str, help="Run scanning for a specific file or word")
def scan(scan):
    config = load_config("config/config.yaml")  
    scanner = CurrentFileScanner(config=config, name=str(scan))
    if scan:
        click.echo(f"Scanning for: {scan}")
        scanner.run()  
    else:
        click.echo("No input provided for scanning.")

if __name__ == "__main__":
    scan()
