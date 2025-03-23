import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")


    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"Change the coordinates: ({self.x}, {self.y})")


    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return distance
    

x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()
point2.show()

distance= point1.dist(point2)
print(f"The distance between 2 points : {distance}")