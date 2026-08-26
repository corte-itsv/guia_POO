class Notebook:
    def __init__(self, notas):
        self.notas=notas

    def addnote(self, note):
        self.notas.append(note)
        return self.notas

    def show_notes(self):
        for i, note in enumerate(self.notas, start=1):
            print(f"{i}. {note}")

n1 = Notebook([])
n1.addnote("Buy groceries")
n1.addnote("Read a book")
n1.addnote("Call the doctor")
n1.show_notes()

        