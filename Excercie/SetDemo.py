thisset = {'apple',3, True,'guava','banana'}
print("Original Set ",thisset)

thisset.add('Cricket')
print("After adding element ",thisset)

anotherset = {'banana',67,89.7,True}

list = [2,3,4]

thisset.update(list)
print('After updating ',thisset)

print("Union : ",thisset.union(anotherset))   #prints the union of the sets
# The union() function combines the data present in both sets.

print("Intersection: ", thisset.intersection(anotherset))  # only common elements
# The intersection() function finds the data present in both sets only.

print("Difference: ", thisset.difference(anotherset))  # deletes the data present in both and outputs data
# present only in the set passed.
# The difference() function deletes the data present in both and outputs data present only in the set passed.

print("Sym_diff: ", thisset.symmetric_difference(anotherset))  # No common elements
# The symmetric_difference() does the same as the difference() function but outputs the data
# which is remaining in both sets.


set1={1,2,8,4,5,10}
set2={4,5}
print(set1.issubset(set2))

print(set1 > set2) # set1.issuperset(set2)

set3 = set1 - set2   # difference
print(set3)

#set4 = sorted(set(thisset))
set4 = sorted(set(set1))  # will work with similar data types
print("Sorted :",set4)

set5 = {'cherry','apple','ararot','chickoo','banana'}
print(sorted(set5))

set1.pop()
print(set1)

set1.remove(10)
print(set1)

set1.discard(10)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)  #This method will keep only the items that are present in both sets.

print("intersection_update ex: ",x)

x1 = {"apple", "banana", "cherry"}
y1 = {"google", "microsoft", "apple"}

x1.symmetric_difference_update(y1) # This method will keep only the elements that are NOT present in both sets.

print("Symmetric differece ex: ",x1)

