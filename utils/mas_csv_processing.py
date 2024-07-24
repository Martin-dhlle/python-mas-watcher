import pandas as pd
from types import SimpleNamespace
from json import loads

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
        return cleaned_mas

def rename_mas_colums(mas_dataframe: pd.DataFrame) -> pd.DataFrame:
    '''
    Renommage des colonnes nettoyées afin de faciliter le traitement 
    de données par l'API.
    '''
    rename_dict = {col[0]: col[1] for col in COLONNES}
    renamed_mas_dataframe = mas_dataframe.rename(columns=rename_dict)
    return renamed_mas_dataframe

def convert_df_to_json_obj(mas_dataframe: pd.DataFrame) -> list[AffranchissementMas]:
    '''
    Conversion du DataFrame en format JSON puis conversion du JSON 
    en dictionnaire.
    '''
    json_mas_data = mas_dataframe.to_json(orient="table")
    parsed_to_obj: list[AffranchissementMas] = loads(json_mas_data, object_hook=lambda d: SimpleNamespace(**d)).data
    return parsed_to_obj