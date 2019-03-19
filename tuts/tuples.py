#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Tuples are lists that cannot be changed
#they share attributes like (len, max, min, indexing, slicing and other basics) with lists
a = (3,)        #comma is required for a single item to be a Tuple
x = ("Diana", 32, "New York")
print(a)
#x[1] = 'Orange'   ->   Returns error. Tuples are unchangeable
print(x)

#Once a tuple is created, you cannot add or remove items. Tuples are unchangeable.

#you can use tuples to assign multiple variables at once
name,age,country = x
print(country)

#append to tuple
x = (3,4,5,6)
x = x + (1,2,3)
print(x)
print(len(x))
print(max(x))
print(min(x))

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])
# Following action is not valid for tuples
# tup1[0] = 100
tup3 = tup1 + tup2     #add tuples
print(tup3[::-1])       #reverse

del tup3  #-> for deleting tuples

#difference with lists
list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)
print(type(list_num))
print(type(tup_num))
print('list_num=',list_num.__sizeof__())
print('tup_num=',tup_num.__sizeof__())          #low size, faster than lists

#list <-> tuple
newlist = list(tup_num)
newtuple = tuple(list_num)

'''
Why use a tuple instead of a list?

Program execution is faster when manipulating a tuple than 
it is for the equivalent list. (This is probably not going 
to be noticeable when the list or tuple is small.)Sometimes 
you don’t want data to be modified. If the values in the collection 
are meant to remain constant for the life of the program, 
using a tuple instead of a list guards against accidental 
modification. There is another Python data type that you will 
encounter shortly called a dictionary, which requires as one of 
its components a value that is of an immutable type. A tuple can 
be used for this purpose, whereas a list can’t be.
    1.The literal syntax of tuples is shown by parentheses () whereas the literal syntax of lists is shown by square brackets [] .
    2.Lists has variable length, tuple has fixed length.
    3.List has mutable nature, tuple has immutable nature.
    4.List has more functionality than the tuple.
'''