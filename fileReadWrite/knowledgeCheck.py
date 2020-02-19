with open('copyText.txt', mode='w+') as t:
	text1 = t.write('give money mordekeiser')
	t.seek(0)
	print(t.read())