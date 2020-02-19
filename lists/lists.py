mylist = ['one', 'two', 'three']
mylist2 = ['four', 'five', 'six']
# Indexing and Splicing works exactly like with Strings
print[mylist[0]]
mylist1 = mylist + mylist2
print[mylist1]
mylist1[3] = 'Tasks 101'
print[mylist1]
mylist1.append('chick chick')
print[mylist1]
print[mylist1.pop()]
print[mylist1]
var = mylist1.pop()
print(var)
var2 = mylist1.pop(-4)
print(var2)
print(mylist1)

list2 = ['a', 'b', 'h', 'z', 'c']
print(list2)
# SORT just SORTS. IT DOES NOT RETURN ANYTHING.
# YOU CANNOT ASSIGN SORTED LIST TO A VARIABLE.
list2.sort()
print(list2)

list2.reverse()
print(list2)