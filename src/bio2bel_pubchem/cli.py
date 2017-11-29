# -*- coding: utf-8 -*-

"""Run this script with :code:`python3 -m bio2bel_pubchem"""

from __future__ import print_function

import logging

import click

from .constants import DEFAULT_CACHE_CONNECTION
from .manager import Manager


@click.group()
def main():
    """PubChem to BEL"""
    logging.basicConfig(level=logging.INFO)


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def drop(connection):
    """Download and insert data"""
    m = Manager(connection=connection)
    m.drop_all()


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
def populate(connection):
    """Download and insert data"""
    m = Manager(connection=connection)
    m.populate()


@main.command()
@click.option('-c', '--connection', help="Defaults to {}".format(DEFAULT_CACHE_CONNECTION))
@click.option('-v', '--debug', is_flag=True)
@click.option('-p', '--port')
@click.option('-h', '--host')
def web(connection, debug, port, host):
    """Run the web app"""
    from .web import create_application
    app = create_application(connection=connection, url='/')
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
