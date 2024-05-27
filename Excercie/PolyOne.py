class Vehicle:
    def capacity(self,capacity):
        self.capacity = capacity
class Bus(Vehicle):
    def buscapacity(self,n):
        self.n = n
class SBus(Bus):
    def print(self):
        pass
b1 = SBus()
print(b1)

b2 = issubclass(SBus,Bus)
if b2 == True :
    print("Its a subclass")


