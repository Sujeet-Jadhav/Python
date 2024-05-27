import re

rstr = "45678"

print("Matches: ", len(re.findall(r'\d{5}', rstr)))
#re.findall() Return all non-overlapping matches of pattern in string,
# as a list of strings. The string is scanned left-to-right,
# and matches are returned in the order found.