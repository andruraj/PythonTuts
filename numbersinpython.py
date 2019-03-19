from random import *

#Single line comment
'''Multi
line
commment'''
#brackets in java = indents in python
#variable types are auto defined
#numbers follow BODMAS

print(1+2-3*2)
print((50 - 5*6) / 4)   #Division (/) always returns a float
print(2**4)             #use the ** operator to calculate powers
x = 5 * 10 - 1
print(x)

x = 1+2j                #supports complex numbers
print(x)

#Casting
x = 3
y = 2.15315315313532
print(float(x))             #casting int to float
print("y = " + str(y))      #casting float to string

'''
int(x)	    Converts x to an integer
long(x)	    Converts x to a long integer
float(x)	Converts x to a floating point number
str(x)	    Converts x to an string. x can be of the type float. integer or long.
hex(x)	    Converts x integer to a hexadecimal string
chr(x)	    Converts x integer to a character
ord(x)	    Converts character x to an integer
'''

#Random -> import random module
print(random())         # Generate a pseudo-random number between 0 and 1.
print(randint(1,100))   # Pick a random number between 1 and 100.
print(uniform(1,10))   # generate a random floating point number between 1 and 10

#random in lists
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(items)          #shuffle items in list
print(items)
print(sample(items,1))  #pick 1 random item from list
print(sample(items,4))  #pick 4 random item from list