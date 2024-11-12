# There may be times when we want to get data from our class that need to be calculated
# for example, we might want an attribute that shows the monthly salary

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
       #self.monthly_salary = salary / 12 # This is not efficient as we need to add the property when creating the class and update it every time the salary changes
        self._monthly_salary = None       # However, we may want to cache (store in memory) the value so they the calculation is not run every time 
    
    # Instead we can use the property decorator to create a 'computed property' which will act like an attribute
    
    @property
    def monthly_salary(self):
        if self._monthly_salary == None:                  # Calculation is only run if it has not been calculated for a new salary
            self._monthly_salary = self.salary / 12       # This calculation is fairly basic but this caching method would be ore applicable to more complex calculations
        return  f'£{format(self._monthly_salary, '.2f')}' # now 'monthly_salary' is called as a attribute but acts as a function
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        if salary <= 0:
            raise ValueError('Salary cannot be negative')
        self._monthly_salary = None # Resets self._monthly_salary' to none when salary is changed
        self.__salary = salary
    
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

# Now we can get the monthly_salary calculated correctly even after modification of the salary
print(george.monthly_salary)
george.increase_salary(10)
print(george.monthly_salary)