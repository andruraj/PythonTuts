#Function
def my_function():
    print("Hello From My Function!")
my_function()

#Functions with parameters
def sum_two_numbers(a, b):
    return a + b
print(sum_two_numbers(19,76))

#Default Parameter Value
def myCountry(country = "Norway"):
  print("I am from " + country)
myCountry("India")
myCountry()

'''
Recursion

Python also accepts function recursion, which means a defined function can call itself.
Recursion is a common mathematical and programming concept. It means that a function 
calls itself. This has the benefit of meaning that you can loop through data to reach 
a result. The developer should be very careful with recursion as it can be quite easy 
to slip into writing a function which never terminates, or one that uses excess amounts 
of memory or processor power. However, when written correctly recursion can be a very 
efficient and mathematically-elegant approach to programming. In this example, 
tri_recursion() is a function that we have defined to call itself ("recurse"). 
We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
'''
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Multiple Function Arguments
def foo(first, second, third, *therest):
#The "therest" variable is a list of variables, which receives all arguments 
#which were given to the "foo" function after the first 3 arguments.
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5)

#It is also possible to send functions arguments by keyword, so that the order of the argument does not matter
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))


#Example program
# edit the functions prototype and implementation
def foo1(a, b, c, *d):
    return len(tuple(d))

def bar1(a, b, c, **d):
    if d.get("magicnumber") == 7:
        return True
    else:
        return False


# test code
if foo1(1,2,3,4) == 1:
    print("Good.")
if foo1(1,2,3,4,5) == 2:
    print("Better.")
if bar1(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar1(1,2,3,magicnumber = 7) == True:
    print("Awesome!")

#Lambda functions
#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
x = lambda a, b : a * b
print(x(5, 6))