import click
from .main import Main

@click.command()
@click.argument('prices_file', type=click.Path(exists=True))
@click.argument('shopping_list_file', type=click.Path(exists=True))
@click.option('--with-count', is_flag=True, help='Display the count for each item')
def cli(prices_file, shopping_list_file, with_count):
    main = Main(prices_file, shopping_list_file)
    click.echo(main.process_file(with_count))

