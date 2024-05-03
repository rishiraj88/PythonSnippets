class Employee:
    nEmployees = 0
    increment = 0.01
    def __init__(self,name,sal,increment) -> None:
        self.id=name
        self.name = name
        self.sal = sal
        self.increment = increment
        Employee.nEmployees += 1

    def raiseMySalaryWithMyProfileRate(self):
        self.sal += self.sal * self.increment
    @classmethod
    def from_str(cls,csv_data_str):
        name,sal,inc = csv_data_str.split(",")
        return cls(name,float(sal),float(inc))


ronak = Employee.from_str("name003,30000,.2")
print(ronak.increment)
print(ronak.sal)
ronak.raiseMySalaryWithMyProfileRate()
print(ronak.sal)