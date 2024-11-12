# In addition to attributes, classes can also be assigned methods as well

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    # Defining an instance method is the same as defining a function
    # These methods are not global and will only work for instances of this class
    # We must also pass 'self' as an argument and use 'dot' notation
    # This is because even though objects use dictionaries they ar not dictionaries

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)
    
    def info(self):
        if self.position[0].lower() in 'aeiou': # logic handles basic grammar of noun prefix
            prefix = 'an'
        else:
            prefix = 'a'

        print(f'{self.name} is {self.age} years old. This employee is {prefix} {self.position} with a salary of £{format(self.salary, '.2f')}')

george = Employee('George Rodgers', 29, 'Aspiring Developer', 25000)

# Calling the method to the instance saved to a variable will run the function
george.info()
george.increase_salary(15) # updates salary
george.info() # shows updated salary
