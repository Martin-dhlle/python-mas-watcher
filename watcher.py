import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from main_scripts.send_mas_affranchissements import prepare_args, send_mas_affranchissements


class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            send_mas_affranchissements(event.src_path)
    
    def on_modified(self, event):
        if not event.is_directory:
            print(f"New file detected: {event.src_path}")
            send_mas_affranchissements(event.src_path)

if __name__ == "__main__":
    args = prepare_args()
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, args.mas_folder_path, recursive=False)
    
    try:
        observer.start()
        print(f"Watching for new files in {args.mas_folder_path}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
