class Stack:
    def __init__(self):
        self.stack=list()
        self.max_size=10
        self.top=0
    def push(self,ele):
        if self.top>=self.max_size:
            print("Stack is full")
            return
        else:
            self.stack.append(ele)
            self.top+=1
            print(ele,"added successfully!!!")

    def pop(self):
        if self.top<=0:
            print("Stack is empty")
            return
        else:
            ele=self.stack.pop()
            self.top-=1
            print(ele,"removed from stack")

    def peek(self):
        if self.top <= 0:
            print("Stack is empty")
        else:
            print(self.stack[-1])

    def size(self):
        return self.top

    def display(self):
        if self.top <= 0:
            print("Stack is empty")
        else:
            print("All elements of stack are:")
            for i in range(0,self.size()):
                print(self.stack[i])
s=Stack()
while True:
    print("1:Add element to stack\n2:Remove element from stack\n3:Get top element\n4:Current size of stack\n5:Display stack\n6:Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
         ele=input("Enter any element:")
         s.push(ele)
    elif ch==2:
         s.pop()
    elif ch==3:
         s.peek()
    elif ch==4:
         print("Current size of stack is:",s.size())
    elif ch==5:
         s.display()
    elif ch==6:
        break
    else:
        print("Error:Invalid choice try again!!!")
