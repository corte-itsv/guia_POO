class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return 2 * self.width + 2 * self.length



if __name__ == "__main__":
    rect = Rectangle(10, 4)
    print("Area =",rect.area(),"Perimeter =",rect.perimeter())