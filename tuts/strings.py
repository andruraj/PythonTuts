print("hello world!")
print("hello"+"world")

x = "hello world!"
print("hello world!")

#x = int(input())                  #set data type of input
print(x)

#x = input("Enter name: ")
print(x)
print(x[2])
print(x[2:4])                      #called String slicing
print(x[:2])
print(x[2:])
print(x[3:42])
print(x[42:])
print(x[:42])
print(x[-1])                       #last char
print(x[1:5:2])                    #char 1 to 5 skipping 1 char -> extended slicing -> [start:stop-1:step]
print(x[::-1])                     #reverse

print('"Isn\'t," they said.')       #use \ for special characters
print("'hi'")                       #using single quote
print(r"hello \n \r \t ' \" \ ")    #raw string using r before strings. (Cannot use " though)


#String literals

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(3 * 'un' + 'ium')             #3 times 'un', followed by 'ium'
print('py' 'thon')
print('py''thon')
a = 'py'
print(a + 'thon')                   #can't concatenate a variable and a string literal -> print(a 'thon') will give error

#python strings are immutable
# x[1] = 'k' will give error


#string formatting
print("String: %s" % 'hello')
print('String:  {}'.format('hello'))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

'''
%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''

#String Operations
s = "i'll catch you if you fall - The Floor"
print(s)
print(s.capitalize())         #capitalise first letter (converts other characters to lower case -> notice 'Floor')
print(s.find('Floor'))        #find is case sensitive
print(s.index("F"))
print(s.index("f"))           #index is case sensitive
print(s.count('l'))
print(s.isalpha)            #check if all are alphabets. Other functions are 'isalnum'-alphanumeric, isspace, isascii, isdecimal, isprintable
len(s)                      #string length
print(s.replace("Floor","Ground"))
print(s.upper())
print(s.lower())
print(s.startswith("i"))
print(s.endswith("I"))
print(s.strip('aeiou'))                 #removes trailing(first and last)
print(s.title())                        #capitalise first letter in each word
newlist = s.split(" ")
print(newlist)