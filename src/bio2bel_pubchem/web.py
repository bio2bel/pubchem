# -*- coding: utf-8 -*-

import logging
import flask_admin
from flask import Flask
from flask_admin.contrib.sqla import ModelView

from bio2bel_pubchem.manager import Manager
from bio2bel_pubchem.models import *

log = logging.getLogger(__name__)

app = Flask(__name__)
admin = flask_admin.Admin(app, url='/')

manager = Manager()

admin.add_view(ModelView(Substance, manager.session))
admin.add_view(ModelView(Compound, manager.session))
admin.add_view(ModelView(SubstanceXref, manager.session))

if __name__ == '__main__':
    logging.basicConfig(level=20)
    log.setLevel(20)
    log.info('starting app with connection: %s', manager.engine.url)
    app.run(debug=True, host='0.0.0.0', port=5000)
