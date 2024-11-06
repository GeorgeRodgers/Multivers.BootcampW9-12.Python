# If we want to pay employee in different way (hourly/salary) we can create separate classes for this
# These can be linked to the parent class below to inherit the name parameters
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

# We no longer need the add the name parameters from the parent class
# In order to do this we need to add the parent class in parenthesis in the class statement
class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        # We use the super function to call it from the parent class
        super().__init__(fname, lname)
        self.salary = salary

    def calcPaycheck(self):
        return self.salary / 12
    
# Now we can repeat this for the hourly employees calling on the name parameters from the parent class
# and adding parameters for hours worked and hourly rate
class HourlyEmployees(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        # New parameters
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    # This class requires an alternative paycheck calculation
    def calcPaycheck(self):
        return self.weekly_hours*self.hourly_rate

# A class can also inherit parameters from child classes
# For example a commission employee earns a salary and can copy all parameters from the salary employee
# But they also earn commissions which requires additional parameters
class CommissionEmployees(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, com_rate):
        super().__init__(fname, lname, salary)
        self.sales_num = sales_num
        self.com_rate = com_rate
    
    def calcPaycheck(self):
        regular_salary = super().calcPaycheck()
        total_commission = self.sales_num*self.com_rate
        return regular_salary + total_commission