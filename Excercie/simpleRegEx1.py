# A Python program to demonstrate working of
# findall()
import re

# A sample text string where regular expression
# is searched.
string = """Hello my Number is 123456789 and
			my friend's number is 987654321 there"""

# A sample regular expression to find digits.
regex = 'there\Z'

match = re.findall(regex, string)
print(match)

pattern = re.findall(r"[^0-9]", string)
print(pattern)
print(pattern.__getitem__(2))



