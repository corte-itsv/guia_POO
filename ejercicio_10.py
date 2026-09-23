class Notebook:
    def __init__(self, lista):
        self.lista = lista
        
    def add_note(self, note):
       self.lista.append(note)
       return self.lista

    def show_notes(self):
        contador = 1
        for i in self.lista:
            print(f"{contador}. {i}")    
            contador += 1
            
notebook1 = Notebook([])
notebook1.add_note("Buy groceries")
notebook1.add_note("Read a book")
notebook1.add_note("Call the doctor")
notebook1.show_notes()