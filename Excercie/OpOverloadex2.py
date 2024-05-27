class Complex:
    def __init__(self,r,i):
        self.real = r
        self.img = i
    def __lt__(self, other):
        if self.real < other.real :
            return True
        elif self.real == other.real:
            if self.img < other.real:
                return True
            else:
                return False
        else:
            return False
    def __str__(self):
       # return str(self.real)+' + '+str(self.img)+'i'
        return str(self.real) + ' + ' + str(self.img) + 'i'
c1 = Complex(5,5)
c2 = Complex(5,4)
print("is c1 less than c2: ",c1<c2)
