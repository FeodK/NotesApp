import datetime

class Note:
    def __init__(self, id, title, message, timestamp=None):
        self.id = id
        self.title = title
        self.message = message
        self.timestamp = timestamp or datetime.datetime.now().isoformat()

    def __repr__(self):
        return f"Note(id={self.id}, title={self.title}, message={self.message}, timestamp={self.timestamp})"
