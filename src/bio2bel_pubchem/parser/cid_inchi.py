# -*- coding: utf-8 -*-

import logging
import os
from urllib.request import urlretrieve

import pandas as pd

from ..constants import CID_INCHI_URL, DATA_DIR

log = logging.getLogger(__name__)

CID_INCHI_DATA_PATH = os.path.join(DATA_DIR, 'CID-InChI-Key.gz')


def download_cid_inchi_data(force_download=False):
    """Downloads the CID InChI Info

    :param bool force_download: If true, overwrites a previously cached file
    :rtype: str
    """
    if os.path.exists(CID_INCHI_DATA_PATH) and not force_download:
        log.info('using cached data at %s', CID_INCHI_DATA_PATH)
    else:
        log.info('downloading %s to %s', CID_INCHI_URL, CID_INCHI_DATA_PATH)
        urlretrieve(CID_INCHI_URL, CID_INCHI_DATA_PATH)

    return CID_INCHI_DATA_PATH


def get_cid_inchi_df(url=None, cache=True, force_download=False):
    """

    :param Optional[str] url: The URL of the CID-InChI mapping file
    :rtype pandas.DataFrame
    """
    if url is None and cache:
        url = download_cid_inchi_data(force_download=force_download)

    return pd.read_csv(
        url or CID_INCHI_URL,
        sep='\t',
    )
