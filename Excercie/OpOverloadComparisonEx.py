# program to compare the scores of two students

class Student :
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, m1,m2):
        m1 = self.m1 + m1
        m2 =  self.m2 + m2
        s3 = student(m1,m2)
    def __gt__(self, other):
        p1 = self.m1 + self.m2
        p2 = other.m1 + other.m2
        return True if(p1>p2) else False
s1 = Student(70,80)
s2 = Student(80,90)
if (s1>s2) :
    print("s1 has more scores")
else:
    print("s2 has more scores")


