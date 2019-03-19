# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    '''or
    def description(self,name,kind,color,value):
        desc_str = "%s is a %s %s worth $%.2f." % (name, color, kind, value)
        return desc_str
    '''

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())

#Constructor
class Animal:
    def __init__(self,name):        #__init__() method is called the constructor
        self.name = name            #name is called class attributes
 
    def walk(self):
        print(self.name + ' walks.')
 
duck = Animal('Duck')
duck.walk()

#Encapsulation => In an object oriented python program, you can restrict access 
#to methods and variables. This can prevent the data from being modified by accident and is known as encapsulation.
#private is marked by __varName or __methodName
class Car:
 
    __maxspeed = 0
    __name = ""
    
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
    
    def drive(self):
        print ('driving.maxspeed ' + str(self.__maxspeed))
    
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
    
redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()

#Method Overloading is different in python
class Printing:
    def hello(self, name=None):
        if name:
            print("Hello " + name)
        else:
            print("Hello!")

a = Printing()
a.hello()
a.hello("Andru")

#Inheritance
class User:
    name = ""
    
    def __init__(self, name):
        self.name = name
    
    def printName(self):
        print ("Name  = " + self.name)
 
class Programmer(User):
    def __init__(self, name):
        self.name = name
    
    def doPython(self):
        print ("Programming Python")
 
brian = User("brian")
brian.printName()
diana = Programmer("Diana")
diana.printName()           #inherited name from User class
diana.doPython()

#Polymorphism
class Bear(object):
    def sound(self):
        print ("Groarrr")
 
class Dog(object):
    def sound(self):
        print ("Woof woof!")
 
def makeSound(animalType):
    animalType.sound()
 
bearObj = Bear()
dogObj = Dog()
 
makeSound(bearObj)
makeSound(dogObj)


#Inner Classes
class Human:
 
    def __init__(self):
        self.name = 'Guido'
        self.head = self.Head()
        self.brain = self.Brain()
    
    class Head:
        def talk(self):
            return 'talking...'
    
    class Brain:
        def think(self):
            return 'thinking...'
 
if __name__ == '__main__':
    guido = Human()
    print (guido.name)
    print (guido.head.talk())
    print (guido.brain.think())