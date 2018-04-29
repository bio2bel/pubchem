# -*- coding: utf-8 -*-

import logging
import os
from urllib.request import urlretrieve

import pandas as pd

from ..constants import CID_MESH_DATA_PATH, CID_MESH_URL

log = logging.getLogger(__name__)


def download_cid_mesh_data(force_download=False):
    """Downloads the CID MeSH Info

    :param bool force_download: If true, overwrites a previously cached file
    :rtype: str
    """
    if os.path.exists(CID_MESH_DATA_PATH) and not force_download:
        log.info('using cached data at %s', CID_MESH_DATA_PATH)
    else:
        log.info('downloading %s to %s', CID_MESH_URL, CID_MESH_DATA_PATH)
        urlretrieve(CID_MESH_URL, CID_MESH_DATA_PATH)

    return CID_MESH_DATA_PATH


def get_cid_mesh_df(url=None, cache=True, force_download=False):
    """Gets the CID to MeSH mapping

    :param Optional[str] url: The URL of the CID-MeSH mapping file
    :rtype pandas.DataFrame
    """
    if url is None and cache:
        url = download_cid_mesh_data(force_download=force_download)

    log.info('reading %s', url or CID_MESH_URL)
    return pd.read_csv(
        url or CID_MESH_URL,
        sep='\t',
        usecols=[0, 1]
    )
