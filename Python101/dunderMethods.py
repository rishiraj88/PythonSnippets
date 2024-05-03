class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getDetails(self):
        return "Person:: ("+self.name+", "+str(self.age)+" years old)"
class Employee(Person):
    nEmployees = 0
    increment = 0.01
    def __init__(self,name,age, sal, increment):
        super().__init__(name,age)
        self.id = name
        self.name = name
        self.salary = sal
        self.increment = increment
        Employee.nEmployees += 1

    def __str__(self):
        return super().getDetails() + "\nwith salary "+ "{:.2f}".format(self.salary)+" and increment rate "+"{:.2f}".format(self.increment)

    def raiseMySalaryWithMyProfileRate(self):
        self.salary += self.salary * self.increment

    @classmethod
    def from_str(cls, csv_data_str):
        name, age,sal, inc = csv_data_str.split(",")
        return cls(name,int(age), float(sal), float(inc))


ronak = Employee.from_str("name003,27,30000,.2")

"""
Without dunder __str__ definitions, the following two lines return output like: <__main__.Employee object at 0x000001A2A58F5C50>

And with the __str__ definitions in place, the following two lines return output like:
Person:: (name003, 27 years old)
with salary 30000.00 and increment rate 0.20
"""
print(str(ronak))
print(ronak)