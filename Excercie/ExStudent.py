class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printPerson(self):
        print(self.fname,self.lname)
class Student(Person):
    def __init__(self,fname,lname,gradyear):
        super().__init__(fname,lname)
        self.gradyear = gradyear
    def printStudent(self):
        print(self.fname,self.lname,self.gradyear)

stud = Student('Kshitija','Joshi',2010)
stud.printStudent()
