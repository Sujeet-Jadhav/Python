class First:
    def __init__(self,text):
        self.text = text
        print("First "+text)
    def add(self,x,y):
        return x + y


class Second:
    def __init__(self,text):
        self.text = text
        print("Second "+text)

    def add(self, p,q):
        addnum = p + q
        return addnum


class Third(First,Second):        # Method Resolution Order (MRO)
    def __init__(self):
        super().__init__("In Super class")
        print("In Third")

tt = Third()
result=tt.add(12,13)
print("Result is ",result)
print("MRO : ",Third.mro())