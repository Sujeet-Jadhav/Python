class Employee1 :
  def __init__(self, name, age, id, salary):
  #def setval(self,name, age, id, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.id = id

  def printEmp(self):
        print("Employee Id : ", self.id)
        print("Employee Name : ",self.name)
        print("Employee Age : ", self.age)
        print("Employee Salary : ", self.salary)
Emplist = []
i=0

while(i<3):
    EmpName = input("Enter the name of the employee ")
    EmpId = int(input("Enter emp id "))
    EmpAge = int(input("Enter the emp age "))
    EmpSalary = float(input("Enter the salary of the emp "))
    emp = Employee1(EmpName,EmpAge,EmpId,EmpSalary)
    Emplist.append(emp)
    i+=1
    print('appended')


#emp.setval(EmpName,EmpAge,EmpId,EmpSalary)

for x in Emplist:
    print(x.printEmp())

