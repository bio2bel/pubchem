# -*- coding: utf-8 -*-

import pandas as pd

from ..constants import CID_INCHI_URL


def get_cid_inchi_df(url=None):
    """

    :param Optional[str] url: The URL of the CID-InChI mapping file
    :rtype pandas.DataFrame
    """
    return pd.read_csv(
        url or CID_INCHI_URL,
        sep='\t',
    )
