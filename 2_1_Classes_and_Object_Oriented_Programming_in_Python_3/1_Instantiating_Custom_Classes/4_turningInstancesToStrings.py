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
        return f'{self.__dict__}' # The '__str__' method must return a string, so here we have converted the stored diction into a string

george = Employee('George Rodgers', 29, 'Aspiring Developer', 25000)

# Printing instance in Python is not as simple as in JavaScript
# print(george) # This gives the name of class for this instance and it's position in the memory which isn;t very useful
# Output:  <__main__.Employee object at 0x000002012B582D20>

# This is a default behaviour and can be changed by defining a '__str__' method

print(george)