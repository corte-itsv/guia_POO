class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f" {i}. {note}")

n = Notebook()
n.add_note("Buy groceries")
n.add_note("Read a book")
n.add_note("Call the doctor")
n.show_notes()