# This is a demo program
i = 10
j = 20
k = i + j
print("k=", k, end="\n\n\n\n")
print("value of i=", i, " and j=", j)

# Example of Arithmetic operators
a = 10
b = 20
c = 0
# p: int = 5

c = a + b
print("Line 1 - Value of c is ", c)

c = a - b
print("Line 2 - Value of c is ", c)

c = a * b
print("Line 3 - Value of c is ", c)

c = a / b
print("Line 4 - Value of c is ", c)

c = a % b
print("Line 5 - Value of c is ", c)

a = 4
b = 6
c = a**b
print("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b
print("Line 7 - Value of c is ", c)

# del p
# 12print("this is value of p ",p)

# reading the input from user

number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
name = input("Enter name ")

print("name: ", name, " and addition of two numbers is: ", (number1 + number2))

sum = eval(input("enter the expression:"))
# This is an in-built function available in python, which takes the strings as an input.
# The strings which we pass to it should, generally, be expressions.
# The eval() function takes the expression in the form of string and evaluates it and returns the result.
print(sum)


