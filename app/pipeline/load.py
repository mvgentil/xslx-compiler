import pandas as pd
import os




def load_xlsx(dataframe: pd.DataFrame, output_path: str, file_name: str) -> str:
    '''
    recebe o dataframe, diretorio de saída e o nome do arquivo e exporta em um unico xlsx
    se a pasta não existir, cria antes de exportar
    '''
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    dataframe.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso!"
