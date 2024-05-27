import re
phn = "412-555-1212"
if re.search(r'\w{3}-\w{3}-\w{4}', phn):
    print("Valid phone number")
# To check for a valid date format or to retrieve a date
s='Today is 21-12-2021 and tomorrow is 22/12/2021'
mo = re.findall(r'\d{2}[-/]\d{2}[-/]\d{4}', s)
print(mo)#.group())


# To check for valid Email id format
email = "anjali.naik@fergusson.edu principal@fergusson.edu abc@abl.com md@.com @ceo.com pc@.com abc@gmc.co.in"

# \S matches any non-whitespace character
# @ for as in the Email
# + for Repeats a character one or more times
print("Matches : ",len(re.findall('\S+@\S+',email)))


#email = "anjali.naik@fergusson.edu "

#print("Matches : ",len(re.findall('([a-zA-Z0-9\\_\\-\\.]+)@([a-zA-Z]+).(.+)',email)))

#([a-zA-Z0-9\\_\\-\\.]+) 1 or more lowercase letters,
# uppercase letters, digits, and special characters
# including underscore, hyphen, and full stop
# (first capture group i.e. username)
# @ at symbol
#([a-zA-Z]+) 1 or more lowercase and uppercase letters
# (second capture group i.e. domain name)
#. a single full stop character
#(.+) 1 or more characters (third capture group i.e. domain)