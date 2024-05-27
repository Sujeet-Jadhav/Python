class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printPerson(self):
        print(f"{self.name} is {self.age} years old")


class Student(Person):
    # pass
    def __init__(self, name, age, classname, rollno):
        self.classname = classname
        self.rollno = rollno
        # Person.__init__(self,name,age)
        super().__init__(name, age)

    def printStudent(self):
            super().printPerson()
            print(f"{self.name} studies in {self.classname} and roll number is  {self.rollno}")

stud = Student('Student1', 12, '5th', 35)
stud.printStudent()

stud1 = Student('Student2',13,'VIth', 22)
stud1.printStudent()
