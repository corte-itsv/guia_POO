class Notebook:
    def __init__(self):
        self.note = []
        
    def add_note(self, note):
        return self.note.append(note)

    def show_note(self):
        for i, note in enumerate(self.note, start=1):
            print(f"{i}. {note}")

nb = Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_note()