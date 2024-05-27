class Complex:
    # defining init method for class
    def __init__(self, r, i):
        self.real = r
        self.img = i

    # overloading the add operator using special function
    def __add__(self, sec):
        r = self.real + sec.real
        i = self.img + sec.img
        return complex(r,i)
        # overloading the less than operator using special function

    def __lt__(self, other):
        if self.real < other.real:
            return True
        elif self.real == other.real:
            if self.img < other.real:
                return True
            else:
                return False
        else:
            return False

        # string function to print object of Complex class



    # string function to print object of Complex class
    def __str__(self):
       # return str(self.real)+' + '+str(self.img)+'i'
        return str(self.real) + ' + ' + str(self.img) + 'i'

c1 = Complex(5,3)
c2 = Complex(6,4)
print("sum = ", c1+c2)
print("Is c1 less than c2: ",c1<c2)