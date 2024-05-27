class Employee :
  def __init__(anothername, name1, age1, id1, salary1):
  #def setval(self,name, age, id, salary):
        anothername.name = name1
        anothername.age = age1
        anothername.salary = salary1
        anothername.id = id1

  def printEmp(anothername):
        print("Employee Id : ", anothername.id)
        print("Employee Name : ",anothername.name)
        print("Employee Age : ", anothername.age)
        print("Employee Salary : ", anothername.salary)

EmpName = input("Enter the name of the employee ")
EmpId = int(input("Enter emp id "))
EmpAge = int(input("Enter the emp age "))
EmpSalary = float(input("Enter the salary of the emp "))

emp = Employee(EmpName,EmpAge,EmpId,EmpSalary)
#emp.setval(EmpName,EmpAge,EmpId,EmpSalary)
emp.printEmp()

#print("Employee.__doc__:", Employee.__doc__)
#print("Employee.__name__:", Employee.__name__)
#print("Employee.__module__:", Employee.__module__)
#print("Employee.__bases__:", Employee.__bases__)
#print("Employee.__dict__:", Employee.__dict__)

EmpName = input("Enter the name of the employee ")
EmpId = int(input("Enter emp id "))
EmpAge = int(input("Enter the emp age "))
EmpSalary = float(input("Enter the salary of the emp "))

emp1 = Employee(EmpName,EmpAge,EmpId,EmpSalary)
#emp1.setval(EmpName,EmpAge,EmpId,EmpSalary)
emp1.printEmp()

#del emp1

#emp1.printEmp()

class Person :
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def printPerson(self):
        print(self.name, self.id)
        emp1.printEmp()

p1 = Person('P1',23)
p1.printPerson()



