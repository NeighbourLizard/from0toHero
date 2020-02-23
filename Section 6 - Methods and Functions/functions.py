def name_function():

	print("Hello")

help(name_function)
print(name_function())

print("==============================")

def say_hello(name='NAME'):
	'''
	DOCSTRING: Information about function
	INPUT: Name
	OUTPUT: hello
	'''
	return 'Hello! '+name

result = say_hello('George')
print(result)

def add(n1,n2):
	return n1+n2

print("==============================")

sum = add(30,200)
print(sum)

print("==============================")

# Is the word "Dog" in the string?
# 

def doggoCheck(someString):
		return 'dog' in someString.lower()

result = doggoCheck('big DOG ')
print(result)

print("==============================")

def pigLatin(word):
	a = ['a','e','i','o','u']
	if word[0].lower == a():
		return word(-1).append('ay')
	else:
		return word.append(word[0] + 'ay')

result333 = pigLatin('magazine')
print(result333)