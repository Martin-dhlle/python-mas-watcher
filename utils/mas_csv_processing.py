import pandas as pd

from config.mas_csv_config import COLONNES


def read_and_clean_mas_csv(mas_file_path: str) -> pd.DataFrame:
    with open(mas_file_path, newline='', encoding='utf-8') as csvfile:
        default_mas = pd.read_csv(csvfile, delimiter=';', quotechar='|')
        cleaned_mas = default_mas[[col[0] for col in COLONNES]]
        return cleaned_mas

def rename_mas_colums(mas_dataframe: pd.DataFrame) -> pd.DataFrame:
    rename_dict = {col[0]: col[1] for col in COLONNES}
    renamed_mas_dataframe = mas_dataframe.rename(columns=rename_dict)
    return renamed_mas_dataframe