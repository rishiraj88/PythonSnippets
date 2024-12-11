class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def getDetails(self):
        return "Person:: ("+self.__name+", "+str(self.__age)+" years old)"
class Employee(Person):
    __nEmployees = 0
    __increment = 0.01
    def __init__(self,name,age, sal, increment,username):
        super().__init__(name,age)
        self.__id = name
        self.__name = name
        self.__salary = sal
        self.__increment = increment
        self.__username=username
        Employee.__nEmployees += 1

    @property
    def __email(self):
        if self.__username == None:
            return "Email ID not available"
        return self.__username+"@commail.com"

    @__email.setter
    def email(self,new_email_id):
        self.__username=new_email_id

    @__email.deleter
    def email(self):
        self.__username=None
    def __str__(self):
        return super().getDetails()+", "+self.__email + "\nwith salary "+ "{:.2f}".format(self.__salary)+" and increment rate "+"{:.2f}".format(self.__increment)

    def raiseMySalaryWithMyProfileRate(self):
        self.__salary += self.__salary * self.__increment

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