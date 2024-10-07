import pandas as pd
from typing import List

'''
funçao para transformar uma lista de datagrames em um unico dataframe
'''


def concat_dataframes(dataframes_list: List[pd.DataFrame]) -> pd.DataFrame:
    
    return pd.concat(dataframes_list, ignore_index = True)