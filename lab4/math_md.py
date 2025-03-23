#convert degree to radian

import math

def degrees_to_radians(degrees):
    return degrees * (math.pi/180)

degrees = float(input("Input degree: "))

radians = degrees_to_radians(degrees)
print(f"Output radian: {radians:.6f}")



#calculate the area of a trapezoid

height = float(input("Height: "))
first = float(input("Base, first value: "))
second = float(input("Base, second value: "))

area = (1/2) * (first + second) * height

print("Expected Output: ", area)



#the area of a polygon

import math

num = int(input("Input number of sides: "))
len = int(input("Input the length of a side: "))

if num==4:
    area = len**2

else:
    area = (num * len**2)/(4 * math.tan(math.pi/num))

print("The area of the polygon is: ", area)
    


#the area of a parallelogram

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
output = base * height

print(f"Expected Output: {output} ")

