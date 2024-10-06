from pipeline.extract import extract_data_from_xlsx

path = "data/input"
lista = extract_data_from_xlsx(path)

print(lista)