import sys
import argparse


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