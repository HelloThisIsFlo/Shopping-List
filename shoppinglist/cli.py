import click
from .main import Main

@click.command()
@click.option('--with-count', is_flag=True, help='Display the count for each item')
@click.option('--without-breakdown', is_flag=True, help='Hide the cost breakdown for each category')
@click.argument('shopping_list_file', type=click.Path(exists=True))
@click.argument('prices_file', type=click.Path(exists=True))
@click.argument('price_overrides_files', type=click.Path(exists=True), nargs=-1)
def cli(shopping_list_file, prices_file, price_overrides_files, with_count, without_breakdown):
    main = Main(shopping_list_file, prices_file, price_overrides_files)
    click.echo(main.process_files(with_count, with_breakdown=not without_breakdown))

