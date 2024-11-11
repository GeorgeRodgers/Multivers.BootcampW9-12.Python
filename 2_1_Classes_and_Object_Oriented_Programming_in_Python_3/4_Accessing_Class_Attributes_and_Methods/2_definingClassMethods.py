from datetime import date

class Employee:
    minimum_wage = 25000 # Given this value is stored to the class and not an instance we need to define a class method in order to edit it
    
    # To do this python provided with a special 'classmethod' decorator
    @classmethod
    def change_minium_wage(cls, new_minimum_wage): # With a classmethod we need to pass cls (class) as an argument
        cls.minimum_wage = new_minimum_wage
    
    # Another reason to uses class methods are for 'factory function' alterative constructor
    # We may do that when working with dates in order to calculate an employee's age
    # In order to do this we have import the 'date' class from the 'datetime' module on line 1
    
    @classmethod
    def new_employee(cls, name, dob): # The first parameter of the classmethod is the cls itself, followed by the employ name and dob 
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day)) # this calculates the age from the dob data provided
        return cls(name, age, cls.minimum_wage) # The entire function returns a call to create a new instance with the name, calculated age and class attribute of minimum wage
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
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

george = Employee.new_employee('George', date(1994, 12, 6)) # Because this is an alternative constructor we have to call the 'new_employee' method from the parent class
print(george.__repr__())