# while statement

i = int(input("enter the value of i: "))
x = int(input("enter the value of x: "))
# print the mathematical power of x raise to i
while i <= 10:
  print(x, "^", i, " = ",  x**i)
  i += 1


i=1
sum = 0
while(i<=30) :
    sum = sum + i
    i += 1
print(" sum is : ", sum)

add=0

# range() returns a sequence of numbers and is immutable (whose value is fixed).
# The range function takes one or at most three arguments, namely the start and a stop value along with a step size.
# range() function can only work when the specified value is an integer or a whole number.
# It does not support the float data type and the string data type.

for num in range(1,31):
     add+=num
print("Addition is :",add)


