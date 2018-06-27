import click
from .main import Main

@click.command()
@click.argument('prices_file', type=click.Path(exists=True))
@click.argument('shopping_list_file', type=click.Path(exists=True))
def cli(prices_file, shopping_list_file):
    main = Main(prices_file, shopping_list_file)
    click.echo(main.process_file())

