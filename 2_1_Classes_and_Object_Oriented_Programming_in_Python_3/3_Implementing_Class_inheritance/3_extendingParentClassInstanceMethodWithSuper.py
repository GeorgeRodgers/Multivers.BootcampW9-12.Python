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
        # self.salary += self.salary * (percent/100) # Instead of rewriting this line 8 we can use 'super()' to call the parent function
        super().increase_salary(percent)
        self.salary += bonus

# This is referred to a writing "DRY" code, Don't Repeat Yourself