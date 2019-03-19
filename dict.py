#Dict are like Maps in java
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
#Creating dict
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
#or
thisdict =	{
  "brand": "Ford",      #key:value
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#accessing items
print(thisdict.get('year'))
print(thisdict["model"])

for name, number in phonebook.items():      #items() for both keys and values
    print("Phone number of %s is %d" % (name, number))

for x in thisdict:
  print(thisdict[x])        #only values
#or
for x in thisdict.keys():   #use keys() or values()
    print(x)

#update
thisdict["year"] = 2018
print(thisdict)

#add
thisdict["color"] = "red"
print(thisdict)

#Dict manipulation
print(len(thisdict))

#delete
#The popitem() method removes the last inserted item
thisdict.popitem()
print(thisdict)
#or
del phonebook["John"]
print(phonebook)
#or
phonebook.pop("Jill")
print(phonebook)

thisdict.clear()
print(thisdict)

del thisdict
print("thisdict Dictionary is now deleted")

#The dict() Constructor
thisdict =	dict(brand="Ford", model="Mustang", year=1964)  #single bracket
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)


#Dict from lists or tuples
x = ('key1', 'key2', 'key3')
y = 0
a = dict.fromkeys(x, y)
print(a)