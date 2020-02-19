# Range Operator will print numbers UNTIL the number
# It's also called generator because it generates elements

# range(0,11,2) creates a list from 0 up until 11 with 2 intervals
a = list(range(0,11,2))
print(a)
for variab in range(3,10):
	print(variab)

# Inumerate

index_count = 0

for letter in 'abcde':
	print('At index {} the letter is {}'.format(index_count,letter))
	index_count += 1

# Now lets use inumerate

word = 'abcde'
for index,letter in enumerate(word):
	print(index)
	print(letter)
	print('\n')

# Zip Function (Zips together 2 lists)

mylist2 = [1,2,3]
mylist3 = ['a', 'b', 'c']
mylist4 = ['a', 'c', 'd','10']
for item33 in zip(mylist2,mylist3,mylist4):
	print(item33)

# Zip works for as long as the shortest list

a = 'a' in ['A world full of surprises']
print (a)

# min and max

mylist34 = [1,2,3,4,5,6,1,2,312,3,45,45,43]
print(min(mylist34))
print(max(mylist34))

# random library and shuffle
# shuffle does NOT return anything!!!!
# You can't write a = shuffle(mylist)

from random import shuffle
print(mylist34)
shuffle(mylist34)
print(mylist34)

# random integer
from random import randint

print(randint(0,100))

#input

result = input('Whats your name?')
print("Hello {}".format(result))