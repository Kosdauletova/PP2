#the squares of numbers up to some n

def square_generator(n):
    for i in range(1, n+1):
        yield i**2

n = int(input())
gen = square_generator(n)

for square in gen:
    print(square)


#even numbers between 0 and n


def even_numbers(n):
    for i in range(0, n+1, 2):
        yield str(i)


n=int(input())

result = ", ".join(even_numbers(n))
print(result)




#divisible by 3 and 4


def divisible_by(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n=int(input())
for num in divisible_by(n):
    print(num, end=" ")



#squares, from a to b


def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a=int(input())
b=int(input())

for square in squares(a, b):
    print(square)



#from n down to 0
def down(n):
    for i in range(n, -1, -1):
        yield i

n=int(input())

for num in down(n):
    print(num)