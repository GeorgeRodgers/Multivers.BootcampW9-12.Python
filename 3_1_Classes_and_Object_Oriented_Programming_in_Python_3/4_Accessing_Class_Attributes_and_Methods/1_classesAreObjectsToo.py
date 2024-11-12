class Employee:
    minimum_wage = 1000 # Instead of storing values in each instance we can store them in the class to reduce memory usage
    
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._monthly_salary = None
    
    @property
    def monthly_salary(self):
        if self._monthly_salary == None:
            self._monthly_salary = self.salary / 12
        return  f'£{format(self._monthly_salary, '.2f')}'
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, salary):
        if salary < Employee.minimum_wage:
            raise ValueError(f'Salary cannot be below minimum wage, £{Employee.minimum_wage}')
        self._monthly_salary = None
        self.__salary = salary
    
    def get_salary(self):
        return f'£{format(self.salary, '.2f')}'
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)
    
    def __str__(self):
        return f'{self.__dict__}'
    
    def __repr__(self):
        return (
            f'Employee('
            f'{repr(self.name)}, '
            f'{repr(self.age)}, '
            f'{repr(self.salary)})'
        )

# Classes are themselves objects, and as such they have attributes which can viewed with the classes' dictionary
# As we can below, function and properties are attributes of the class object

print(Employee.__dict__) # returns {'__module__': '__main__',
                         #          'minimum_wage': 1000,
                         #          '__init__': <function Employee.__init__ at 0x000001E1CE328CC0>,
                         #          'monthly_salary': <property object at 0x000001E1CE315300>,
                         #          'salary': <property object at 0x000001E1CE315CB0>,
                         #          'get_salary': <function Employee.get_salary at 0x000001E1CE328FE0>,
                         #          'increase_salary': <function Employee.increase_salary at 0x000001E1CE329080>,
                         #          '__str__': <function Employee.__str__ at 0x000001E1CE3291C0>,
                         #          '__repr__': <function Employee.__repr__ at 0x000001E1CE329260>,
                         #          '__dict__': <attribute '__dict__' of 'Employee' objects>,
                         #          '__weakref__': <attribute '__weakref__' of 'Employee' objects>,
                         #          '__doc__': None
                         #         }