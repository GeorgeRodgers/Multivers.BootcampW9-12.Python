# It is possible to import multiple classes from a file
from employee import Employee, SalaryEmployee, HourlyEmployees, CommissionEmployees

class Company:
    def __init__(self):
        self.employees = []

    def addEmployee(self, new_employee):
        self.employees.append(new_employee)
    
    def getEmployees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('')

    def payEmployees(self):
        print('Paying Employee: ')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calcPaycheck():,.2f}')
            print('')

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Sarah', 'Hess', 50000)
    my_company.addEmployee(employee1)
    employee2 = HourlyEmployees('Lee', 'Smith', 25, 50)
    my_company.addEmployee(employee2)
    employee3 = CommissionEmployees('Bob', 'Brown', 30000, 5, 200)
    my_company.addEmployee(employee3)

    my_company.getEmployees()
    my_company.payEmployees()

main()