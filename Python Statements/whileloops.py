# while some_boolean_condition:
# do something
# else can also be used

x = 0

while x < 5:
	print(x)
	x += 1
	# x += 1 == x = x + 1
else:
	print("X ain't less than 5")

# keywords: break, continue, pass
# break - Breaks out of the current closest enclosing loop
# conitnue - goes to the top of the current closest enclosing loop
# pass - does nothing at all

x = [1,2,3]
for item in x:
	pass
print('end of my script')

print("=============================")
print("=============================")

mystring = 'Sammy'

for letter1 in mystring:
	if letter1 == 'a':
		continue
	print(letter1)

print("=============================")
print("=============================")

for letter in mystring:
	if letter == 'a':
		break
	print(letter)

print("=============================")
print("=============================")

x1 = 5

while x1 < 100:
	x1 += 1
	if x1 == 44:
		print("x = 44")
		break
	else:
		continue
		print("not yet.", "X only equals to : ", x1)

print("=============================")
print("=============================")