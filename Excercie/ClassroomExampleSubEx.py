import re

result = re.sub('was','is','Bharat was a land of agriculture and it was full of energy')
print(result)

pattern = re.compile('is')
result = pattern.findall('Bharat is a land of agriculture and it is full of energy')
print(result)