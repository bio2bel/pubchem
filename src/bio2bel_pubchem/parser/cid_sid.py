import pandas as pd

from ..constants import CID_SID_URL


def get_cid_sid_df(url=None):
    """

    :param Optional[str] url: The URL of the CID-InChI mapping file
    :rtype pandas.DataFrame
    """
    return pd.read_csv(
        url or CID_SID_URL,
        sep='\t',
        compression='gzip',
    )
