# Classes are essentially blocks of code used to create objects
# These contain both information stored as a dictionary but also functions that are specific to the class

class Employee: # 'class' keyword used to create a new class followed by the name
    def __init__(self): # Unlike JavaScript the 'self' keyword is used instead of 'this' amd must be passed as an argument during the creation of a class
        self.name = 'testName' # For the purpose of this test no arguments are passed as parameters
        self.age = 'testAge'
        self.position = 'testPosition'
        self.salary = 'testSalary'

e = Employee() # Creates a new instance of the 'Employee' class and save it to a variable

print(e) # Prints information about the object and not the information in the object

print(e.__dict__.keys()) # Prints the entire dictionary stored in this instance of the class

print(e.name) # Prints the attribute parameter
print(e.age)
print(e.position)
print(e.salary)