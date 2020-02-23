def pigLatin(word):
	first_letter = word[0]
	if first_letter.lower() in 'aeiou':
		pig_word = word + 'ay'
	else:
		pig_word = word[1:] + first_letter + 'ay'

	return pig_word

def myfunc(*args, **kwargs):
	print(args)
	print(kwargs)
	print('I would like {} {}'.format(args[0],kwargs['food']))

print("=========================================")

theWordIs = 'leri'
result333 = pigLatin(theWordIs)
print(result333)

print("=========================================")

myfunc(10,20,30, fruit='orange', food='eggs', animal='dog')
