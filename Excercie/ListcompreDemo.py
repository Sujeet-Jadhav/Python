list = ['apple','banana','berry','cherry']
anotherlist = [x for x in list if "b" in x]
print(anotherlist)

list1=[1,2,3,4,5]
newlist = [x ** 2 for x in list1]

print(newlist)

list2 = [3,6,8,2,9]
newlist=[x for x in list2 if x<7]
print("new list : ",newlist)

list3 = ['apple','banana','pineapple','cherry']
newlist = [x for x in list3 if 'apple' in x]
print(newlist)

