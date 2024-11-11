from dataclasses import dataclass

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

@dataclass(slots=True) # To implement slots into dataclasses, we simply set slots to true for the decorator
class Project:
    # In the dataclass style 'type hints' are provided along with the attributes
    # They provide a hint to the type f value you expect them to have
    # Because Python is a dynamic language it is still possible to define payment as a string
    name: str
    payment: int
    client: str

new_project = Project('testProject', 123456, 'testClient')
george = Employee('George', 29, 25000, new_project)

print(george.project)