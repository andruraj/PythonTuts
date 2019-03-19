#List is a collection which is ordered and changeable. Allows duplicate members.
x = ['b','a']       #initiate list
print(x)
print(x[0])         #list is indexed

x[0] = 'hello'      #change value
print(x)

y = [1,2,3]
print(y)

print(y * 3)        #multiplies instances of values

#add lists together
l = [x,y]           #add lists as sublists of a single main list
print(l)

#or

m = x + y           #combines to make a single list with all values
print(m)

#list manipulation
x.append('c')
print(x)

x.insert(1,'b')
print(x)

x.remove('hello')
print(x)

x.sort()
print(x)

x.reverse()
print(x)

del x[0]
print(x)

print(len(x))
print(max(x))
print(min(x))

x1 = list(('b','a'))        #Create list using 'list constructor'
print(x1)

#List Comprehensions
#List Comprehensions is a very powerful tool, which creates a 
#new list based on another list, in a single, readable line.
#example 1
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
#normal code
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

#using list comprehensions
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)

#example 2
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(n) for n in numbers if n > 0]
print(newlist)

#Remove duplicates in list
#using sets
duplist = [1,2,3,2,3,4,5]
duplist = list(set(duplist))
print(duplist)

#using dict
duplist = [1,2,3,2,3,4,5]
duplist = list(dict.fromkeys(duplist))
print(duplist)