def simpleadd(x, y):
    sum = x + y
    return sum

# this is the function demo
x, y = 10, 20
print(f'Sum ={simpleadd(x, y)}')

# All parameters (arguments) in the Python language are passed by reference.
# It means if you change what a parameter refers to within a function, the change also reflects back in the calling function.

def changeval(mylist):
    print("the passed list is : ", mylist)

    mylist=[10, 20, 30, 40]
    # change  the value of this list
    print("the changed list is : ", mylist)
    print(id(mylist))    #id funtion is used to show the memory location where the variable points
    mylist.append(['a', 'b', 'c'])
    return mylist

# now assign the value to mylist and call the function
mylist = [1, 2, 3, 4]

print(f'Values out of the function : {changeval(mylist)}')
print(id(mylist))

print('out of the function :',  mylist)

#The parameter mylist is local to the function changeval. Changing mylist within the function does not affect mylist.

# default arguments

def printinfo(name, age=30) :
    print(f"name is {name} and age is {age} ")

printinfo("First", 40)
printinfo("Second")

# Arbitrary arguments ( when number of parameters are not known)
def arbarg(**name):
    """This is the demo for arbitrary arguments with **. This considers the arguments as key-value pair"""
    print('first name :' +name['fname'] + 'and last name : '+ name['lname'])

arbarg(fname='Anjali', lname='naik')

def arbarg1(*name):
    """This is the demo for arbitrary arguments with a *. This considers the arguments as tuples"""
    print('names of the children are : ', name)


arbarg1('abc','ccc','ddd')

#keyword arguments

def childname(child2,child3,child1):
    print('the names of the children are :', child1,child2,child3)

childname(child3='three',child2='two',child1='one')



# list parameter

def listparam(mylist):
    print(mylist)
    sum = 0
    for i in mylist:
        sum+=int(i)
    print("sum is :", sum)

mylist = [10,20,30,40]
listparam(mylist)

# example of kwargs
def f(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key,val in kwargs.items():
        print(key, '->' , val)

f(fname ="Sachin", mname ="R.", lname ="Tendulkar")

x , y = 10, 20

def globallocaldemo():
    global x
    y = 45
    x +=20
    print(x,y)

globallocaldemo()
print(f'x={x} ,y={y}')

# examples of lambda functions:



print((lambda x: x+1)(4))

num1 = -13
num2 = -12.45

print("Abs of num1 : ",(abs(num1)))
print("Abs of num2 : ",(abs(num2)))