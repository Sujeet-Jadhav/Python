class Parent:
    def func1(self):
        print("this is function one")

class Child(Parent):
    def func2(self):
        print("this is function 2")


class Child1(Parent):
    def func3(self):
        print(" this is function 3")


class Child2(Parent, Child1):
    def func4(self):
        print(" this is function 4")


chd = Child2()
chd.func1()