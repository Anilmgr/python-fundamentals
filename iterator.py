# Iterator #
# An iterator is an object that contains a countable number of values.

# Iterator vs Iterable #
''' 
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator:
'''

# iterator on tuple
myTuple = ("apple", "asus", "acer", "dell") 
myIt = iter(myTuple)
print(next(myIt))
print(next(myIt))
print(next(myIt))

#iterator on string
myStr = "Anil"
myIter = iter(myStr)
print(next(myIter))
print(next(myIter))
print(next(myIter))


# loop through an iterator
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)

# Create an Iterator
# have to implement the methods __iter__() and __next__() to your object.

class MyIter:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a += 1
    return x

myObj = MyIter()
p1Iter = iter(myObj)
print(next(p1Iter))
print(next(p1Iter))
print(next(p1Iter))
print(next(p1Iter))

# Stop Iteration
class MyIterV2:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyIterV2()
myiter = iter(myclass)

for x in myiter:
  print(x)