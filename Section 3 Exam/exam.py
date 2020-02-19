# Examples
s = 'hello' # grab "e"
print[s[1]]
# Reverse string s
print(s[::-1])
# Produce letter "o" in two different methods
print(s[-1])
print(s[4])

# Build this list [0,0,0] in two separate ways
list1 = [0,0,0]
# Reeassign 'hello' in this nested list to say 
# 'goodbye' instead
list3 = [1,2,[3,4,'hello']]
insideList = list3[-1]
insideList[-1] = 'goodbye'
print(list3)
print(insideList)

# Sort the list below
list4 = [5,3,4,6,1]
print(list4)
list4.sort()
print(list4)


# Using keys and indexing, grab the 'hello'
# from the following dictionaries

d = {'simple_key':'hello'}
# Grab Hello
print("Grab Hello from Dictionary : ", d)

print(d['simple_key'])

# Grab Hello

d2 = {'k1':{'k2':'hello'}}

print("Grab Hello from Dictionary : ", d2)
print(d2['k1']['k2'])
# Grab Hello
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print("Grab Hello from Dictionary : ", d3)
# first = d3['k1']
# second=first[0]['nest_key'][1]
# second=d3['k1'][0]['nest_key'][1]
# print(first)

print(d3['k1'][0]['nest_key'][1])
print("__________________________")

# Grab Hello

dragon = {'k1':[1,2,{'k2':['this is tricky', {'though':[1,2,['hello']]}]}]}
print("Grab Hello from Dictionary : ", dragon)
one = dragon['k1'][2]['k2'][1]['though'][2]
print(one)

# What is the difference between tuples and lists?
# Tuple elements cannot be changed while list's can