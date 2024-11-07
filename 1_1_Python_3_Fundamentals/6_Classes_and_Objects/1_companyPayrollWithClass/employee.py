# Classes in Python are very similar to JavaScript, however the syntax is slightly different
# The class can have both properties and defined methods

class Employee:
    def __init__(self, fName, lName, salary):
        self.fName = fName
        self.lName = lName
        self.salary = salary
    
    def calcPaycheck(self): # 'self' is always passed to the class method as an argument
        return self.salary/12 # Splits paycheck into monthly amounts

