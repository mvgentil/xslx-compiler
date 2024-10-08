from typing import List

import pandas as pd


def concat_dataframes(dataframes_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    funçao para transformar uma lista de datagrames em um unico dataframe
    """

    return pd.concat(dataframes_list, ignore_index=True)
