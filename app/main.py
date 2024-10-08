from pipeline.extract import extract_data_from_xlsx
from pipeline.load import load_xlsx
from pipeline.transform import concat_dataframes

if __name__ == '__main__':

    path = 'data/input'

    lista_dataframes = extract_data_from_xlsx(path)
    dataframe = concat_dataframes(lista_dataframes)
    load_xlsx(dataframe, 'data/output', 'output')
