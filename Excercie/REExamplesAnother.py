import re

with open("ExampleRE.txt", encoding="utf-8") as fre:
    for line in fre:
        name = re.search("\S*",line)
        re_obj = re.compile("\d{1,3}")
        #print(re_obj.group(0))
        if name.group(0).__eq__("Sachin"):
            line = re_obj.sub("47",line)
        else:
            line = re_obj.sub("48", line)
        print(line)


# Now try to replace this in the original file.


num = "111 1234 12345 123456 1234567 1 11"
print(len(re.findall(r'\d{3,7}',num)))
print(re.findall(r'\d{3,7}',num))


from datetime import datetime

now = datetime.now().time() # time object

print("now =", now)
print("type(now) =", type(now))



