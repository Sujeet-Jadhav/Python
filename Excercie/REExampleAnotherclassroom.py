import re
str = " This is to inform all students regarding the scholarship information"

reg = re.finditer("inform",str)
for i in reg:
    extuple = i.span()
    print(extuple)


stringex = "Clap, Slap, Lap, Map, Tap, Sleep, Keep"
res = re.findall('[A-Z][a-z]*p',stringex)
print(res)

str1 = """
This is a 
very beautiful
place to stay for 
a week
"""

print(str1)
regex = re.compile("\n")
str1 = regex.sub(" ",str1)
print(str1)

if re.search("\w{2,20}\s\w{2,20}","Sachin Tendulkar"):
    print("Valid name")

grade1 = 80
grade2 = 90
average = (grade1 + grade2) / 2
print(average)


names1 = ['Amir', 'Bala', 'Charlie']
names2 = [name.lower() for name in names1]
print(names2[2][0])

try:
   f = open("testfile", "r")
   f.write("This is the test file for exception handling!!")
except IOError:
   print ("Error: could not find a file or read data")
else:
   print ("content is written in the file successfully")

