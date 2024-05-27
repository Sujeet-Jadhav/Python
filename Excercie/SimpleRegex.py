import re
example = "This is the example FOR for regular expression"
regexample = re.match(r'\w{3}',example)
print(regexample.group()) #This
regexample = re.search(r'\w{7}',example)
print(regexample.group())    #example
regexample = re.findall(r'\w{7}',example)
print(regexample) #['example', 'regular', 'express']
regexample=re.compile(r'\s',flags=0)
print(regexample.search(example)) #<re.Match object; span=(4, 5), match=' '>
#----------------------------------------------------------
#example 2
example2="This is 1 and this is 22. Here $ is very important"
regexample2 = re.compile(r'\d+',flags=0)
print(regexample2.search(example2).group()) #1
print(regexample2.findall(example2)) #['1', '22']

print(re.search(r'[\d*]',example2).group())  #1

print(re.findall(r'[\d*]',example2))  #['1', '2', '2']

print(re.split(r'\d',example2))
#['This is ', ' and this is ', '', '. Here $ is very important']

print(re.split(r'[\d|\s]',example2))
#['This', 'is', '', '', 'and', 'this', 'is', '', '', '.', 'Here', '$', 'is', 'very', 'important']


print(re.sub(r'\d+','this is replaced',example2))
#This is this is replaced and this is this is replaced. Here $ is very important

example3="""This is a example of multiline
to represent the regular
expression example for metacharacters"""
result=re.findall(r'.+',example3)
print(result)
#['This is a example of multiline', 'to represent the regular', 'expression example for metacharacters']

result=re.findall(r'.+',example3,re.S)
print(result)
#['This is a example of multiline\nto represent the regular\nexpression example for metacharacters']

result=re.findall(r'^\w{2,4}',example3,re.M)
print(result)
#['This', 'to', 'expr']

result=re.findall(r'^\w{4}',example3,re.M)
print(result)
#['This', 'expr']

result=re.findall(r'\w{2}$',example2)
print(result)
#['nt']

numstr = "Numbers are 1,12, 23, 123, 12345"
result=re.findall(r'\d\d*',numstr)
print(result)
#['1', '12', '23', '123', '12345']

numstr = "Numbers are 1,12, 23, 123, 12345"
result=re.findall(r'\d\d+',numstr)
print(result)
#['12', '23', '123', '12345']