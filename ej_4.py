class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

s1 = Student("Alice", [85, 90, 78, 92, 88])

print(f"{s1.name}'s average grade: {s1.average()}")