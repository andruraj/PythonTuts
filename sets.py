#Set is a collection which is unordered and unindexed. No duplicate members.
#Once a set is created, you cannot change its items, but you can add new items.
#Create a Set
thisset = {"apple", "banana", "cherry"}
print(thisset)

print(set("my name is Eric and Eric is my name".split()))

#Access items -> no index
for x in thisset:
  print(x)

#Check
print("banana" in thisset)

#Set Manipulation
thisset.add("orange")       #add single item
print(thisset)

thisset.update(["orange", "mango", "grapes"])       #add multiple items
print(thisset)

print(len(thisset))
thisset.remove("banana")        #If the item to remove does not exist, remove() will raise an error.
print(thisset)
thisset.discard("banana")       #If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)
    
'''remove last item in set -> Sets are unordered, so when using the pop() method,
you will not know which item that gets removed.'''
thisset.pop()   
print(thisset)

thisset.clear()
print(thisset)

del thisset

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

'''
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
'''

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])
#and
print(a.intersection(b))
print(b.intersection(a))
#Except what is present in both sets
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#minus
print(a.difference(b))
print(b.difference(a))

print(a.union(b))

