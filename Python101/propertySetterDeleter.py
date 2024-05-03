class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getDetails(self):
        return "Person:: ("+self.name+", "+str(self.age)+" years old)"
class Employee(Person):
    nEmployees = 0
    increment = 0.01
    def __init__(self,name,age, sal, increment,username):
        super().__init__(name,age)
        self.id = name
        self.name = name
        self.salary = sal
        self.increment = increment
        self.username=username
        Employee.nEmployees += 1

    @property
    def email(self):
        if self.username == None:
            return "Email ID not available"
        return self.username+"@commail.com"

    @email.setter
    def email(self,new_email_id):
        self.username=new_email_id

    @email.deleter
    def email(self):
        self.username=None
    def __str__(self):
        return super().getDetails()+", "+self.email + "\nwith salary "+ "{:.2f}".format(self.salary)+" and increment rate "+"{:.2f}".format(self.increment)

    def raiseMySalaryWithMyProfileRate(self):
        self.salary += self.salary * self.increment

    @classmethod
    def from_str(cls, csv_data_str):
        name, age,sal, inc,username = csv_data_str.split(",")
        return cls(name,int(age), float(sal), float(inc),username)


ronak = Employee.from_str("name003,27,30000,.2,emp003a0")
print(ronak) # emp003a0@commail.com

ronak.username = "ronak"
print(ronak) # ronak@commail.com
ronak.email = "emp003a1"
print(ronak) # emp003a1@commail.com

del ronak.email
print(ronak) # Email ID is not available