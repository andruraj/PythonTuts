#Partial functions allow one to derive a function with x parameters 
#to a function with fewer parameters and fixed values set for the more limited function.
from functools import partial

def mul(x,y):
    return x*y
a = partial(mul,4)
print(a(2))

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
a=partial(func,5,6,7)
print(a(8))

print(dir(func))    #returns all attr

#Closures
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

transmit_to_space("Test message")

def print_msg(number):
    def printer():
        "Here we are using the nonlocal keyword"
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)
#Without the nonlocal keyword, the output would be "3 9", 
# however, with its usage, we get "3 3", that is the value of the "number" variable gets modified.
print_msg(9)

#eg1
def transmit_to_space1(message):
  "This is the enclosing function"
  def data_transmitter():
      "The nested function"
      print(message)
  return data_transmitter

fun2 = transmit_to_space1("Burn the Sun!")
fun2()

#eg2
def multiplier_of(number):
    def multiply(n):
        return n*number
    return multiply
multiplywith5 = multiplier_of(5)
a = multiplywith5(9)
print(a)