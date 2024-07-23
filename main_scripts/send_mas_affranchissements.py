import sys
import argparse

from utils.check_file import file_is_correct, get_src_path_to_filename
from utils.mas_csv_processing import read_and_clean_mas_csv, rename_mas_colums


def prepare_args() -> argparse.Namespace:
    try:
        parser = argparse.ArgumentParser(description='Surveille si un fichier MAS a ete cree puis formatte et envoie les donnees vers le serveur')
        parser.add_argument('--mas-folder-path', help='Le chemin du repertoire dans lequel sont crees les fichiers MAS. Chemin absolu recommande')
        args = parser.parse_args()
        if(not args.mas_folder_path):
            raise argparse.ArgumentError(
                argument=args.mas_folder_path,
                message="Le chemin vers le repertoire du MAS n'est pas specifie\n --mas-folder-path <chemin du repertoire MAS>"
            )
        return args
    except argparse.ArgumentError as e:
        print(e.message)
        sys.exit()

def send_mas_affranchissements(file_path: str):
    if not file_is_correct(get_src_path_to_filename(file_path)):
        print(f"incorrect file detected : {file_path}")
        return
    cleaned_mas = read_and_clean_mas_csv(file_path)
    cleaned_mas = rename_mas_colums(cleaned_mas)
    print(cleaned_mas)