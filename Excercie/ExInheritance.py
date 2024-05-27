class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def printperson(self):
        print(f" the person {self.id} and {self.name} are these")

class Student(Person):          # Student will behave exactly similar to Person class
    pass

s = Student(1,'aaa')
s.printperson()

class Student1(Person):       # Student will have its own initializer
    def __init__(self,id,name,studclass,studrollno):
        self.studclass = studclass
        self.studrollno = studrollno
        Person.__init__(self,id,name)
    def printStud(self):
        super().printperson()
        print(f" the student's class {self.studclass} and roll no  {self.studrollno} are these")

s1 = Student1(22,'StudentAAA','5th',144)
#s1.printperson()   # calls the parent method with current instance parameters
s1.printStud()

class Student2(Person):
    def __init__(self):
        super().__init__(100, 'SuperAAA')
    def printChild(self):
        print(f" the person {self.id} and {self.name} are these")

s3 = Student2()
s3.printChild()

print('Id of s3 before = ',id(s3))

s3 = s
print(f"In the child class now {s3.id} and {s3.name}")

print('Id of s = ',id(s))

print('Id of s1 = ',id(s1))

print('Id of s3 = ',id(s3))

class stud(Student):
    def __init__(self):
        super().__init__(100,'Super')
s2 = stud()
s2.printperson()

