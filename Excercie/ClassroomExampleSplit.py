
import re

string = 'Twelve:12 Eighty nine:89.'
pattern = ':'

result = re.split(pattern, string)
print(result)

