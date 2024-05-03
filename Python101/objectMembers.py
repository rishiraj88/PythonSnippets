class Employee:
    nEmployees = 0
    increment = 0.01
    def __init__(self,name,sal,increment) -> None:
        self.id=name
        self.name = name
        self.sal = sal
        self.increment = increment
        Employee.nEmployees += 1

    def raiseMySalaryAtStandardRate(self):
        self.sal = self.sal*(1+Employee.increment)
    
    def raiseMySalaryAtMyProfileRate(self):
        self.sal = self.sal*(1+self.increment)

    def raiseMySalaryAtArbitraryRate(self,incRate):
        self.sal = self.sal*(1+incRate)

    @classmethod
    def modifyIncrementRate(cls,newRate):
        increment = newRate

# 1. to view the data members of instances and of class 
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

# 2. to use instance method and class method
print(emp001.sal)
emp001.raiseMySalaryAtMyProfileRate()
print(emp001.sal)
emp001.sal = 20000
emp001.raiseMySalaryAtStandardRate()
print(emp001.sal)
emp001.sal = 20000
emp001.raiseMySalaryAtArbitraryRate(.3) # raise by 30 percent
print(emp001.sal)

