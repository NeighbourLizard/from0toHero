# Use for, .split(), and if to create a Statement 
# that will print out words that start with 's':
# 
st = 'Sunny D and rum Print only the words that start with s in this sentence'
stSplit = st.split()
print(stSplit)
for word in stSplit:
	if word[0].lower() == 's':
		print(word)

print("\nNext Task: \n")

# Use range() to print all the even numbers from 0 to 10.
# 

x = list(range(0,10))
print(x)
for s in x:
	if s % 2 == 0:
		print(s)

print("\nNext Task: \n")

# Use a List Comprehension to create a list of 
# all numbers between 1 and 50 that are divisible by 3.
# 

x1 = list(range(1,50))
print(x1)
x3 = list()
for num in x1:
	if num % 3 == 0:
		x3.append(num)
print(x3)

print("\nNext Task: \n")

# Go through the string below and if the length of a word
#  is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'

for word in st.split():
	if len(word) % 2 == 0:
		print(word)

print("\nNext Task: \n")

# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
# 

x5 = list()

for element in list(range(1,100)):
	if element % 3 == 0 and element % 5 != 0:
		x5.append("Fizz")
	elif element % 5 == 0 and element % 3 != 0:
			x5.append("Buzz")
	elif element % 5 == 0 and element % 3 == 0:
			x5.append("Fizz Buzz")
	else:
		x5.append(element)

print(x5)

print("\nNext Task: \n")

# Use List Comprehension to create a list of the first letters 
# of every word in the string below:
# 

st2 = 'Create a list of the first letters of every word in this string'

x6 = list()

for element in st2.split():
	x6.append(element[0])
print(x6)