# High-level, Object-Oriented, Interpreted language, Dynamically-Typed and General-purpose

# inner working
# '''Source Code -> Byte Code -> Python Virtual Machine
# 1. Compile to byte code (.pyc)
# compiled python (frozen binaries)

# __pycache__ (python system folder)
# source change and python version
# works only for imported files
# not for top level files
# '''

#PVM
# '''Python virtual machine (Run time engine) 
# Code loop to iterate byte code
# also known as python interpreter

# Byte code is not machine code
# python specific interpretation
# cpython (standard implementation), jython (jpython), Iron Python, Stackless, PyPy 
#  '''

# # print statement
# print("Hello Python")

# # print multiple value
# i = 8
# print("*" * i)

# # Taking input
# name = input("Enter name:")
# print("hi "+ name)

# Data Types / Object Types
# '''
# There No data type for variable but for object data type are present which is assign to variable

# 1) Number 
# eg) 1234, 3.142, 3+4j, 0b111, Decimal(), Fraction()

# 2) String 
# eg) 'spam', "Bob's", b'a\x01c', u'sp\xc4m'

# 3) List
# eg) [1, [2, 'three'], 4.5], list(range(10))

# 4) Tuple
# eg) (1, 'spam', 4, 'U'), tuple('spam'), namedtuple

# 5) Dictionary
# eg) {'food': 'spam', 'taste': 'yum'}, dict(hours=10)

# 6) Set 
# eg)set('abc'), ('a', 'b', 'c'}

# 7) File
# eg) open('eggs.txt'), open (r'C:\ham.bin', 'wb')

# 8) Boolean
# eg) True, False

# 9) None
# eg) None

# 10) Funtions, modules, classes

# 11) Advance: Decorators, Generators, Iterators,
# MetaProgramming
# '''

# Internal Working - There is an ref_count to count the reference of the particular value
# eg a=10 b=10  a,b -> 10
# Number and String are not immediantly taken by garbage collector 

# import sys
# print(sys.getrefcount(24601))
# print(sys.getrefcount("hello"))

# list1 = [1,2,3]
# list2 = list1
# print("List1",list1)
# print("List2",list2)
# print("List1==List2",list1==list2)
# print("List1 is List3",list1 is list2) # same reference
# list1[0] = 45
# print("List2",list2) 
# list2[0] = 33
# print("List1",list1)
# # as both the list are pointing to same reference so change in one list may affect the other
# to avoid this use
# import copy
# list1 = [1,2,3,[4,5]]
# list2 = copy.copy(list1)
# print(list1)
# list3 = copy.deepcopy(list1)
# print(list3)
# print("List1==List3",list1==list3)
# print("List1 is List3",list1 is list3) # different reference

# # Number
# Boolean value is treated as number internally 
# print(True==1)
# print(False==0)
# print(True is 1)
# print(False is 0)
# print(True+4)

# import math
# # print(math.ceil(3))
# # floor() closes value below number
# print(math.floor(10.5))
# print(math.floor(-10.5))
# # trunc() towards zero
# print(math.trunc(2.8)) 
# print(math.trunc(-2.8)) 
# print(math.factorial(5))
# # Octal Number 0o (zero o)
# print(0o20)
# print(oct(64))
# # Hex Number 0x (zero x)
# print(0xF)
# print(hex(64))
# # Binary Number 0b (zero b)
# print(0b1000)
# print(bin(64))
# # using int() to convert 
# print(int('64'))
# print(int('64',8))
# print(int('64',16))
# print(int('1000',2))

# # known problems with solution
# from decimal import Decimal
# print(0.1+0.1+0.1)
# print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1'))

# from fractions import Fraction
# fra = Fraction(2,7)
# print(fra)

# # Type conversion int()
# birth_year = int(input("Enter Birth Year:"))
# age = 2023 - birth_year
# print("Age:",age)

# # String
# course = ''' Multi line String
# Using triple quotes
#
# Thank You
# '''
# print(course)
course = 'This is "Python" Language  '
# print(course[0])  # first letter (positive)
# print(course[-1])  # last letter (negative)
# print(course[0:5])  # print from 0 to 5
# print(course[0:])  # print from 0 to last
# print(course[:5])  # print from first to 5
# print(course[:])  # print whole string
# print(course[1:-1])  # print whole string excluding first and last char
# print(course[:17:2]) # print from 0 to 16 (17 excluting) giving step of 2
# msg = f'{course} using formatted string' # Formatted String f'{}'
# print(msg)
# print(len(msg))  # calculate length
# print(course.upper())  # Convert in upper case
# print(course.lower())  # Convert in lower case
# print(course.strip()) # remove unwanted spaces
# print(course.find("s"))  # Find letter First occurrence
# print(course.find("Python"))  # Find word First occurrence
# print(course.replace("is","was"))  # replace string
# print('Python' in course)  # Check string
# print(course.split(" ")) # convert to list
# print(course.count("is")) # count the occurrence
# print("is" in course) # check string in variable (True or False)
# order = "I ordered {} cups of {}"
# print(order)
# quantity = 2
# type = "coffee"
# print(order.format(quantity,type)) # add variable value to {}
# type=["Coffee","Tea","Water"]
# print(" - ".join(type))
# path=r"C:\user\admin" # to ignore unicode characters 
# print(path)
# for letter in course:
#     print(letter)

