class Notebook:
    def __init__(self, notas):
        self.notas = notas

    def add_note(self, note):
        self.notas.append(note)

    def show_notes(self):
        for i in range(len(self.notas)):
            print(f"{i+1}. {self.notas[i]}")

n1 = Notebook([])
n1.add_note("Buy groceries")
n1.add_note("Read a book")
n1.add_note("Call the doctor")
n1.show_notes()