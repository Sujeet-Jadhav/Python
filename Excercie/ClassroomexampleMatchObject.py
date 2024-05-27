import re

string = '12345 456, 2021 1111'

# Three digit number followed by space followed by two digit number
#pattern = '(\d{3})(\d{2})' #will give 12345
pattern = '(\d{3}) (\d{2})' #will give 345 45

# match variable contains a Match object.
match = re.search(pattern, string)

if match:
  print(match.group())
else:
  print("pattern not found")

print(match.groups())
print(match.group(1))
print(match.group(1,2))

print('start: ',match.start())
print('end: ',match.end())
print('span : ',match.span())

print(match.re)
print(match.string)