# # Operators
# print(10 // 3)  # floor division (int)
# print(10 / 3)  # division (float)
# print(10 ** 3)  # exponent
# print(10 % 3)  # mod
#
# print(round(10.823))  # round off
# print(abs(-23.45))  # absolute value (positive)


# # if statements
# age = 58
# if age<18:
#     print("Can not drive")
# elif age<40:
#     print("Can drive")
# else:
#     print("Can drive but be careful")

# # Logical operators
#
# t=True
# f=False
#
# if t and f:  # both true
#     print("and")
#
# if t or f:  # any one true
#     print("or")
#
# if not f:  # invert
#     print("not")

# # while loop
# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
# else:
#     print("Done")
#
# # for loop
# for i in "Python":
#     print(i)


# # range(start,end,steps)
# for i in range(5,51,5):
#     print(i)


# # List '[]' mutable
l: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l[0]) # access element using index
print(l[:6:2]) # using slicing
i=["I","study","lang"]
i[1:2]="Python" # insert char one by one
print(i)
i[1:2]=["Python"] # insert element

# for i in l:
#     print(i)
#
# letter = [5,1,5,1,5]
# for i in letter:
#     output = ''
#     for j in range(i):
#         output+='*'
#     print(output)

# list1 = [1,2,3]
# list2 = list1
# print("List1",list1)
# list1[0] = 45
# print("List2",list2) 
# list2[0] = 33
# print("List1",list1)
# as both the list are pointing to same reference so change in one list may affect the other
# to avoid this use slicing [:]

# # largest no of list
# num = [25,3,7,8,12,1,9,4]
# max = num[0]
# for i in num:
#     if i > max:
#         max = i
# print(max)
#
#
# names = ['John','Bob','Mosh','Santa','Fadrit']
# print("First name in list: "+names[0])
# print("Last name in list: "+names[-1])
# print(names[2:])
# print(names[:4])
# print(names[2:5])

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# print(matrix[1][0])
#
# for row in matrix:
#     print(row)
#     for i in row:
#         print(i)


# # List operations
# num = [25, 3, 7, 8, 12, 1, 9, 4, 12]
# print("Original List:",num)
# num.insert(2,10)  # add element at index position
# print(num)
# num.remove(25)  # remove element
# print(num)
# num.append(10)  # add element at last position
# print(num)
# num.pop()  # remove last element
# print(num)
# print(num.index(1))   # return index of element
# print(50 in num)   # check the element in list
# print(num.count(12))  # count no of element specified
# num.sort()
# print(num)
# num.reverse()
# print(num)
# num1=num.copy()
# print(num1)
# num.clear()  # remove all elements
# print(num)

# num = [5, 3, 7, 5, 12, 12, 9, 4, 12]
# num1 = []
#
# for i in num:
#     if i not in num1:
#         num1.append(i)
# print(num1)


# # Tuples '()' immutable
# num = (1,2,3,4,2,5)
# # print(num.index(4))
# # print(num.count(2))
# tup1 = (10,20,30)
# num +=tup1  # add tuple/list in another tuple
# print(num)

# # Unpacking
# coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
# # instead we can write
# x,y,z = coordinates
# print(x,y,z)
#
# coordinates = [1,2,3]
# a,b,c=coordinates
# print(a,b,c)

# # dictionary (key,value) pairs
# dict = {
#     "name":"John",
#     "age":30,
#     "verified":True,
#     "Id": 100
# }
# print(dict["name"])
# dict["BOD"] = "1 April 2011"  # add new key,value pair
# # get(key,defaultValue) - does give None value if key is not present or print default value
# print(dict.get("Date",15))
# print(dict)

# # sets are mutable, unordered collections of unique elements
# my_set = {1, 2, 3}
# print(my_set)
# my_set.add(4)  # add element
# print(my_set)
# my_set.remove(1)  # raising an error if not present
# print(my_set)
# my_set.discard(5)  # not raising an error if not present
# print(my_set)
# set1 = {10,20,30}
# my_set =set1 | my_set  # union
# print(my_set)
# my_set.update({4, 5, 6})
# print(my_set)

# # split() - return converted string to list of words
# msg = input(">")
# words=msg.split(' ')
# print(words)

