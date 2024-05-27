# This is the demo for control flow statements in python
# if statement
i = int(input("enter the value of i : "))
if i == 10:
    print("value of i:", i)
else:
    i += 1
    print("now value is : ", i)

# if-else-if statement
j = int(input("enter the value of j : "))
if (j < 4):
    print("j less than four")
elif (j > 4 and j < 10):
    print("value of j is :",j)
else:
    print("j not in range")

# PASS statement demo
num = [10, 20, 30,400, 500, 600]
for i in num:
   if i<100:
       #print("pass statement executed")
       pass
else:
   print("Give these numbers to the students: ",i)
