#multiply all the numbers in a list
import math

def multiply_list(num):
    return math.prod(num)


num = list(map(int, input().split()))
result = multiply_list(num)
print(f"The product of the numbers is: {result}")


#Calculate the num of upper case and lower case
def count_case(string):
    upper_case = sum(1 for c in string if c.isupper())
    lower_case = sum(1 for c in string if c.islower())
    return upper_case, lower_case


string = input()
upper, lower = count_case(string)
print(f"Upper case letters : {upper}, Lower case letters : {lower}")


#palindrome or not
def is_palindrome(string):
    return string == string[::-1]

string = input()
result = is_palindrome(string)
print(f"Is it palindrome? {result}")


#square root 
import time
import math

def square_root_after_delay(number, delay_ms):
    time.sleep(delay_ms / 1000)  
    return math.sqrt(number)

# Ввод от пользователя
number = float(input())
delay_ms = int(input())

result = square_root_after_delay(number, delay_ms)
print(f"Square root of {number} after {delay_ms} miliseconds is: {result}")


#true if all elements  of the tuple are true
def all_true(tup):
    return all(tup)

tup = tuple(map(int, input().split()))
result = all_true(tup)
print(f"Are all elements in the tuple true? {result}")
