class Student:

    def __init__(self):
        self.__name=''
  #  def setname(self, name):
   #     print('setname() called')
    #    self.__name=name
  #  def getname(self):
   #     print('getname() called')
  #      return self.__name

    @property
    def getname(self):
        return self.__name

    #name=property(getname, setname)
    #def printname(self):


s1 = Student()
s1.name = 'Anjali'
print(s1.name)
s1.name="Aparna"
print(s1.name)
#print(property(s1.name))



