import re

print("Match")
result = re.match(r'SA', 'SA Analytics Pune SA')
print(result.group(0))
print()

print("Search")
result = re.search(r'Analytics', 'SA Analytics Pune SA')
print(result.group(0))
print()

print("Split")
result=re.split(r'y','Analytics')
print(result)
print()
result=re.split(r'i','Analytics Pimpri Pune')
print(result)
print()
result=re.split(r'i','Analytics Pimpri',maxsplit=1)
print(result)
print()

print("Compile and findall")
pattern = re.compile('SA')
result=pattern.findall('SA Analytics Pune SA')
print(result)
result2=pattern.findall('SA is largest analytics community of India')
print(result2)

Str = "we need to inform him with the latest information"

for i in re.finditer("inform.", Str):
    locTuple = i.span()
    print(locTuple)

rstr = """ You Should Never
  Give Up Easily
  Keep trying."""
print(rstr)
regex = re.compile("\n")
rdstr = regex.sub(" ", rstr)
print(rdstr)

print("Lowercase s:", re.search(r'Eat\scake', 'Eat cake').group())
print("Uppercase S:", re.search(r'cook\Se', "Let's eat cookie").group())

# classroom examples
str1 = "This is the example"
#res = re.search(r'\w',str1).group(0)
res = re.findall(r'\w*',str1)
print(res)

res = re.search(r'\w\w',str1).group(0)
print(res)

res = re.findall(r'\b[aeiou]\w+',str1)  # can also try using ^
print(res)

line = "This is, the name; of the , person who: works in the, company"
#res = re.split(r'[,;:\s]',line)
line = re.sub(r'[,;:\s]','%',line)
print(line)

line1 = "abc@gmail.com"
res = re.findall('@\w+.\w+',line1)
print(res)

line1 = " This is 2 digit number and those are 3 and 4 digit numbers"
res = re.findall(r'\d',line1)
print(res)

today = " date is 23/04/2021"
res = re.findall(r'\d{2}/\d{2}/\d{4}',today)
print(res)



