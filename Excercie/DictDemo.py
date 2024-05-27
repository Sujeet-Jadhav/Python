my_dict = {"Brands":"Mercedez","Year" :1955,"Colour":"White"}
print(my_dict)
print(my_dict["Year"])
my_dict["model"] = "Maruti"

print(my_dict)

my_dict.pop("Year")
print(my_dict)

poppeditem = my_dict.popitem()
#print(my_dict)
print("Popped item : ",poppeditem)

my_dict["brands"] = "Honda"
print(my_dict)

print(my_dict.keys())
print(my_dict.values())

my_dict1 = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81, 2:4}
for i in my_dict1:
    print(my_dict1[i])

print("Sorted dictionary : ",sorted(my_dict))
print("Sorted dictionary : ",sorted(my_dict1))