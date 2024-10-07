import os
import glob
import pandas as pd
from typing import List



def extract_data_from_xlsx(path: str) -> List[pd.DataFrame]:

    '''
    função para ler os arquivos da
    pasta data/input e retorna uma lista de dataframes

    args: input_path (str) : caminho da pasta com os arquivos

    return lista de dataframes

    '''

    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    dataframes_xlsx = []
    for file in all_files:
        dataframes_xlsx.append(pd.read_excel(file))

    return dataframes_xlsx

