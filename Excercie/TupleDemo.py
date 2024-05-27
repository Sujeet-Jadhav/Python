my_tuple = (1,2,3,4,'pqr',6,7,8)
print(my_tuple)

my_tuple = list(my_tuple)
my_tuple[0] = 'abc'
my_tuple = tuple(my_tuple)

print(my_tuple)

(a,b,c,*d) = my_tuple
print(" The asterisk tuple")
print(a)
print(b)
print(c)
print(d)

my_tuple1 = (1, 2, 3, ['hindi', 'python'])
my_tuple1[3][0] = 'english'    # updated hindi with english
print(my_tuple1)
print(my_tuple1.count(2))
print(my_tuple1.index(['english', 'python']))

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
