import os
import logging

import click


from {{cookiecutter.project_name}}.main import hello


logger = logging.getLogger('{{cookiecutter.project_name}}')
sh = logging.StreamHandler()
logger.addHandler(sh)
logger.setLevel(logging.INFO)


@click.group()
@click.option('--debug', is_flag=True, default=False)
def cli(debug):
    # Set DEBUG logging based on ENV or --debug CLI flag
    if debug or os.environ.get('DEBUG'):
        logger.setLevel(logging.DEBUG)


@cli.command
@click.argument('name')
def hello(name: str):
    hello(name)
