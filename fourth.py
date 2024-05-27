res = lambda temp: sorted(temp)

Tuple = (1, 2, 3, 4), (1, 2, 3, 4)
ans = list()
for data in Tuple:
    ans.append(tuple(res(data)))
ans = tuple(ans)
print(ans)
