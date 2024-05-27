s1="abc"
s2="This is the example of a new string"
s3='''This is the example
of a multiline string.
 This is very simple
 to understand'''
s4='this is another string'

print("string s1 = ",s1)
print("string s2 = ",s2)
print("string s3 = ",s3)
print("string s4 = ",s4)
print("This is the substring of s4 = ",s4[3:-2])

print("This is the substring of s3 = ",s3[2:8])
print("This is the substring of s1 = ",s1[1:2])
print("This is the substring of s4 = ",s4[1:10:2])
print("Length of string s3 = ",len(s3))

# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)

# Writing two string literals together also concatenates them like + operator.
string1 = "Hello" "Everyone"
print("String1 = ",string1)

string2 = ("Hello" 
           "Everyone")
print("String2 = ",string2)

# Iterating through a string
count = 0
for lt in 'Hello World':
    if(lt == 'l'):
        count += 1
print(count,'letter found')

for ch in "Hello Class":
    print("Character is : ",ch)

# The enumerate() function returns an enumerate object.
# It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
#
# Similarly, len() returns the length (number of characters) of the string.

string2 = 'It is very warm'

# enumerate()
list_enumerate = list(enumerate(string2))
print('list(enumerate(string2) = ', list_enumerate)

#character count
print('len(string2) = ', len(string2))

if("was" not in "This is in the Sea"):
    print("not present")

print("THis is the string example \"single quote\" lets check")


print(s1.upper())
s5 = "  THIS IS THE CAPITALIZED STATEMENT  "
print(s5.lower())

print(s5.strip())   # removes whitespaces from beginning or end

print(s5.replace('T', 'G'))     # replaces the character in the string

print(s5.replace('THIS', 'To'))  # replaces a word in the string

print(s5.split(' '))

print('Value of character c  is : ', ord('c'))

print('Character Value of integer 99  is : ', chr(99))


s6 = 'this is a python example'
print(s6.capitalize())

s7 = 'This has to be the beginning of the chapter'
print(s7.replace('the beginning', 'the end'))


# printing string with %
#Unfortunately, this kind of formatting isnât great because it is verbose and leads to errors,
# like not displaying tuples or dictionaries correctly
name = "sunil"
title = "Mr."
print("hello %s . Is your name %s ?" % (title, name))

# Python string format() method

# default(implicit) order
default_order = "{}, {} and {}".format('Ram','Shyam','Radha')
print('\n--- Default Order ---')
print(default_order)

# order using positional argument
positional_order = "{1}, {0} and {2}".format('Ram','Shyam','Radha')
print('\n--- Positinal Order ---')
print(positional_order)

# order using keyword argument
keyword_order = "{rad}, {s} and {r}".format(r='Ram',s='Shyam',rad='Radha')
print('\n--- Keyword Order ---')
print(keyword_order)


# str.format() is an improvement on %-formatting. It uses normal function call syntax
print("hello {} . Is your name {} ?" .format(title, name))

# You can reference variables in any order by referencing their index:

print("hello {1} . Is your name {0} ?" .format(name,title))
# Code using str.format() is much more easily readable than
# code using %-formatting, but str.format() can still be quite verbose
# when you are dealing with multiple parameters and longer strings.

# f-strings are string literals that have an f at the beginning and curly braces
# containing expressions that will be replaced with their values. This is less verbose.

# formatted strings

n1=int(input("enter first number :"))
n2 = int(input("enter the second number"))
addition = n1 + n2
#print(f'the addition of {n1} and {n2} is {addition}')

formatstring = f'the addition of {n1} and {n2} is {addition}'
print(formatstring)

print(f'{s2.upper()} is the capitalized string')

# raw string if the backslash character is not to be treated specially
raw_str = r" This is one/ slash and these are // slashes"
print(raw_str)

print('abcefd'.replace('ce', '12'))
#def f(value, values):
#    global t
  #  t = 1
    #values[0] = 44
   # values=[44,2,3]
    #print(id(values))
#t = 3
#v = [1, 2, 3]
#f(t, v)
#print(t, v[0])
#print(v)
#print(id(v))

print(s7.startswith("This"))
print(s1.join(s2))
