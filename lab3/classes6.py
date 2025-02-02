is_prime = lambda x: x>1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

input_numbers = input()

numbers = []
for num in input_numbers.split():
    numbers.append(int(num))

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers are: ", prime_numbers)