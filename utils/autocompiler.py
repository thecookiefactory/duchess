from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from tasks import build


class AssetsEventHandler(PatternMatchingEventHandler):
    def on_any_event(self, event):
        build()


def watch_assets(path):
    event_handler = AssetsEventHandler(
        patterns=['*.sass', '*.js'],
        ignore_patterns=['*.min.js'],
        ignore_directories=True,
    )
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
