# Surrounded by either single quotation marks, or double quotation marks. #

# Assign to variable #

# single line string
s = "Anil"
print(s)

# multiple line string
s = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(s)

# String as Array #
a = 'Hello World'
print(a[1])     # prints letter of index 1 => 'e'

# Looping String #
for x in "apple":
    print(x)

# String Length #
t = "Hello Python"
print(len(t))   # returns 12

# Check String #
txt = "You are awesome the way you are!"
print("way" in txt) # returns boolean check if substring exist

# Slice str[start idx:end idx] #
# => start idx included
# => end idx not included

b = "Hello World"
print(b[2:5])       #returns llo
print(b[2:])        #returns llo World
print(b[:5])        #returns Hello
print(b[-5:-2])     #returns Wor

