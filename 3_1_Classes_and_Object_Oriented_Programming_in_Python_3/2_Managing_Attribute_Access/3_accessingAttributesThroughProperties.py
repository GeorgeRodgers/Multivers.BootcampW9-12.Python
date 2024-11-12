# If we were to implement this encapsulation strategy in a previously defined class it could lead to bugs
# For example many of the methods within this class have been written using '.salary' not '._salary'
# Instead of modifying every attribute modifiers we can use we utilize properties descriptor

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        # self.set_salary(salary) # Because we have used the decorated the setter on line 19, we no longer need to use the 'set_salary' method here
        self.salary =salary
        
    @property         # property decorator is prepended with '@' and converts the function to a property
    def salary(self): # This simply means the function can be called without the requirement of '()'
        return self.__salary
    
    # We can also redefine this setter function so that the '.salary' attribute can be set
    # For this we need to decorate the property ('salary') we have created
    @salary.setter # salary is now decorated as a setter
    def salary(self, salary):
        if salary <= 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = salary # This property descriptor only works as a getter and '.__salary' is required to modify data
    
    def get_salary(self):
        return f'£{format(self.salary, '.2f')}'
    
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
    
    def __repr__(self):
        return (
            f'Employee('
            f'{repr(self.name)}, '
            f'{repr(self.age)}, '
            f'{repr(self.position)}, '
            f'{repr(self.salary)})'
        )

george = Employee('George Rodgers', 29, 'Aspiring Developer', 25000)

# Both methods run

george.increase_salary(5)                      
print('Method result:',george.salary)

george.salary = 1000    
print('Setter result:',george.salary)