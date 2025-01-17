import click
from config.config_loader import load_config
from script.Scanner.system_scanner import CurrentFileScanner
from script.Zipper.zip import zip  

@click.group()
def cli():
    """Main entry point for the file scanning tool."""
    pass

@click.command()
@click.argument('scan', type=str)
@click.argument('print', type=bool)
def scan(scan, print):
    """Scan for a specific file or word."""
    config = load_config("config/config.yaml")
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

cli.add_command(scan)
cli.add_command(exit)
cli.add_command(zipit)

if __name__ == "__main__":
    cli()
