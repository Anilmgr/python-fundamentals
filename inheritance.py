class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printName(self):
         print("Full Name: {0} {1} ".format(self.fname,self.lname))

class ChildPerson(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

    def __str__(self):
        return "Full Name: {0} {1} ".format(self.fname,self.lname)
    
    def printInfo(self):
        print("Name: {} {}, Age: {}".format(self.fname,self.lname,self.age))

p1 = ChildPerson("Anil", "Baral", 25)
print(p1)

p2 = ChildPerson("Jhon", "Doe", 30)
p2.printName()

p2.printInfo()

