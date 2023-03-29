import os

'''
# There are four different methods (modes) for opening a file:
    "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    "a" - Append - Opens a file for appending, creates the file if it does not exist
    "w" - Write - Opens a file for writing, creates the file if it does not exist
    "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)
'''

## READ ##

f = open('hello.txt','r')
g = open('hello.txt','r')

print(f.read())
f.close()

print(g.read(4)) # first 4 character
g.close()

fh = open('hello.txt','r')
print(fh.readline())
print(fh.readline())
fh.close()

fl = open('hello.txt','r')
for y in fl:
    print(y)
fl.close()

## WRITE ##
f = open("hello1.txt", 'a') # append
f.write("Hello Python ")
f.close()

f = open("hello1.txt", 'r')
print(f.read())
f.close()

f = open("hello1.txt", 'w') # write
f.write("Hello Python ")
f.close()

f = open("hello1.txt", 'r')
print(f.read())
f.close()

try:
    f = open("myfile.txt", 'x') # create
    print(f.write("This is created file"))
    f.close()
except:
    print("Already created!")    
finally:
    f = open("myfile.txt", 'r')
    print(f.read())
    f.close()

## Remove file ##

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("This file does not exist")

if os.path.exists("folder"):
    os.rmdir("folder")
else:
    print("This folder does not exist")