dict = {'Data Structure': 45,'Database': 36, 'Python' : 40,'Java':48}

print(dict)

min_value = min(dict.values())

for key,value in dict.items():
    if value == min_value :
        min_key = key

print(min_key, " : " ,min_value)