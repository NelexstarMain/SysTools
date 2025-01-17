import click
from config.config_loader import load_config
from script.Scanner.system_scanner import CurrentFileScanner

@click.group()
def cli():
    """Main entry point for the file scanning tool."""
    pass

@click.command()
@click.argument('scan')
def scan(scan):
    """Scan for a specific file or word."""
    config = load_config("config/config.yaml")
    scanner = CurrentFileScanner(config=config, name=str(scan))
    
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


cli.add_command(scan)
cli.add_command(exit)


