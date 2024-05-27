list = [1,2,1,4,2,3,5]
print(list)


list.insert(3,'abc')    #Insert an item at a given position.
print("Element inserted at location 3")
print(list)

print("Length of the list : ",len(list))

print("List with the elements from 1st to 3rd location: ",list[1:4])

list.remove(3)
print("Element removed from position 3: ",list)

del list[2]
print(list)

x = 2
if x in list :   # List membership operator
    print('Element is present')

print("Prints the list two times : ",list * 2)

list2 = ['abc',4,6]
print("Appending the lists list1 and list2 : ",list+list2)

list3 = [3,2,5,1,6,8,7]
print("Sorted list : ",sorted(list3))      #Return a new sorted list from the items in iterable.

list3.append([1,'a'])    # Add an item to the end of the list
print("Appended list: ",list3)

list3.extend([1,'a']) # Extend the list by appending all the items from the iterable.
print("Extends method : ",list3)

x= list3.pop(4)
print("Popped item : ",x)

print("Item appeared : ",list3.count(5))








