class Vehicle:
    wheels = 4  # Class variable

    def __init__(self, make, model, rent):
        self.make = make      # Instance variable
        self.model = model    # Instance variable
        self.rent = rent
    
    def annual_rent(self,amount):
        self.rent = self.rent*amount*12
        return self.rent

    def info(self):
        return f"{self.make} {self.model} has {Vehicle.wheels} wheels and has rent: {self.rent}"

v1 = Vehicle("Honda", "Civic",200)
v2 = Vehicle("Toyota", "Camry",300)

#Before rent
print(v1.info())  # Honda Civic has 4 wheels.
print(v2.info())  # Toyota Camry has 4 wheels.

#After rent has been added

print(v1.annual_rent(10))
print(v1.info()) # Honda Civic has 4 wheels.
print(v2.annual_rent(20))
print(v2.info())  # Toyota Camry has 4 wheels.

#After Class Variable is changed
# Changing class variable via class name
Vehicle.wheels = 6

print(v1.annual_rent(20))
print(v1.info())  # Honda Civic has 6 wheels.
print(v2.info())  # Toyota Camry has 6 wheels.
