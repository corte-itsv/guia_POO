class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        promedio = sum(self.marks) / len(self.marks)
        return promedio

s1 = student("Alice", [85, 90, 78, 92, 88])
print(f"{s1.name} average grade: {s1.average()} ")