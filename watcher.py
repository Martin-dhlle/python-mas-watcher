import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from main_scripts.send_mas_affranchissements import send_mas_affranchissements
from main_scripts.manage_args_env import validate_environment, prepare_args

'''
Le script principal qui gère les événements du système de fichier.
'''
class NewFileHandler(FileSystemEventHandler):
    # Quand un fichier est créé dans le répertoire du MAS
    def on_created(self, event):
        if not event.is_directory:
            print(f"Nouveau fichier détecté: {event.src_path}")
            send_mas_affranchissements(event.src_path)
    
    # Quand un fichier est modifié dans le répertoire du MAS
    def on_modified(self, event):
        if not event.is_directory:
            print(f"Nouveau fichier détecté: {event.src_path}")
            send_mas_affranchissements(event.src_path)

if __name__ == "__main__":
    validate_environment()
    args = prepare_args() # Récupération des arguments de l'application
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, args.mas_folder_path, recursive=False)
    
    try:
        observer.start()
        print(f"En attente de nouveau fichier dans le répertoire : {args.mas_folder_path}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
