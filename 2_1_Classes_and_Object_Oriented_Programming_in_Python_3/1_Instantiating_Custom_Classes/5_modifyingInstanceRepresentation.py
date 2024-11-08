class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)
    
    def info(self):
        if self.position[0].lower() in 'aeiou':
            prefix = 'an'
        else:
            prefix = 'a'
        print(f'{self.name} is {self.age} years old. This employee is {prefix} {self.position} with a salary of £{format(self.salary, '.2f')}')
    
    def __str__(self):
        return f'{self.__dict__}'
    
    # Along with the '__str__' method the representation, '__repr__', should return a string
    # This string should represent the code used to evaluate the original instance
    def __repr__(self):
        return (
            f'Employee('
            f'{repr(self.name)}, '     # Inbuilt objects such as srt, int, float ect. have there own repr function
            f'{repr(self.age)}, '      # If we didn't use this, the attribute parameter would be returned as a variable
            f'{repr(self.position)}, ' # which would cause an error
            f'{repr(self.salary)})'
        )

george = Employee('George Rodgers', 29, 'Aspiring Developer', 25000)

# Methods with underscores before and after are called 'Dunder' methods (e.g. __init__, __str__, __repr__ ect.)
# This 'repr' method can be called in two ways
print(george.__repr__()) # standard '.method()' notation
print(repr(george)) # or 'function()' notation providing the instance as the argument

# Using the 'repr' we should be able to create a clone of the original instance
georgeClone = eval(repr(george)) # 'eval()' takes a string and evaluates it as python code

# The instances of the class will not be equal as they are stored in different parts of the memory
print(george == georgeClone) # evaluates to false

# They will contain the same information
print(george.__str__() == georgeClone.__str__()) # evaluates to true
print(george.__class__ == georgeClone.__class__) # evaluates to true