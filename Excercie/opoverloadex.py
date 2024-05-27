# program to compare scores and overload the gt operator
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, m1,m2):
        m1 = self.m1 + m1
        m2 = self.m2 + m2
        s3 = Student(m1,m2)
        return s3
    def __gt__(self, other):
        res1 = self.m1 + self.m2
        res2 = other.m1 + other.m2
        return True if(res1>res2) else False

s1 = Student(70,80)
s2 = Student(70,85)


if(s1>s2):
  print("s1 scores more than s2")
else:
  print("s2 scores more than s1")

