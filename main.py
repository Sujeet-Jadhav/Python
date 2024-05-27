# a = float(input("enter the temp in fahrenheit: "))
# print(type(a))

# c = 5 / 9 * (a - 32)
# print("temperature in celcius: ", c)
# print(type(c))


'''i = 20
while i == 20:
    print(i)
    i += 1'''

'''n = int(input("Enter the number:"))
fact = 1
i = 2
while i <= n:
    fact = fact * i
    i = i + 1
print("Factorial is: ", fact)

a = int(input("Enter the number for fibonacci:"))
n1 = 1
n2 = 1
i = 3
while i <= a:
    i = i + 1
    temp = n2
    n2 = n2 + n1
    n1 = temp
print("fibonacci series of given number:", n2)

b = int(input("Enter the number:"))
i = 2
flag = 1
while i < b // 2:
    if (b % i) == 0:
        flag = 0
        break

if flag == 1:
    print("number is prime")
else:
    print("number is not prime") 

n = int(input("Enter the number:"))
#n=1
while n<=5:
    print("less than 5")
    #n=n+1
else:
    print("greater than 5")

for i in range(5):
    print("numbers:",i)

for i in range(30,0, -3):
    print("numbers :", i)
# 12345678
a = "rajratna"
b = "bhalerao"
for i in a:
    print(i)
print(a + b)

s = input("enter the string:")
t = s[-1::-1]
if s==t:
    print("palindrome",t)
else:
    print("not palindrome:")

cnt = 0
i = 10
i = 1 + i
print(i)


ans = eval(input("Enter the operation: "))
print(ans)

A="Save Earth"
print(A[1:3])
print(A[3:])
print(A[:3])
print(A[:])
print(A[-2:])
print(A[:-2])

A = "pineapple"
cnt = 0
for ch in A:
    if ch == 'p':
        cnt += 1
        print(ch,end=" ")
        
print(cnt)'''


# b = int(input("Enter the number:"))
# a = int(input("Enter the number:"))
# c = int(input("Enter the number:"))
# if b > a and b > c:
#     print(b, " maximum number")
# elif a > c:
#     print(a, "maximum number")
# else:
#     print(c, "maximum number")
# help(str)
# a = "ThisIsmycountry"
# b = "ThisIsmycountry"
# if a == b:
#     print("yes")

# l1 = [10, 20, 30, 56]
# l2 = [10, 20, 30, 56]
#
#
# # l.insert(1,99)
# def add(*l):
#     ans = 0
#     for data in l:
#         ans += sum(data)
#     return ans
#
#
# print(add(l1, l2))


# def my():
#     n1=int(input("Enter the number"))
#     n2=int(input("Enter the second number"))
#     sum=n1+n2
#     print(sum)
# my()

# l.append([69,88,])
# print(l)
# l.extend(l)
# print(l)
def caeser_encryption(Str, n):
    encry = ""

    for ch in Str:
        encry += (chr(ord(ch) + n))
    return encry


def caeser_decryption(Str, n):
    decry = ""

    for ch in Str:
        decry += (chr(ord(ch) - n))
    return decry


Str = input("Enter the String: ")
n = int(input("Enter the increment count:"))

Str = caeser_encryption(Str, n)

print("After Encryption String is:", Str)

Str = caeser_decryption(Str, n)

print("After Decryption string is:", Str)
