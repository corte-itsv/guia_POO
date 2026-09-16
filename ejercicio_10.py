class Notebook:
    def __init__(self):
        self.lista = []
    def add_note(self, note):
        self.lista.append(note)
    def show_notes(self):
        for i, note in enumerate(self.lista, start=1):
            print(f"{i}. {note}")

nb = Notebook()
nb.add_note("Buy groceries")
nb.add_note("Read a book")
nb.add_note("Call the doctor")
nb.show_notes()

