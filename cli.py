#!/usr/bin/env pipenv run python
import click
from shoppinglist.main import Main


@click.command()
@click.argument('shopping_list_file', type=click.Path(exists=True))
def cli(shopping_list_file):
    main = Main(shopping_list_file)
    click.echo(main.process_file())


if __name__ == '__main__':
    cli()
