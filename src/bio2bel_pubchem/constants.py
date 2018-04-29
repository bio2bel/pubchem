# -*- coding: utf-8 -*-

"""This module contains constants for use by all aspects of the library"""

from bio2bel.utils import get_connection, get_data_dir
import os

MODULE_NAME = 'pubchem'
DATA_DIR = get_data_dir(MODULE_NAME)
DEFAULT_CACHE_CONNECTION = get_connection(MODULE_NAME)

#: Map from compound to InChI (4.5 GB)
CID_INCHI_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-InChI-Key.gz'
CID_INCHI_DATA_PATH = os.path.join(DATA_DIR, 'CID-InChI-Key.gz')

#: Map from compound to MeSH term (3.7 MB)
CID_MESH_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-MeSH'
CID_MESH_DATA_PATH = os.path.join(DATA_DIR, 'CID-MeSH')

#: Map from compound to substance (1.2 GB)
CID_SID_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Compound/Extras/CID-SID.gz'
CID_SID_DATA_PATH = os.path.join(DATA_DIR, 'CID-SID.gz')

#: Map from substance to MeSH term (38 MB)
SID_MESH_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-MeSH'

#: Map from substance to (2.1 GB) (SID, Source Name, Registry identifier, Optional[CID])
SID_MAP_URL = 'ftp://ftp.ncbi.nih.gov/pubchem/Substance/Extras/SID-Map.gz'
