# using the range function
# It returns a sequence of numbers and is immutable (whose value is fixed).
# The range function takes one or at most three arguments, namely the start and a stop value along with a step size.
# range() function can only work when the specified value is an integer or a whole number.
# It does not support the float data type and the string data type.


for i in range(1,10,2):
    print("i = ", i)

# printing elements of a list
list1 = [10,20,'abc',123.34]
for x in list1:
    print(x)

# printing characters in a string
string1 = "This is the example"
for ch in string1:
    print(ch)

#print(string1[:5:2])

# adding the elements of a tuple
tuple1 = (10,20,30,40)
sum=0
for t in tuple1:
    sum = sum + t
print("summation of the tuple is : ",sum)

# example for nested loops
rows = range(1, 10)
for x in rows:
   for star in range(1, x+1):
       print('* ', end=' ')
   print()

listnew = [10, 12, 14, 15]
print(listnew)
#x = listnew
y = int(input("enter the element to search :"))
for x in listnew:
    if y != x:
        continue
    elif y==x:
        print(" y is in list")
    break
else:
    print("out of list")

num = [10, 20, 30,400, 500, 600]
for i in num:
   if i<100:
       print("pass statement executed")
       pass
else:
   print("Give these numbers to the students: ",i)