# # functions
# def hello(exp):
#     print(f"Hello Python {exp}")
#
#
# hello("!!!")
# hello("...")
#
# def user(first,last):
#     print(f"Hi {first} {last}")
#     return 10
#
#
# id=user(last="Smith",first="John")
# print(id)

# # default value to parameters
# def name(first="ABC",last="XYZ"):
#     print(first,last)
#
# name()
# name("OM")
# name("OM","Sai")
# name(last="Sai")

# # exceptions
# try:
#     age=int(input("Age="))
#     id = 100/age
#     print(age)
# except ZeroDivisionError:
#     print("Age cannot be zero")
# except ValueError:
#     print("Invalid value")

# # Classes
# class Point:
#     # self - reference to current object
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# # Object
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.y)
# point1.draw()
#
# point2 = Point()
# point2.y = 0
# print(point2.y)
# point2.move()
#
#
# # Constructor __init__
# class Pointer:
#     name = "ABC"
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def give(self, name):
#         self.name = name
#         print(self.name)
#
#
# p = Pointer(5, 6)
# print(p.x, p.y)
# p.give("Om")


# # Inheritance
# class Pet:
#     def walk(self):
#         print("Walk")
#
#
# class Animal(Pet):
#     pass  # does not do anything
#
#
# p = Pet()
# p.walk()
# a = Animal()
# a.walk()

# # Module - collection of files
# import converters
# import converters as c
# from converters import kg_to_lbs
#
# print(kg_to_lbs(100))
# print(converters.lbs_to_kg(100))
# print(c.kg_to_lbs(45))

# # Packages - container for multiple modules
# import ecommerce.shipping
# from ecommerce.shipping import cal_ship
# from ecommerce import shipping
# shipping.cal_ship()
# cal_ship()
# ecommerce.shipping.cal_ship()

# # built-in modules
# import random
# print(random.randint(1,100))
# no = [10,20,50,30,40]
# print(random.choice(no))
# print(random.shuffle(no))
# for i in range(5):
#     print(random.random())
#     print(random.randint(10,20))
#
# member = ['John',"Mary",'Bob',"Mosh",'Prime',"Yong"]
# leader = random.choice(member)
# print(leader)

# # rolling two dice
# import random as r
#
#
# class Dices:
#     dice = (1, 2, 3, 4, 5, 6)
#
#     def roll(self):
#         return r.choice(self.dice), r.choice(self.dice)
#
#
# dice = Dices()
# print(dice.roll())

# # Files and Directories
# # Absolute path - path from root to file
# # Relative path - path from current folder to file
# from pathlib import Path
# path = Path("ecommerce")
# print(path.exists())
# path.mkdir()  # create directory
# path.rmdir()  # remove directory
# for file in path.glob('*.py'):  # files in current directory
#     print(file)
#
# path = Path()
# for file in path.glob('*.*'):  # files in current directory
#     print(file)

# Regular expression
# .: Matches any character except a newline.
# *: Matches 0 or more occurrences of the preceding character.
# +: Matches 1 or more occurrences of the preceding character.
# ?: Matches 0 or 1 occurrence of the preceding character.
# []: Specifies a character class.
# ^: Matches the start of a string.
# $: Matches the end of a string.
#
# import re
#
# pattern = r"\b\w+\b"  # Matches words
# text = "This is a sample sentence."
#
# matches = re.findall(pattern, text)
#
# print(matches)
#
# import re
#
# pattern = r"\d+"  # Matches one or more digits
# text = "There are 123 apples and 456 oranges."
#
# modified_text = re.sub(pattern, "X", text)
#
# print(modified_text)
#
#
# import re
#
# pattern = r"\b[A-Za-z]+\b"  # Matches whole words
# text = "123 apples and oranges."
#
# matches = re.findall(pattern, text)
#
# print(matches)


# # files
# # Opening a file in read mode
# file = open("example.txt", "r")

# # Opening a file in write mode
# file1 = open("example.txt", "w")

# # Opening a file in append mode
# file2 = open("example.txt", "a")

# # Reading the entire content of a file
# content = file.read()

# # Reading a single line from the file
# line = file.readline()

# # Reading all lines into a list
# lines = file.readlines()

# # Writing a single line to a file
# file.write("This is a new line.\n")

# # Writing multiple lines to a file
# lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
# file.writelines(lines)

# # check if a file exists before performing operations on it
# import os
# print(os.getcwd) #current working directory
# file_path = "example.txt"

# if os.path.exists(file_path):
#     with open(file_path, "r") as file:
#         content = file.read()
# else:
#     print(f"The file {file_path} does not exist.")

# import sys 
# print(sys.platform)

# Reload the module and return it.
# from importlib import reload
# reload(math_operation)

# # import other python file
# from math_operation import sub
# print(sub(10,20))
# import math_operation
# print(math_operation.add(10,20))
# print(math_operation.PI)