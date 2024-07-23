from utils.check_file import file_is_correct, get_src_path_to_filename
from utils.mas_csv_processing import read_and_clean_mas_csv, rename_mas_colums, convert_df_to_json_obj


def send_mas_affranchissements(file_path: str):
    if not file_is_correct(get_src_path_to_filename(file_path)):
        return
    cleaned_mas = read_and_clean_mas_csv(file_path)
    cleaned_mas = rename_mas_colums(cleaned_mas)
    json_mas = convert_df_to_json_obj(cleaned_mas)

    # test logs
    print(json_mas[0])