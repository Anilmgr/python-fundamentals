import re

# re Function
'''
Function----Description----
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string
'''

txt = "a quick brown fox jumps over the lazy dog"
x = re.search("^a.*dog$",txt)
y = re.findall("o", txt)
z = re.split("\s", txt)
w = re.sub("\s", "9", txt)
print(x)
print(y)
print(z)
print(w)

'''
The Match object has properties and methods used to retrieve information about the search, and the result:
=> .span() returns a tuple containing the start-, and end positions of the match.
=> .string returns the string passed into the function
=> .group() returns the part of the string where there was a match
'''

print(x.span())
print(x.string)
x = re.search(r"\bd\w+",txt)
print(x)
print(x.group())