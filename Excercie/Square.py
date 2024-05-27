class Calculate:
    def __init__(self,n):
        self.n = n

    def square(self,n):
        return self.n * self.n

    def cube(self,n):
        return self.n * self.n * self.n
n= int(input("Enter a number"))

obj = Calculate(n)
sq = obj.square(n)
cu = obj.cube(n)

print("Square is:",sq)
print("Cube is :",cu)

