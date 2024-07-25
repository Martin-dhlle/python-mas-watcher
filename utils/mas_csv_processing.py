import pandas as pd
from types import SimpleNamespace
from json import loads, dumps

from config.mas_csv_config import COLONNES
from utils.models.affranchissement_mas import AffranchissementMas


def read_and_clean_mas_csv(mas_file_path: str) -> pd.DataFrame:
    '''
    Lecture du fichier .csv et filtrage avec les colonnes définies
    dans la configuration.
    '''
    with open(mas_file_path, newline='', encoding='utf-8') as csvfile:
        default_mas = pd.read_csv(csvfile, delimiter=';', quotechar='|')
        cleaned_mas = default_mas[[col[0] for col in COLONNES]]

        for col in [COLONNES[2][0], COLONNES[5][0]]:
            # Replace commas with dots
            cleaned_mas.loc[:, col] = cleaned_mas[col].str.replace(',', '.')
            # Convert to float
            cleaned_mas.loc[:, col] = cleaned_mas[col].astype(float)
        
        return cleaned_mas

def rename_mas_colums(mas_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
    Renommage des colonnes nettoyées afin de faciliter le traitement 
    de données par l'API.
    '''
    rename_dict = {col[0]: col[1] for col in COLONNES}
    renamed_mas_dataframe = mas_dataframe.rename(columns=rename_dict)
    return renamed_mas_dataframe

def convert_df_to_json_str(mas_dataframe: pd.DataFrame) -> str:
    '''
    Conversion du DataFrame en format JSON.
    '''
    json_mas_data = mas_dataframe.to_json(orient="table")
    parsed = loads(json_mas_data)["data"]
    json = dumps(parsed)
    return json

def convert_df_to_json_obj(mas_dataframe: pd.DataFrame) -> list[AffranchissementMas]:
    '''
    Conversion du DataFrame en format JSON puis conversion du JSON 
    en dictionnaire.
    '''
    json_mas_data = mas_dataframe.to_json(orient="table")
    parsed_to_namespace = loads(json_mas_data, object_hook=lambda d: SimpleNamespace(**d))
    parsed_to_obj: list[AffranchissementMas] = [
        AffranchissementMas(**vars(item)) for item in parsed_to_namespace.data
    ]
    
    return parsed_to_obj