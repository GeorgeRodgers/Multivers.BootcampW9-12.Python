# all class created in python inherit functionality from the 'object' class
# this is where the default dunder methods come from

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def run_test(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")
        

class Developer(Employee):
    def increase_salary(self, percent, bonus = 0):
        self.salary += self.salary * (percent/100)
        self.salary += bonus

tester = Tester('person1', 123, 20000)
developer = Developer('person2', 123, 20000)

# We can inspect instances of of a class using the globally available 'isinstance' and 'issubclass' functions

# All return true as expected
print(isinstance(tester, Tester))
print(isinstance(tester, Employee))

print(issubclass(Developer, Employee))
print(issubclass(Developer, object))
print(issubclass(Employee, object))