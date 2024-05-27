# multilevel inheritance
# Base class
class Family:
    def showFamily(self):
       return "This is our happy Family "

class Father(Family):
    def __init__(self, name):
        self.name = name
    def showFamily(self):
     #   print(super().showFamily())
        return f" My name is {self.name} " + super().showFamily()

class Mother(Family):
    def __init__(self, name):
        self.name = name
    def showFamily(self):
      #  print(super().showFamily())
        return f" My name is {self.name} " + super().showFamily()

class Child(Father,Mother):

    def __init__(self,name):
        self.name = name

    def showFamily(self):
        f = Father("Father")
        m = Mother("Mother")

        f.showFamily()
        m.showFamily()
        return print(f"My name is {self.name} " + f.showFamily() + m.showFamily())


child = Child("Indraneel")
child.showFamily()

