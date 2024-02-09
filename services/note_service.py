from modules.note import Note

class NoteService:
    def __init__(self, note_repository):
        self.note_repository = note_repository

    def add_note(self, title, message):
        notes = self.note_repository.load_notes()
        new_note_id = len(notes) + 1
        new_note = Note(new_note_id, title, message)
        notes.append(new_note)
        self.note_repository.save_notes(notes)
        return new_note

    def list_notes(self):
        return self.note_repository.load_notes()

    def edit_note(self, note_id, title, message):
        notes = self.note_repository.load_notes()
        for note in notes:
            if note.id == note_id:
                note.title = title
                note.message = message
                self.note_repository.save_notes(notes)
                return note
        return None

    def delete_note(self, note_id):
        notes = self.note_repository.load_notes()
        for note in notes:
            if note.id == note_id:
                notes.remove(note)
                self.update_note_ids(notes)
                self.note_repository.save_notes(notes)
                return True
        return False

    def update_note_ids(self, notes):
        for i, note in enumerate(notes, start=1):
            note.id = i

    def filter_notes_by_date(self, date):
        notes = self.note_repository.load_notes()
        filtered_notes = [note for note in notes if note.timestamp.split('T')[0] == date]
        return filtered_notes