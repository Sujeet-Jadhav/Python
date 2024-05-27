import os
import shutil   #shutil module offers a number of
# high-level operations on files and collections of files.
import re   # regular expressions
from distutils.dir_util import copy_tree

# Read the file
f = open("demotext.txt", 'r')
c = f.read()
print('File : ',c)
#if c is None:
 #   print('Reached end of the file')
f.close()

with open('demotext.txt', 'r') as fr:
    for line in fr:
        print(line.strip())


f = open('demotext.txt', 'r')
print("Current pointer position : ",f.tell())  # gives the current file pointer position

# Write to the file
fileex = open('C:\\ppt\\Python\\Examples\\demo1.txt', 'w')
fileex.writelines("This is the example of python. This is a language which is largely used for handling large data and uused in data science")
fileex.close()

fileex = open('C:\\ppt\\Python\\Examples\\demo1.txt', 'a')
fileex.writelines('''This is the information added 
             later
             this is another one''')
fileex.close()


fileex = open('C:\\ppt\\Python\\Examples\\demo1.txt','r')
#The seek(offset[, from]) method changes the current file position
# The offset argument indicates the number of bytes to be moved.
# The from argument specifies the reference position from where the bytes
# are to be moved.
#If from is set to 0, it means use the beginning of the file as the reference position and
# 1 means use the current position as the reference position and
# if it is set to 2 then the end of the file would be taken as
# the reference position.

fileex.seek(12,0)
print('example of seek',fileex.read())

#os.mkdir("D:\\Anjali\\Fergusson College\\Newdir")
print(os.getcwd())

shutil.copyfile("C:\ppt\Python\Examples\demo1.txt","C:\ppt\Python\Examples\demo5.txt")

f1 = open("C:\ppt\Python\Examples\demo1.txt",'r')
f2 = open("C:\ppt\Python\Examples\demo5.txt",'a')

for line in f1:
   f2.write(line)
f2.close()

f2 = open("C:\ppt\Python\Examples\demo5.txt",'r')
print(f2.read())

f3 = open('demotext.txt', 'r')
text = f3.read()
text = re.sub('tell everyone','explain', text)
print(text)

fromdirectory = "C:\ppt\Python\Examples\\trial"
todirectory = "C:\ppt\Python\Examples\\Newdir"

copy_tree(fromdirectory,todirectory)

#os.rename("D:\Anjali\Fergusson College\demo.txt","D:\Anjali\Fergusson College\demonew.txt")

#f = open('C:\\Users\\Anjali\\Pictures\\Screenshots\\Screenshot1.png','rb+') # opening a binary file
#content = f.read() # reading all lines
#print(content)
#shutil.copyfile("C:\\Users\\Anjali\\Pictures\\Screenshots\\Screenshot1.png","C:\\Users\\Anjali\\Pictures\\Screenshots\\Screennew.png")
#f.close()

flen = os.path.getsize("C:\ppt\Python\Examples\demo5.txt")

print('file length:',flen)

# Reading the 2nd line in file
linenumber = 2
f1 = open("C:\ppt\Python\Examples\\demotext.txt",'r')
currentline=1
for line in f1:
    if currentline == linenumber:
        print("This is the second line")
        print(line)
        break
    currentline = currentline+1
