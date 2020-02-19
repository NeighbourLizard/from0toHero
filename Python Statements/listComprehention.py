mystring = 'hello'

mylist = []

for letter in mystring:
	mylist.append(letter)

print(mylist)

# mylist = [letter for letter in mystring]
# It's the same as he previous statement just shorter

mylist1 = [num for num in range (0,11)]
print(mylist1)

# for loops
mylist2 = [num**2 for num in range(0,11)]
print(mylist2)

# if statement
mylist3 = [something for something in range(0,11) if something % 2 == 0]
print(mylist3)

# Example of more complex thingy

celcius = [0, 10, 20, 35.5]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

# ^^^^^^^^^^^^^^^^^
# is the same as
# |||||||||||||||||
# vvvvvvvvvvvvvvvvv

fahrenheit = []
for temp in celcius:
	fahrenheit.append((9/5)*temp + 32)
print(fahrenheit)

# It's also possible to include else if but it's NOT RECOMMENDED
# because it looks ugly and it's hard to read

results = [x if x%2==0 else 'ODD' for x in range(0,11)]
print(results)

# We can also transform nested loops
# ALSO NOT RECOMMENDED DUE TO SAME REASONS AS ABOVE

mylist = []
for x in [2,4,6]:
	for y in [1,200,300]:
		mylist.append(x*y)
print(mylist)

mylist4 = [x*y for x in [2,4,6] for y in [1,10,1000]]
print(mylist4)