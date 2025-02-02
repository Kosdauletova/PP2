class Shape:
    def __init__(self):
        pass

    def area(self):
        print("Shape's area is 0")

    
class Square(Shape):
    def __init__(self, length):
        self.length = length


    def area(self):
        print(f"The area of the square: {self.length * self.length}")


length = float(input())
shape = Shape()
square = Square(length)

shape.area()
square.area()
