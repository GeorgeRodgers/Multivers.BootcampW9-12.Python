# Occasionally you my have a related method you want to share with only some child classes
# You cannot put this in the parent class as this would pass the method every child
# And rewriting the method in every child class would not follow the principle of 'DRY' coding
# In this case we could create a second parent class for select child classes to inherit from

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

# Not every parent class will use a dictionary to store their attributes
# In this case we may want to add a method to check this only to certain child classes

class DictInspectorMixin: # The 'Mixin' suffix doesn't has a purpose other than to explain we are mixing this class into another
    def uses_dict(self):
        return hasattr(self, "__dict__")

class Tester(Employee):
    def run_test(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")


class Developer(DictInspectorMixin, Employee): # The Developer class now inherits from both super classes
    def __init__(self, name, age, salary, framework):
        super().__init__(name, age, salary)
        self.framework = framework
    
    def increase_salary(self, percent, bonus = 0):
        super().increase_salary(percent)
        self.salary += bonus


developer = Developer('person1', 123, 20000, 'Flask')

print(developer.uses_dict()) # The instance is able to use the 'uses_dict()' function

# In the case that a method was repeated in a parent class with a slightly different functionality, we can use the '__mro__' attribute on the class to return a tuple with the order in which the methods will be search for within the inheritance tree

print(Developer.__mro__) # returns '(<class '__main__.Developer'>, <class '__main__.DictInspectorMixin'>, <class '__main__.Employee'>, <class 'object'>)'