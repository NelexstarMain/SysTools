import click
from config.loader import load_config
from modules.Scanner.scanner import CurrentFileScanner
from modules.Zipper import zip  
from modules.Structurer import parser

@click.group()
def cli():
    """Main entry point for the file scanning tool."""
    pass

@click.command()
@click.argument('scan', type=str)
@click.argument('print', type=bool)
def scan(scan, print):
    """Scan for a specific file or word."""
    config = load_config("config/settings.yaml")
    scanner = CurrentFileScanner(config=config, name=str(scan), print=print)
    
    if scan:
        click.echo(f"Scanning for: {scan}")
        scanner.run()
    else:
        click.echo("No input provided for scanning.")

@click.command()
def exit():
    """Exit the CLI tool."""
    click.echo("Exiting program.")
    raise SystemExit

@click.command()
@click.argument('files', type=str)  
def zipit(files):
    """Zip the specified files into a single archive."""
    zip(files)
    click.echo(f"File have been zipped")

@click.command()
@click.argument('path', type=str)
def copy(path) -> None:
    """Copy specified directory structure."""
    copy_element = parser.Parser(path, "./config/structures/removals.json", "./config/structures/structures.json")
    copy_element.get_removals()
    copy_element.scan_directory()
    copy_element.save_to_json()
    
cli.add_command(scan)
cli.add_command(exit)
cli.add_command(zipit)
cli.add_command(copy)

if __name__ == "__main__":
    cli()
