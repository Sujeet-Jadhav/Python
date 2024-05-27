import re

result=re.findall(r'.','SA is largest Analytics community of India')
print(result)
print()

result=re.findall(r'\w','SA is largest Analytics community of India')
print(result)
print()

result=re.findall(r'\w*','SA is largest Analytics community of India')
print('*',result)
print()

result=re.findall(r'\w+','SA is largest Analytics community of India')
print('+',result)
print()

result=re.findall(r'^\w','SA is largest Analytics community of India')
print(result)
print()

result=re.findall(r'\w$','SA is largest Analytics community of India')
print(result)
print()

result=re.findall(r'\b[aeiouAEIOU]\w+','SA is largest Analytics community of India')
print(result)
print()
