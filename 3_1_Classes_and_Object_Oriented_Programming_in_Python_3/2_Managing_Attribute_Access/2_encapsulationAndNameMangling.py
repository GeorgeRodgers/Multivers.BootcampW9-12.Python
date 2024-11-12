# Unlike JavaScript, python is designed to be open and so it is not possible to create private attributes in the same way
# The convention is to put an underscore before the attribute name to inform the user that the attribute is 'non-public'
# If you really need to stop access outside of a class you can use 'name mangling', this is where you prepend the attribute name with a double underscore

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary)
    
    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = salary # Double underscore works within the class
    
    def get_salary(self):
        return f'£{format(self.__salary, '.2f')}' # Double underscore works within the class

george = Employee('George Rodgers', 29, 'Aspiring Developer', 25000)

# print(george._salary) # If we only used a single underscore the '_salary' attribute can still accessed outside the class

try:
    print(george.__salary) # This will throw and error
except:
    print("The '.__salary' attribute is not globally accessible") # This code runs instead
    print(george.get_salary())