def myfunc(str):
	s = list()
	i = 0
	for letter in str:
		while i < len(str):
			i += i
			if i % 2 == 0:
				s.append(str[i].upper())
			elif i == 1:
				s.append(str[i].lower())
	return s
print(myfunc('Anthropomorphism'))

