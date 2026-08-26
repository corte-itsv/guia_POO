class Notebook:
    def __init__(self, note_list):
        self.note_list = note_list
        
    def add_note(self, note):
        self.note_list.append(note)
    
    def show_notes(self):
        note_number = 1
        for note in self.note_list:
            print(f"{note_number}. {note}")
            note_number =  note_number + 1
            
n1 = Notebook([])

n1.add_note("Buy groceries")
n1.add_note("Read a book")
n1.add_note("Call the doctor")

n1.show_notes()