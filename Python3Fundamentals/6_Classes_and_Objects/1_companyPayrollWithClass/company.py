# We need to import the Employee class we made in the employee file
# The syntax for importing is 'from <file> import <class>'

from employee import Employee

class Company:
    def __init__(self): # This company class does not have parameters
        self.employees = [] # It's only property is the list of employees
    
    def addEmployee(self, newEmployee): # A method is required to add employees to the list
        self.employees.append(newEmployee)
    
    def getEmployees(self): # We also need a method to retrieve the Employees
        print('Current employees:\n')
        for employee in self.employees:
            print(employee.fName, employee.lName)
        print('')
    
    def payEmployees(self): # We can also create a method for to get the employees paycheck
        print('Monthly paychecks:\n')
        for employee in self.employees:
            print('Paycheck for:', employee.fName, employee.lName)
            print('Amount: $', format(employee.calcPaycheck(), ",.2f"), sep='')
            print('')

# Unlike JavaScript we do need to write 'new' before creating a new iterances of a class

def main():

    myCompany = Company()

    employee1 = Employee('Dave', 'Smith', 50000)
    myCompany.addEmployee(employee1)
    employee2 = Employee('John', 'Doe', 25000)
    myCompany.addEmployee(employee2)
    employee3 = Employee('Jane', 'Doe', 60000)
    myCompany.addEmployee(employee3)

    myCompany.getEmployees()
    myCompany.payEmployees()

main()