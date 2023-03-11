# Python Lambda #
# A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

# Syntax #
# lamda arguments : expression
 

x = lambda a : a+3
print(x(5))

sum = lambda a, b : a + b
print(sum(5,10))

# Why Use Lambda Functions? #
'''
The power of lambda is better shown when you use them as an anonymous function inside another function.
Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
'''

def multiplyer(n):
    return lambda a : a*n

tripler = multiplyer(3)
print(tripler(4))

doubler = multiplyer(2)
print(doubler(4))