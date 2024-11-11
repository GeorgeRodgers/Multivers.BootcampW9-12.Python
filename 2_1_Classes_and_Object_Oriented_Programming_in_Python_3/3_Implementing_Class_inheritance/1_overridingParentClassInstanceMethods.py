# The parent class is occasionally called the super class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

# To inherit all parameters and methods from a parent class, pass the class as an argument to the child class
class Tester(Employee):
    def run_test(self): # The tester class has an additional method which is specific to the Tester class
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")
        

class Developer(Employee):
    # It is possible to override parent methods by redefining them in the child class
    # This concept is referred to as polymorphism 
    def increase_salary(self, percent, bonus = 0): # Here an additional bonus is parameter is added and the default argument is set to to zero
        self.salary += self.salary * (percent/100)
        self.salary += bonus

tester = Tester('person1', 123, 20000)
developer = Developer('person2', 123, 20000)

tester.increase_salary(10)
developer.increase_salary(10, 100)

print(f"tester salary increased to {tester.salary}")

print(f"developer salary increased to {developer.salary}")

try:
    tester.increase_salary(0, 100) # Cannot provide second bonus argument to the tester instance
except:
    print("It is not possible to provide a bonus as a second argument to the tester instance")