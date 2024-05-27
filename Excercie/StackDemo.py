maxsize = 10
stack = [100,200,300,400]


for i in range(0, maxsize-1):
     stack.append(i)
#     stack[i] = 'a'
 #    print(stack[i])

print(stack)

stack.pop(stack[maxsize-1])

print(stack)

