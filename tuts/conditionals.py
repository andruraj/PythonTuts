x = 2.0
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

#Boolean
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

print(not False) # Prints out True
print((not False) == (False)) # Prints out False

#The "in" operator
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

#The 'is' operator -> check instance
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#Loops
print("\nIf loop")
#if Loop
if (isinstance(x,int)):
    print("x is an integer")
elif(isinstance(x,str)):
    print("x is an String")
else:
    print("x is not a string or integer")

#for loop
print("\nFor loop")
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):    #  =>  (start,stop-1,step)
    print(x)

#while loop
print("\nWhile loop")
# Prints out 0,1,2,3,4
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as (count = count + 1) or (count++)

#"break" and "continue" statements
'''break is used to exit a for loop or a while loop,
whereas continue is used to skip the current block,
and return to the "for" or "while" statement'''
# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)

print("\nCan we use 'else' clause for loops? Yes")
#unlike languages like C,CPP.. we can use else for loops
'''When the loop condition of "for" or "while" statement 
fails then code part in "else" is executed. If break statement
is executed inside for loop then the "else" part is skipped.
Note that "else" part is executed even if there is a continue statement.'''
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")


#Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
try:
    while 1:
        print(next(myit))
except StopIteration:
    print("Iteration Stopped")