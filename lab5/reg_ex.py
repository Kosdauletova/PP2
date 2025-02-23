#matches a string that has an 'a' followed by zero or more 'b''s

import re

string = input()
pattern = r'a*b*'
match = re.match(pattern,string)
print("Matched: ", bool(match))


#matches a string that has an 'a' followed by two to three 'b'

import re

string = input()
pattern = r'a[b]{2,3}'
match = re.fullmatch(pattern,string)
print("Matched: ", bool(match))



#find sequences of lowercase letters joined with a underscore

import re
string = input()
pattern = r'[a-z]+_[a-z]+'
matches = re.findall(pattern , string)
print("Matched: ", bool(matches))


#find the sequences of one upper case letter followed by lower case letters.

import re
string = input()
pattern = r'[A-Z][a-z]+'
matches = re.findall(pattern , string)
print("Matched: ", bool(matches))



#matches a string that has an 'a' followed by anything, ending in 'b'

import re
string = input()
pattern = r'a.*b'
#.*-после ф идет люое значение,но заканчивается на b
matches = re.findall(pattern , string)
print("Matched: ", bool(matches))



#replace all occurrences of space, comma, or dot with a colon.


import re
string = input()
new_string = re.sub(r'[ ,.]', ":" , string)
print(new_string)



#convert snake case string to camel case string.

import re

def snake_to_camel(snake_str):
    return re.sub(r'_(.)' , lambda x: x.group(1).upper() , snake_str)

snake_case_str = input()

camel_case_str = snake_to_camel(snake_case_str)

camel_case_str = camel_case_str[0].lower() + camel_case_str[1:]

print(camel_case_str)


#split a string at uppercase letters.

import re
string = input()

split_string = re.split(r'(?=[A-Z])', string)
print(split_string)


# insert spaces between words starting with capital letters.

import re
string = input()

new_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', string)
print(new_string)



#convert a given camel case string to snake case
import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([A-Z])' , r'_\1' , camel_str).lower()
    if snake_str[0] == '_':
        snake_str = snake_str[1:]
    return snake_str



camel_case_str = input()

snake_case_str = camel_to_snake(camel_case_str)

print(snake_case_str)
