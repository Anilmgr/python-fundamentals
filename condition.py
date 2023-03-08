# if..else statement #
a = 33
b = 200

# if #
if a > b:
    print("a is greater.")

# short hand if #
if a > b: print("a is greater.")

# if...else #
if a > b:
    print("a is greater.")
else:
    print("b is greater.")

# short hand if..else #
print("a is greater.") if a > b else print("b is greater.") 

# elif #
a = 50

if a == 5:
    print("value of a is 5")
elif a > 5:
    print("value of a is greater than 5")
else:
    print("valie of a is lesser than 5")

# and #
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or #
if a > b or a > c:
  print("True of any conditions is True")

# not #
if not a > 300:
    print("condition statisfied")

# Nested if #
age = 25
if age >= 19:
    print("Eligible to vote")
    if(age > 60):
        print("Elder")
    else:
        print("Younger")

# pass Statement #
'''
if statements cannot be empty, but if you for some reason have an if statement with no content, 
put in the pass statement to avoid getting an error.
'''
x = 5
y = 10
if x < y:
    pass