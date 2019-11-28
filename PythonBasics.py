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
Learn by using,do google when necesary.
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

# String Indexes
selfish = 'mememe'
print(selfish[0])
print(selfish[1])
print(selfish[2])
# String Slicing
"""
[start:stop]
[start:stop:stepover]
[start:]
[:start]
[::1]
[-2]
[-1]
[::-1]
[::-2]
"""
print(selfish[0:4])
print(selfish[0:6:2])
print(selfish[4:])
print(selfish[:4])
print(selfish[::1])
print(selfish[::-1])
print(selfish[::2])
print(selfish[::-2])

# Immutability => cannot reassign part of a string
"""
Mystr = '012345678'
Mystr[0] = '8'
print(Mystr)
"""
#Built in Functions-Methods
"""
-see documentation and practice
-We just create or destroy strings ,
they cannot be changed or modified,
 they are immutable
"""
# Booleans
"""
-True/False
"""
name = "Tanweer"
is_cool = True
print(bool(1))
print(bool(0))

# Exercise-Type Conversion
"""
bool
int
float
str
list
tuple
set
dict
"""
name = 'Arefin Tanweer'
age = 25
relationship_status = 'single'
relationship_status = 'It\'s complicated'
print(relationship_status)
"""
birth_year = input("What year were you born?")
current_year = 2019
age = current_year - int(birth_year)
print(f"Your age is {age} ")
"""
# Developer Fundamentals -2
"""
-It's good to comment your code->but don't use unnecessary comment
-Your code should be self explainable without comment
-Use comment in complex situation
"""
# Exercise : Password Checker
"""
username = input("What is your username?")
password = input("What is your password?")
print(f"{username},Your password ,{password}, is {len(password)} letters long")

password_length = len(password)
hidden_password = '*' * password_length
print(f"{username},Your password ,{hidden_password}, is {password_length} letters long")
"""

"""
List:
-array/ordered sequence
-Data structure
-very very useful one
-extremly important 
"""
li1 = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']
li3 = [1, 'a', 2, 'b', 3, True]
amazon_cart = ['notebook', 'sunglasses']
print(amazon_cart[0])
print(amazon_cart[1])

# List-Slicing
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
print(amazon_cart[0:2])
print(amazon_cart[0::2])
"""
-list are mutable
-In list slicing everytime we slice a list we create a new copy of that list
-there is a difference between copying and modifying
"""
#new_cart = amazon_cart[:]
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# Matrix-2D list
matrix = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8],
]
print(matrix[0][1])

# List-methods - part 1

"""
len()
sorted()
--------
append()
insert()
extend()
pop()
remove()
clear()
index()
count()
sort()
reverse()
"""
basket = [1, 2, 3, 4, 5]
print(len(basket))

# list-adding
#new_list = basket.append(1000)
#new_list = basket.insert(4, 100)
new_list = basket.extend([101])
print(new_list)  # none
new_list = basket
print(new_list)  # normal

# removing
new_list = basket.pop()
new_list = basket
print(new_list)

new_list = basket.remove(5)  # remove value not index
new_list = basket
print(new_list)

# new_list = basket.clear()  # clears everything
#new_list = basket
# print(new_list)

# List methods - part 2
print(basket.index(2))

basket = ['a', 'b', 'c', 'd', 'e', 'd']
print('a' in basket)
print('x' in basket)

print(basket.count('d'))

# List methods - part 3
basket.sort()
print(basket)
print(sorted(basket))  # sorted modify + create a copy instatntly

basket.reverse()
print(basket)

# Common List Patterns
"""
-reverse a list -> [::-1]
-copy of a list -> [:]
-portion of a list -> [0:4]
-range(start,stop)
-.join() => for combining string and list
"""
print(list(range(1, 100)))
sentence = ' '
new_sentence = sentence.join(['hi', 'my', 'name', 'is', 'Tanweer'])
print(new_sentence)

# List Unpacking
a, b, c = [1, 2, 3]
print(a)
print(b)
print(c)

a, b, c, *other = [1, 2, 3, 4, 5, 6]
print(a)
print(b)
print(c)
print(*other)

# None
weapons = None
print(weapons)

# Dictionary
"""
-{}
-Unordered
-'Key':value pair
-Data Type + Data Structure
-Called as Hash Table/Map/Object
-Sort form : Dict
"""
dictionary = {
    'a': [1, 2, 3],
    'b': 'Hello',
    'x': True
}
print(dictionary)

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'Hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'Oh! Hello',
        'x': True
    }
]
print(my_list[0]['a'][2])

# Developer Fundamentals : Part -3
"""
-Understanding Ds
-A good programmer is able to understand when to use what Ds
-When to use List?
-When to use Dictionary?
"""
# Dictionary Keys
"""
-dictionary key needs to be immutable(ex : string)
-numbers,string,boolean,Tuple
-Normally we use string
-every key has to be unique
"""
# Dictionay Methods
"""
get()
dict()
keys()
values()
items() - return full dictionary in a tuple
clear()
copy()
pop()
update()
"""
user = {
    'basket': [1, 2, 3],
    'greet': 'hello'
}
print(user.get('age', 55))

user2 = dict(name='JhonJhon')
print(user2)

print('basket' in user.keys())
print('hello' in user.values())
print(user.items())

# Tuples
"""
-Data structure + Data Type
-()
-Immutable list
-are like list but immutable
-less flexible than list
"""
# Tuple methods
"""
count()-frequency
index()
len()
"""
my_tuple = (1, 2, 3, 4, 4, 5)
print(my_tuple.count(4))
print(my_tuple.index(4))
print(len(my_tuple))

# Sets
"""
-Datatype + Data Structure
-unordered collection of unique items,no duplicate items allowed
-{}
-DOES NOT SUPPORT INDEXING!
-set toi list and list to set conversion possible
"""
my_set = {1, 2, 3, 4, 5, 6}
my_set.add(100)
my_set.add(2)
print(my_set)
# print(my_set[0])  # error dibe
print(1 in my_set)

my_list = [10, 20, 30, 10, 10, 20, 30, 40]
no_duplicate = set(my_list)
print(no_duplicate)

# Set Methods
"""
.difference()
.difference_update()
.discard()
.union()
.intersection()
.issubset()
.issuperset()
.isdisjoint()
"""
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

print(my_set.difference(your_set))
# print(my_set.discard(5))
# print(my_set)
