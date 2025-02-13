from utils.models.affranchissement_mas import AffranchissementMas
from utils.check_file import file_is_correct, get_src_path_to_filename
from utils.mas_csv_processing import read_and_clean_mas_csv, rename_mas_colums, convert_df_to_json_str, convert_df_to_json_obj
from utils.http.http_post_mas import http_post_mas


def send_mas_affranchissements(file_path: str):
    '''
    Vérifie que le fichier traité est correct puis nettoyage des
    données csv et conversion en json.
    '''
    if not file_is_correct(get_src_path_to_filename(file_path)):
        return
    cleaned_mas = read_and_clean_mas_csv(file_path)
    cleaned_mas = rename_mas_colums(cleaned_mas)
    affranchissements_mas = convert_df_to_json_obj(cleaned_mas)
    print(affranchissements_mas[0].nom_departement)
    affranchissements_mas_is_valid = len([AffranchissementMas.validate(affr) for affr in affranchissements_mas if affr is False]) <= 0
    if(affranchissements_mas_is_valid):
        json_str = convert_df_to_json_str(cleaned_mas)
        http_post_mas(json_str, file_path)
    return
    