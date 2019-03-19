'''
Generators are very easy to implement, but a bit difficult to understand.
Generators are used to create iterators, but with a different approach. 
Generators are simple functions which return an iterable set of items, one at a time, in a special way.
When an iteration over a set of item starts using the for statement, the generator is run. 
Once the generator's function code reaches a "yield" statement, the generator yields its 
execution back to the for loop, returning a new value from the set. The generator function 
can generate as many values (possibly infinite) as it wants, yielding each one in its turn.
'''

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))



# eg2
def fib():
    a, b = 1, 1
    while 1:
        yield a
        a, b = b, a + b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break