import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        else:
            print(f'File {event.src_path} has been created.')
            destination_folder = "C:/Users/shubh/workspace/downloads"
            shutil.copy(event.src_path, destination_folder)
            print(f'File copied to {destination_folder}.')

def monitor_directory(path):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print("observer started")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    directory_to_watch = "C:/Users/shubh/workspace/uploads"
    print(directory_to_watch)
    monitor_directory(directory_to_watch)
