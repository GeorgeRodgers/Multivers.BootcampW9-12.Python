# Methods from previous sections removed for clarity
# Getter and Setter method are also used in python

class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.set_salary(salary) # although the setter is defined below, we are able to call it here
    
    # With this setter method we can inject logic so that a salary cannot be set to less than zero
    def set_salary(self, salary):
        if salary <= 0:
            raise ValueError('Salary cannot be negative')
        self.salary = salary
    
    # Currently the attributes of this class are not private so there is not much point to having a getter other than to format the output of 'self.salary
    def get_salary(self):
        return f'£{format(self.salary, '.2f')}'

george = Employee('George Rodgers', 29, 'Aspiring Developer', 2000)