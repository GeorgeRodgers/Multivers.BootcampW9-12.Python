# In order to create novel instances of a class we need to pass the parameter values to the class as arguments

class Employee:
    def __init__(self, name, age, position, salary): # We still include self along with the parameter arguments
        self.name = name # These are then set parameter to the attribute
        self.age = age
        self.position = position
        self.salary = salary

e = Employee('testName', 'testAge', 'testPosition', 'testSalary') #The parameter values are then passed to the class constructor here

print(e.name) # Prints the attribute parameter
print(e.age)
print(e.position)
print(e.salary)

print(e.__class__) # we can use '.__class__' to get the class of an object