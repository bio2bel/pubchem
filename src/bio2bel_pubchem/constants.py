# -*- coding: utf-8 -*-

"""This module contains constants for use by all aspects of the library"""

import os

BIO2BEL_DIR = os.environ.get('BIO2BEL_DIRECTORY', os.path.join(os.path.expanduser('~'), '.pybel', 'bio2bel'))
DATA_DIR = os.path.join(BIO2BEL_DIR, 'pubchem')
os.makedirs(DATA_DIR, exist_ok=True)

DEFAULT_DATABASE_NAME = 'pubchem.db'
DEFAULT_DATABASE_PATH = os.path.join(DATA_DIR, DEFAULT_DATABASE_NAME)
DEFAULT_CACHE_CONNECTION = os.environ.get('BIO2BEL_DB', 'sqlite:///' + DEFAULT_DATABASE_PATH)

#: Map from compound to InChI (4.5 GB)
CID_INCHI_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-InChI-Key.gz'

#: Map from compound to MeSH term (3.7 MB)
CID_MESH_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-MeSH'

#: Map from compound to substance (1.2 GB)
CID_SID_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-SID.gz'

#: Map from substance to MeSH term (38 MB)
SID_MESH_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-MeSH'

#: Map from substance to (2.1 GB) (SID, Source Name, Registry identifier, Optional[CID])
SID_MAP_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-Map.gz'
