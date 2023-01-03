import os
import click

__author__ = "{{cookiecutter.etl_author}}"
__copyright__ = ""
__credits__ = []
__version__ = "0.1.0"
__maintainer__ = "{{cookiecutter.etl_author}}"
__email__ = "{{cookiecutter.etl_author}}"
__status__ = ""

# Click is the modern way to handle command line arguments.
@click.command()
@click.argument('date')

def main(date):
    print("Hello ETL World!")
    click.echo("This is the main function.")
    click.echo("Given the same inputs it should produce the exact same output.")
    click.echo(f"This is the date passed to the main function: {date}")
    
    click.echo("These are the environment variables available:\n")
    
    for k, v in os.environ.items():
        click.echo(f'    {k}={v}')

if __name__ == "__main__":
    main()
