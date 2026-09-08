class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)

if __name__ == "__main__":
    s1 = Student("Alice", [85, 90, 78, 92, 88])
    print(s1.name , "Average Grade:",s1.average())