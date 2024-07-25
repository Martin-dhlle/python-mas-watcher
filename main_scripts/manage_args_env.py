import sys
import argparse

from config.request_config import MAS_API_KEY, API


def prepare_args() -> argparse.Namespace:
    '''
    Récupère et vérifie les arguments passées en ligne de commande
    '''
    try:
        parser = argparse.ArgumentParser(description='Surveille si un fichier MAS a ete créé puis formatte et envoie les données vers le serveur')
        parser.add_argument('--mas-folder-path', help='Le chemin du repertoire dans lequel sont créés les fichiers MAS. Chemin absolu recommandé')
        args = parser.parse_args()
        if(not args.mas_folder_path):
            raise argparse.ArgumentError(
                argument=args.mas_folder_path,
                message="Le chemin vers le répertoire du MAS n'est pas sépcifié\n --mas-folder-path <chemin du repertoire MAS>"
            )
        return args
    except argparse.ArgumentError as e:
        print(e.message)
        sys.exit()

def validate_environment():
    '''
    Verifie les variables d'environnement
    '''
    env_vars_to_check = {
        'MAS_API_KEY': MAS_API_KEY,
        'API': API
    }
    missing_vars = [name for name, value in env_vars_to_check.items() if value is None]
    if len(missing_vars) > 0:
        missing_vars_str = ", ".join(missing_vars)
        print(f"Variables d'environnement {missing_vars_str} manquantes")
        sys.exit()
    pass