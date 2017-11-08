# -*- coding: utf-8 -*-

import pandas as pd

from ..constants import CID_MESH_URL


def get_cid_mesh_df(url=None):
    """

    :param Optional[str] url: The URL of the CID-MeSH mapping file
    :rtype pandas.DataFrame
    """
    return pd.read_csv(
        url or CID_MESH_URL,
        sep='\t',
        usecols=[0, 1]
    )
