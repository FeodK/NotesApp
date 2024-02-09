from modules.note import Note
import json
import os

class NoteRepository:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_notes(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                return [Note(**note_data) for note_data in json.load(file)]
        return []

    def save_notes(self, notes):
        with open(self.file_path, "w") as file:
            json.dump([note.__dict__ for note in notes], file, indent=4)
