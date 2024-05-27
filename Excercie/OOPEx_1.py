class Car:
    carcnt = 0
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        Car.carcnt+=1


    def InformCar(self):
         print(f"name is {self.name}, model is {self.model} and year is {self.year}")


    @staticmethod
    def printInf():
        #print("THis is a Car class")
        return Car.carcnt


c = Car("Maruti","K10","2010")
c.InformCar()

c1 = Car("Honda","Amaze","2002")
c1.InformCar()

c2 = Car("Honda","City","2008")
c2.InformCar()

print("Total objects created:", Car.carcnt)
carcnt = Car.printInf()
print(carcnt)
