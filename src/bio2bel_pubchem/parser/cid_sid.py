# -*- coding: utf-8 -*-

import logging
import os
from urllib.request import urlretrieve

import pandas as pd

from ..constants import CID_SID_DATA_PATH, CID_SID_URL

log = logging.getLogger(__name__)


def download_cid_sid_data(force_download=False):
    """Downloads the CID SID Info

    :param bool force_download: If true, overwrites a previously cached file
    :rtype: str
    """
    if os.path.exists(CID_SID_DATA_PATH) and not force_download:
        log.info('using cached data at %s', CID_SID_DATA_PATH)
    else:
        log.info('downloading %s to %s', CID_SID_URL, CID_SID_DATA_PATH)
        urlretrieve(CID_SID_URL, CID_SID_DATA_PATH)

    return CID_SID_DATA_PATH


def get_cid_sid_df(url=None, cache=True, force_download=False):
    """

    :param Optional[str] url: The URL of the CID-InChI mapping file
    :rtype pandas.DataFrame
    """
    if url is None and cache:
        url = download_cid_sid_data(force_download=force_download)

    log.info('reading %s', url or CID_SID_URL)
    return pd.read_csv(
        url or CID_SID_URL,
        sep='\t',
        compression='gzip',
    )
