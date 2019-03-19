import re

#the re.match function can be used to determine whether it matches at the beginning of a string.
pattern = r"spam"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")

#The function re.search finds a match of a pattern anywhere in the string.
if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

#The function re.findall returns a list of all substrings that match a pattern.
print(re.findall(pattern, "eggspamsausagespam"))

match = re.search(pattern, "eggspamsausage")
if match:
   print(match.group())     #group returns the string matched
#start and end which return the start and ending positions of the first match
   print(match.start())
   print(match.end())
   print(match.span())      #span returns the start and end positions of the first match as a tuple.

#Substitute all occurences
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

#Metacharacters
#(dot) => .
pattern = r"gr.y"
if re.match(pattern, "grey"):
   print("Match 1")
if re.match(pattern, "gray"):
   print("Match 2")
if re.match(pattern, "blue"):
   print("Match 3")

#(^ and $) match the start and end of a string, respectively.
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
   print("Match start")
if re.match(pattern, "gray"):
   print("Match end")
if re.match(pattern, "stingray"):
   print("No Match")

#Character Classes => square brackets
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
   print("Vowels found")
if re.search(pattern, "qwertyuiop"):
   print("Vowels found")
if re.search(pattern, "rhythm myths"):
   print("Vowels not found")

#The class [a-z] matches any lowercase alphabetic character.
#The class [G-P] matches any uppercase character from G to P.
#The class [0-9] matches any digit. 
#Multiple ranges can be included in one class. For example, [A-Za-z] matches a letter of any case.
pattern = r"[A-Z][A-Z][0-9]"
if re.match(pattern, "LS8"):
   print("Match 1")
if re.match(pattern, "E3"):
   print("Match 2")
if re.match(pattern, "1ab"):
   print("Match 3")

#Place a ^ at the start of a character class to invert it. 
pattern = r"[^A-Z]"
if re.match(pattern, "this is all quiet"):
   print("only lowercase")
if re.match(pattern, "AbCdEfG123"):
   print("Match 2")
if re.match(pattern, "THISISALLSHOUTING"):
   print("Match 3")

# * matches 0 or more occurrences of the preceding expression.
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
   print("Match 1")
if re.match(pattern, "eggspamspamegg"):
   print("Match 2")
if re.match(pattern, "spam"):
   print("Match 3")

# [a^] => Zero or more repetitions of "a" or "^"

# + matches 1 or more occurrence of the preceding expression.
pattern = r"g+"
if re.match(pattern, "g"):
   print("Match 1")
if re.match(pattern, "gggggggggggggg"):
   print("Match 2")
if re.match(pattern, "abc"):
   print("Match 3")

# ? means "zero or one repetitions"
pattern = r"ice(-)?cream"           #eg.2 -> colo(u)?r
if re.match(pattern, "ice-cream"):
   print("Match 1")
if re.match(pattern, "icecream"):
   print("Match 2")
if re.match(pattern, "sausages"):
   print("Match 3")
if re.match(pattern, "ice--ice"):
   print("Match 4")

#{x,y} means "between x and y repetitions of something"
#Hence {0,1} is the same thing as ?.
#If the first number is missing, it is taken to be zero. If the second number is missing, it is taken to be infinity.
pattern = r"9{1,3}$"
if re.match(pattern, "9"):
   print("Match 1")
if re.match(pattern, "999"):
   print("Match 2")
if re.match(pattern, "9999"):
   print("Match 3")

#Groups

#A group can be created by surrounding part of a regular expression with parentheses. 
#This means that a group can be given as an argument to metacharacters such as * and ?.
pattern = r"egg(spam)*"
if re.match(pattern, "egg"):
   print("Match 1")
if re.match(pattern, "eggspamspamspamegg"):
   print("Match 2")
if re.match(pattern, "spam"):
   print("Match 3")

#eg2 => '([^aeiou][aeiou][^aeiou])+' gives 1 or more reps of nonvowels,vowels,nonvowels

#A call of group(0) or group() returns the whole match. 
#A call of group(n), where n is greater than 0, returns the nth group from the left. 
#The method groups() returns all groups up from 1.
pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())

'''
There are several kinds of special groups. 
Two useful ones are named groups and non-capturing groups.
Named groups have the format (?P<name>...), where name is the name of the group, 
and ... is the content. They behave exactly the same as normal groups, except they 
can be accessed by group(name) in addition to its number. Non-capturing groups have 
the format (?:...). They are not accessible by the group method, so they can be added 
to an existing regular expression without breaking the numbering.
'''
pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

#eg2
pattern = r"(a)(b(?:c)(d)(?:e))"
match = re.match(pattern, "abcde")
if match:
    print(len(match.groups()))

# | used for OR
#eg => red|blue

#Special Sequences
#backslash followed by another character => number of times reg ex is repeated
pattern = r"(.+) \1"
match = re.match(pattern, "word word")
if match:
   print ("Match 1")
match = re.match(pattern, "?! ?!")
if match:
   print ("Match 2")    
match = re.match(pattern, "abc cde")
if match:
   print ("Match 3")

#Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to the 
#first group's subexpression, which is the matched expression itself, and not the regex pattern.

'''
More useful special sequences are \d, \s, and \w.
These match digits, whitespace, and word characters respectively. 
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_].
In Unicode mode they match certain other characters, as well. For instance, \w matches letters with accents.
Versions of these special sequences with upper case letters - \D, \S, and \W - mean 
the opposite to the lower-case versions. For instance, \D matches anything that isn't a digit.

Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively. 
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.
'''

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())