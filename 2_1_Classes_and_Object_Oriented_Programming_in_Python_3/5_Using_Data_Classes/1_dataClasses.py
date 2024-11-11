from dataclasses import dataclass

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project # In this class the intention is to have an instance of a project class attached to the employee


# These '__init__()' functions are fairly long and cna be simplified using the dataclasses module (see line 1)

# class Project:
#     def __init__(self, name, payment, client):
#         self.name = name
#         self.payment = payment
#         self.client = client
#        
#     def __repr__(self):
#         return f"Project(name={repr(self.name)}, payment={repr(self.payment)}, client={repr(self.client)})"

# Now we can use the dataclass decorator to define the 'Project' class

@dataclass # this will proved both the __init__ and __repr__ methods written above
class Project:
    name: str
    payment: int
    client: str

new_project = Project('testProject', 123456, 'testClient')
george = Employee('George', 29, 25000, new_project)

# When we print the project attribute of the employee instance we are given the project representation

print(george.project)

# This strategy is referred to as 'composition' and is often used instead of inheritance
# Inheritance implements an 'is a' relationship
# Composition implements a 'has a' relationship