# Data Types-int, float, bool, str, list, tuple, set, dict

# Custom Types-class

# Specialized Data Types-Packages and Modules

# None

#int and float
# print(2+4)
# print(2-4)
# print(2*4)
# print(type(2/4))
# print(type(5.000))

# print(2 ** 3)
# print(5 // 4)
# print(10 % 4)

# Math Functions
print(round(3.1))
print(round(3.9))
print(abs(-20))

# Developer Fundamentals
"""
Don't read the dictionary : Don't learn every function,syntax!
Don't memorize every single things!
Learn by using.
"""

# Operator precedence
print(20 + 12 * 3)
"""
1.()
2.**
3.* and /
4.+ and -
"""
# Decimal to binary and binary to decimal
print(bin(5))
print(int('0b101', 2))

# variables - Ways to store data
Iq = 190
print(Iq)
a, b, c = 10, 20, 30
print(b)
"""
snake_case
start with lowercase or _
letter,numbers,underscore
Case sensitive
don't overwrite keywords
"""

# constants
PI = 3.1415
print(PI)

# __ (Dunder variables)

# Expression Vs Statements
"""
statement : user_age = iq/5
Expression : iq/5
"""
# Augmented Assignment Operator
i = 2
i += 2
i -= 2
i *= 2
print(i)

# Strings (str) : A piece of Text
print(type("Hi there"))
print('hello there!')

username = 'admin'
password = "admin"
print(username)
print(password)

long_string = ''' Wow
0 0 
----
'''
print(long_string)

first_name = 'Arefin'
last_name = 'Tanweer'
full_name = first_name + ' ' + last_name  # concatanation

print(full_name)

# Type Conversion
print(type(int(str(100))))

a = str(100)
b = int(a)
c = type(b)
print(c)

# Escape Sequence
weather = "it\'s sunny\"kind of"
print(weather)
print("My name is \t arefin")
print("My name is \n Tanweer")

# Formatted Strings
name = "Tanweer"
age = 24

print('hi ' + name + ' You are ' + str(age) + ' Years old')

print(f"hi {name} you are {age} years old")
