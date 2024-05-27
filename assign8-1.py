keys = ["one", "two", "three", "four", "five"]
values = [1, 2, 3, 4, 5]

ans = zip(keys, values)
ans = list(ans)
dic = dict()
for data in ans:
    dic[data[0]] = data[1]
print(dic)

res = float('inf')
key = None

for keys in dic:
    if res >dic[keys]:
        res = dic[keys]
        key = keys
    print(key," : ",dic[key])
