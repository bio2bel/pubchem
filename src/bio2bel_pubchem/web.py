# -*- coding: utf-8 -*-

from bio2bel_pubchem.manager import Manager

if __name__ == '__main__':
    manager = Manager()
    app = manager.get_flask_admin_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
