from array import *
array1 = array('i',[10,20,30,40])
print(array1)

print(array1[1])

for x in array1:
    print(x)

array1.insert(3,60)
print(array1)

array1.remove(20)
print(array1)

print(array1.index(10))

array1[0] = 100

print(array1)