class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        
    def show_notes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")

nk = Notebook()
nk.add_note("Buy groceries")
nk.add_note("Read a book")
nk.add_note("Call the doctor")
nk.show_notes()