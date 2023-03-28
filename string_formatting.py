txt1 = "Hello {} {}, how are you?"
txt2 = "Hello {1} {0}, how are you?"
txt3 = "Hello {firstName} {lastName}, how are you?"
txt4 = "Its height is {:.2f}"

print(txt1.format("Jhon", "Doe")) # multiple
print(txt2.format("Doe", "Jhon")) # number indexed values
print(txt3.format(lastName = "Doe", firstName = "Jhon")) # name indexed value
print(txt4.format(22.567))