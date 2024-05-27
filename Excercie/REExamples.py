# Example of Regular expression
import re
str = "This is, the lesson; to be learnt: today in this; lecture"
#res = re.split(r'[,:;\s]',str)
str = re.sub(r'[,;:]',"$",str)
print(str)
#print(res)

st = "This, is the < most, remarkable job, till now."
print(re.findall(r'([,<.])',st))
print(len(re.findall(r'([,<.])',st)))
#re.match(r'<,.*',st)
print("----------------------------------------------------------------")
print("Email verification without using named groups")
statement = 'Please contact us at: placements@fergusson.edu'
match = re.search(r'([\w\.-]+)@([\w\.-]+)', statement)
if statement:
  print("Email address:", match.group()) # The whole matched text
  print("Username:", match.group(1)) # The username (group 1)
  print("Host:", match.group(2)) # The host (group 2)

print("------------------------------------------------------------------")
print(" With named groups")
str1 = "these are the email ids: abc@gmail.com hbcds@yahoo com a @ dd"
match = re.search(r'(?P<email>(?P<username>[\w.-]+)@(?P<host>[\w.-]+))', str1)
if str1:
  print("Email address:", match.group('email'))
  print("Username:", match.group('username'))
  print("Host:", match.group('host'))
#print("Email Matches: ", len(re.findall(r'w._%+-{1,20}@w.-{2,20}.A-Za-z{2,3}', str1)))

st = "these are the email ids: abc_12@gmail.com hbcds@yahoo.com anjali.naik@fergusson.edu @ dd"
#em = re.findall(r'(\S+@\S+\.\S+)',st)
em = re.findall(r'(\S+@\S+\.\S+)',st)
print(em)

mo = re.search(r'([0-9]+).*: (.*)', "Customer number: 254678, Date: March 31, 2021")
print(mo)
print("-------------------------------------------------------------------------------")
print(" With the html or xml tags")
fh = open("tags.txt")
for i in fh:
     res = re.search(r"<([a-z]+)>(.*)</\1>",i)
     print(res.group(1) + ": " + res.group(2))
print("*********************************************************************************")

# Postcode units consist of between five and seven characters,
# which are separated into two parts by a space.
# The two to four characters before the space represent
# the so-called outward code or out code intended to directly
# mail from the sorting office to the delivery office.
# The part following the space, which consists of a digit followed
# by two uppercase characters, comprises the so-called inward code,
# which is needed to sort mail at the final delivery office.
# The last two uppercase characters do not use the letters CIKMOV,
# so as not to resemble digits or each other when hand-written.
# The outward code can have the following form:
# One or two uppercase characters, followed by either a digit
# or the letter
with open("german_postal_codes.txt", encoding="utf-8") as fh_post_codes:
    codes4city = {}
    for line in fh_post_codes:
        res = re.search(r"[\d ]+([^\d]+[a-z])\s(\d+)", line)
        if res:
            city, post_code = res.groups()
            if city in codes4city:
                codes4city[city].add(post_code)
            else:
                codes4city[city] = {post_code}

with open("largest_cities_germany.txt", encoding="utf-8") as fh_largest_cities:
    for line in fh_largest_cities:
        re_obj = re.search(r"^[0-9]{1,2}\.\s+([\w\s-]+\w)\s+[0-9]", line)
        city = re_obj.group(1)
        print(city, codes4city[city])
print("--------------------------------------------------------")

example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]

pc_re = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"

for postcode in example_codes:
    r = re.search(pc_re, postcode)
    if r:
        print(postcode + " matched!")
    else:
        print(postcode + " is not a valid postcode!")
print("\n----------------------------")

# example with multiline

sample="""
 Sachin is 47 and Rahul is 48
 Saurav is 48 and Sunny is 65
"""

ages=re.findall(r'\d{1,3}',sample)
names = re.findall(r'[A-Z][a-z]*',sample)

nameagedict = {}
x=0

for eachname in names:
    nameagedict[eachname] = ages[x]
    x+=1
print(nameagedict)

