class Employee:
    nEmployees = 0
    def __init__(self,name,sal,increment) -> None:
        self.name = name
        self.sal = sal
        self.increment = increment
        Employee.nEmployees += 1

print(Employee.nEmployees)
emp001 = Employee("name01",20000,0.02)
print(Employee.nEmployees)
emp002 = Employee("name02",15000,0.03)
print(Employee.nEmployees)
emp002 = Employee("name02",15000,0.03) # assigning to emp002 again, with identical initializer
print(Employee.nEmployees) # output?? interesting to see

print(emp001.__dict__)
print(emp001.__class__)
print("---------")
print(Employee.__dict__)