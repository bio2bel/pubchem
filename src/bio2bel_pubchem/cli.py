# -*- coding: utf-8 -*-

"""Run this script with :code:`python3 -m bio2bel_pubchem"""

from __future__ import print_function

import logging

import click

from .constants import DEFAULT_CACHE_CONNECTION
from .manager import Manager


@click.group()
def main():
    """ChEBI to BEL"""
    logging.basicConfig(level=10, format="%(asctime)s - %(levelname)s - %(message)s")


@main.command()
@click.option('-c', '--connection', help="Custom OLS base url. Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def drop(connection):
    """Download and insert data"""
    m = Manager(connection=connection)
    m.drop_all()


@main.command()
@click.option('-c', '--connection', help="Custom OLS base url. Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def populate(connection):
    """Download and insert data"""
    m = Manager(connection=connection)
    m.populate()


@main.command()
def web():
    """Run the web app"""
    from .web import app
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
