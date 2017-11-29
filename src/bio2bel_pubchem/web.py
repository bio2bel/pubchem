# -*- coding: utf-8 -*-

import logging

import flask_admin
from flask import Flask
from flask_admin.contrib.sqla import ModelView

from bio2bel_pubchem.manager import Manager
from bio2bel_pubchem.models import *

log = logging.getLogger(__name__)


def create_application(connection=None, url=None):
    """Builds a Flask application

    :param Optional[str] connection:
    :param Optional[str] url:
    :rtype: flask.Flask
    """
    app = Flask(__name__)
    manager = Manager(connection=connection)
    add_admin(app, manager.session, url=url)
    return app


def add_admin(app, session, **kwargs):
    """Adds the administrator views

    :param flask.Flask app: A Flask application
    :param session:
    """
    admin = flask_admin.Admin(app, template_mode='bootstrap3', **kwargs)
    admin.add_view(ModelView(Substance, session))
    admin.add_view(ModelView(Compound, session))
    admin.add_view(ModelView(SubstanceXref, session))
    return admin


if __name__ == '__main__':
    logging.basicConfig(level=20)
    log.setLevel(20)
    app = create_application()
    app.run(debug=True, host='0.0.0.0', port=5000)
