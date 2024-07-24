from config.path import MAS_DEFAULT_FILE_NAME, MAS_FILE_EXTENSION


def get_src_path_to_filename(path: str) -> str:
    '''
    Récupère le nom du fichier son chemin
    '''
    filename = path.split("/")[-1]
    return filename

def file_is_correct(filename: str) -> bool:
    '''
    Vérifie que le fichier traité soit bien un fichier d'affranchissements MAS
    '''
    found_file_valid = filename.find(MAS_DEFAULT_FILE_NAME) != -1 and filename.find(MAS_FILE_EXTENSION) != -1
    return found_file_valid