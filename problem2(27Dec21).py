"""
Problem 2:
Create a class named "Employee" .It should contain following attributes
First Name
Last Name
Age
Location
Email -> firstname.lastname@company.com
Salary

(a) Define methods to do the following operations
(1) create email from the first and last names
(2) Print the details of the employee in a readable table format Eg: Tabulate module - https://pypi.org/project/tabulate/
(b) Demonstrate this program using 3 sample employee objects
(c) Calculate the time used for execution of this program
(d) Read about the significance of self parameter
"""
"""
from tabulate import tabulate


class Employee:

    def __init__(self, first_name, last_name, age, location, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = first_name + "." + last_name + "@xyz.com"
        self.location = location
        self.salary = salary
        self.emp_list = []

    # created email for emplyee
    def getemail(self):
        return self.email

    # display table form created emp_details
    def del_emp(self):
        self.emp_list.append(self.first_name)
        self.emp_list.append(self.last_name)
        self.emp_list.append(self.age)
        self.emp_list.append(self.email)
        self.emp_list.append(self.location)
        self.emp_list.append(self.salary)

    def table_emp(self):
        print(tabulate([["First_name", "Last_name", "Age", "Email", "Loaction", "Salary"], self.emp_list],
                       headers="firstrow"))


emp1=Employee("Arun","kumar",23,"chennai",22000)
emp2=Employee("surya","ganesh",23,"chennai",25000)
emp3=Employee("santhosh","kumar",24,"madurai",25000)

emp1.del_emp()
emp2.del_emp()
emp3.del_emp()

emp1.table_emp()
emp2.table_emp()
emp3.table_emp()
"""

#update code
from tabulate import tabulate
import time

#from datetime import datetime

start=time.time()

class Employee:
    
    def __init__(self,first_name,last_name,age,location,salary):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.email=first_name+"."+last_name+"@xyz.com"
        self.location=location
        self.salary=salary
        self.emp_list=[]
    
    #created email for emplyee    
    def getemail(self):
        return self.email
    
    #display table form created emp_details
    def del_emp(self):
        self.emp_list.append(self.first_name)
        self.emp_list.append(self.last_name)
        self.emp_list.append(self.age)
        self.emp_list.append(self.email)
        self.emp_list.append(self.location)
        self.emp_list.append(self.salary)
        
    def table_emp(self):
        print(tabulate([["First_name","Last_name","Age","Email","Loaction","Salary"],self.emp_list],headers="firstrow"))
        
emp1=Employee("john","son",23,"chennai",22000)
emp1.del_emp()
time_check=emp1.table_emp()

#(c) Calculate the time used for execution of this program
end=time.time()
print("\nTime of execution of above program is:",end-start)


#(d) Read about the significance of self parameter 

"""
self-self keyword is special refernce to a particular object from with in the object itself and also member function of current
object it also represent the instance of the class it binds the attribute with the given arguments.
"""
