from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class MyEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"File created: {event.src_path}")

    def on_deleted(self, event):
        print(f"File deleted: {event.src_path}")

    def on_modified(self, event):
        print(f"File modified: {event.src_path}")

    def on_moved(self, event):
        print(f"File moved: {event.src_path} to {event.dest_path}")

paths = ["test2.py", "test.py"]
event_handler = MyEventHandler()

observer = Observer()

for path in paths:
    observer.schedule(event_handler, path, recursive=True)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

