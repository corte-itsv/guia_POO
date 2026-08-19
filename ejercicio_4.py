class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks) 
        rounded_average = round(self.average(), 1)
        return rounded_average

s1 = Student("Alice", [85, 90, 78, 92, 88])
print(f"{s1.name}'s Average Marks: {s1.average()}")