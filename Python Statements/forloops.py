# my_iterable = [1,2,3]
# for item_name in my_iterable:
# 	print(item_name)

mylist = [1,2,3,4,5,6,7,8,9,10]
for number in mylist:
	if number % 2 == 0:
		print(number)
	else:
		print('Odd Numbers: ', number)

print("=====================================")
print("=====================================")
print("=====================================")

list_sum = 0

for num in mylist:
	list_sum = list_sum + num
print(list_sum)


print("=====================================")
print("=====================================")
print("=====================================")

for var in 'Hello World':
	print(var)


print("=====================================")
print("=====================================")
print("=====================================")

tuplllle = (1,2,3)

for item in tuplllle:
	print(item)

# Tuples have some special perks with for loops

mylist2 = [(1,2),(3,4),(5,6),(7,8)]

# for var2 in mylist2:
#	print(var2)

# If we imitate the structure inside the tuple
# we can call unto specific elements
for (a,b) in mylist2:
	print(a)

print("=====================================")
print("=====================================")
print("=====================================")

# How to iterate through dictionary?

d = {'k1':1, 'k2':2, 'k3':3}

for var3 in d.items():
	print(var3)