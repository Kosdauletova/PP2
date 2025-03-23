class Shape:
    def __init__(self):
        pass


    def area(self):
        print("The area of shape: 0")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        print(f"Area of rectangle: {self.length * self.width}")


length = float(input())
width = float(input())

shape = Shape()
rectangle = Rectangle(length, width)

shape.area()
rectangle.area()

