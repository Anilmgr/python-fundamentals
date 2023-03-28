'''
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks
'''

#Exception handeling

try:
    print(x)
except:
    print("x is undefined")

#multiple exceptions
try:
  print(x)
except NameError:
  print("x is not defined")
except:
  print("Something else went wrong")

try:
   print(1)
except:
   print("Something went wrong")
else:
   print("nothing went wrong")


#finally
try:
   print(x)
except:
   print("something is fishy")
finally:
   print("Always there")

#raise an exception (throw)

age = 15

try:
   if(age < 16):
      raise Exception("Not elegible to vote!")
except:
   print("unable to proceed")