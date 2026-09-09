class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def show_notes(self):
        for i, note in enumerate(self.notes, start=1):
            print(f"{i}. {note}")

cuaderno = Notebook()
cuaderno.add_note("Buy groceries")
cuaderno.add_note("Read a book")
cuaderno.add_note("Call the doctor")
cuaderno.show_notes()