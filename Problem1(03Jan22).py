"""
Problem 1: OOP
Create a vehicle class with attributes - company name, vehicle name, capacity, cc, mileage, manufacturing year
Inherit vehicle class and create classes bus, car, van, bike, scooter
Create methods to set and get various attributes.
Add any specific new attributes to the inherited classes
Create relevant objects for each class, and display their attributes.
"""


# Create a vehicle class with attributes - company name, vehicle name, capacity, cc, mileage, manufacturing year
class Vehicle:

    def __init__(self, company_name, vehicle_name, mileage, manufacturing_year):
        self.company_name = company_name
        self.vehicle_name = vehicle_name
        self.mileage = mileage
        self.manufacturing_year = manufacturing_year

    # Create methods to set and get various attributes.
    def get_company_name(self):
        return self.company_name

    def set_company_name(self, company_name):
        self.company_name = company_name

    def get_manufacturing_year(self):
        return self.manufacturing_year

    def set_manufacturing_year(self, manufacturing_year):
        self.manufacturing_year = manufacturing_year

    def get_attributes(self):
        return self.__dict__


# Inherit vehicle class and create classes bus, car, van, bike, scooter
# Add any specific new attributes to the inherited classes
class Bus(Vehicle):
    def __init__(self, company_name, vehicle_name, mileage, manufacturing_year, seating_capacity):
        Vehicle.__init__(self, company_name, vehicle_name, mileage, manufacturing_year)
        self.seating_capacity = seating_capacity


class Car(Vehicle):
    def __init__(self, company_name, vehicle_name, mileage, manufacturing_year, seating_capacity):
        Vehicle.__init__(self, company_name, vehicle_name, mileage, manufacturing_year)
        self.seating_capacity = seating_capacity


class Van(Vehicle):
    def __init__(self, company_name, vehicle_name, mileage, manufacturing_year, seating_capacity):
        Vehicle.__init__(self, company_name, vehicle_name, mileage, manufacturing_year)
        self.seating_capacity = seating_capacity


class Bike(Vehicle):
    def __init__(self, company_name, vehicle_name, mileage, manufacturing_year, cc):
        Vehicle.__init__(self, company_name, vehicle_name, mileage, manufacturing_year)
        self.cc = cc


class Scooter(Vehicle):
    def __init__(self, company_name, vehicle_name, mileage, manufacturing_year, cc):
        super().__init__(company_name, vehicle_name, mileage, manufacturing_year)
        self.cc = cc


#Create relevant objects for each class, and display their attributes.
v1=Bus("volvo","Bus",4.5,2010,55)
v2=Car("Skoda","Car",22,2015,5)
v3=Bike("yamaha","R15",40,2011,150)
v4=Van("Maruti","Omni",35,2010,20)
v5=Scooter("Honda","Activa",40,2020,120)



print(v5.get_attributes())
print(v4.get_attributes())

print(v3.get_company_name())
v3.set_company_name("Royal Enfield")
print(v3.get_attributes())