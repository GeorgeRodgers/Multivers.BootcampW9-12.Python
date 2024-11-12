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
    # We can also override the '__init__' method from parent class to include extra attributes
    def __init__(self, name, age, salary, framework):
        # We can use 'super()' to run the parent 'init' method
        super().__init__(name, age, salary) # We do not need to provide 'self' as an argument
        self.framework = framework
    
    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus

developer = Developer('person1', 123, 20000, 'Flask') # We can now initialise the new developer instance with the extra 'Framework' argument

print(developer.name)
print(developer.framework)
print('The new attribute has been correctly initialized')