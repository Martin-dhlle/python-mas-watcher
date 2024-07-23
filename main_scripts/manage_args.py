import sys
import argparse


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