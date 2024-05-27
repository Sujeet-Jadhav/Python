# This is just a demo
i = 10
j = 20
k = i + j \
    + 10     # this is the line continuation

print("value of K=", k, end="\n\n\n")
print("value of i=", i, " and j=", j)

a = "hello"
b = "goodbye"
cc = """ Well this is the example of
multiline string
which can be done in this way"""

print(a + " " + b)

i = "abc"
print(i, end="\n\n")
print(cc)


a=b=c=2
print(a,b,c, end="\n\n")

a,b,c = 4,5, "abcd"
print(a,b,c)

print(type(a))
print(type(i))
print(type(cc))

# python Lists
list = ['xyz', 456, 2.23, 'rama', 50.2 ]

otherlist = [123, 'rama']

print(list)          # Prints complete list
print(list[0])       # Prints first element of the list
print(list[1:3])     # Prints elements starting from 2nd till 3rd
print(list[2:])      # Prints elements starting from 3rd element
print(otherlist * 2)  # Prints list two times
print(list + otherlist)  # Prints concatenated lists

list[2] = 100

print(list)

# python Tuple

tuple = ('xyz', 456, 2.23, 'trama', 50.2 )

othertuple = (123, 'trama')

print(tuple)          # Prints complete list
print(tuple[0])       # Prints first element of the list
print(tuple[1:3])     # Prints elements starting from 2nd till 3rd
print(tuple[2:])      # Prints elements starting from 3rd element
print(othertuple * 2)  # Prints list two times
print(tuple + othertuple)  # Prints concatenated lists

 #tuple[2] = 102

# python dictionary
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

otherdict = {'name': 'rana', 'code': 400, 'department': 'support'}


print(dict['one']) # Prints value for 'one' key
print(dict[2]) # Prints value for 2 key
print(otherdict) # Prints complete dictionary
print(otherdict.keys()) # Prints all the keys
print(otherdict.values()) # Prints all the values

print('Python', end ='@')

#res = lambda str: (str == str[::-1])
#print(res('malayalam'))
print((lambda str: (str == str[::-1]))('malayalam'))

#print(result)
print(abs(-17.69))
