# myfile = open('textFile.txt')
# Sometimes file won't open a second time. In this case we use
# myfile.seek(0) which reads the file again
# myfile.seek(0)
# print(myfile.readlines) 
# This works but you will get /n 
# A better option is below:
# print(myfile.read())
# Don't forget to close the file in the end
# myfile.close()

# GOOD and Correct way of opening files with "with" statement

# with open('file.txt', mode = 'r')
# r stands for read only, 
# w stands for write only (and will overwrite the file or create a new one))
# r+ stands for read + write
# w + stands for writing and reading
# a stands for append (add a line)

with open('textFile.txt', mode='w+') as my_new_file:
	my_new_file.write('This is a new string for this text file')
	my_new_file.seek(0)
	contents = my_new_file.read()
	print(contents)


with open('textFile.txt', mode='a') as f:
	f.write('\n take me to church')
	f.seek(0)
	contents1 = f.read()
	print(contents1)

with open('somethingsomething.txt', mode='w+') as d:
	d.write('New File bitches')
	d.seek(0)
	contents2 = d.read()
	print(contents2)