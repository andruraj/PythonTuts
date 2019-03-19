'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''
try:
    f = open("demo.txt")            #default open
except Exception as err:
    print(err)

try:
    f = open("demo.txt","r")            #open as read only => r or read only text mode => rt
    print(f.read())                     #read full file
    print(f.read(5))                    #read first 5 char
    print(f.readline())                 #read first line
    for x in f:
        print(x)                        #read line by line
except Exception as err:
    print(err)

try:
    f = open("demo.txt", "a")               #open with append
    f.write("If file is not present, new file is created ")
    f.close()
    f = open("demo.txt", "r")
    print(f.read())
    f.close()
    f = open("demo.txt", "w")
    f.write("Text replaced/overwritten")
    f.close()
    f = open("demo.txt", "r")
    print(f.read())
    f.close()
except Exception as er:
    print(er)
    f.close()

#delete file
import os
if os.path.exists("demo.txt"):
  os.remove("demo.txt")
  print("File deleted")
else:
  print("The file does not exist")

#delete folder
import os
try:
    os.mkdir("myfolder")        #create folder
    os.rmdir("myfolder")        #delete folder  => You can only remove empty folders.
except Exception as er:
    print(er)