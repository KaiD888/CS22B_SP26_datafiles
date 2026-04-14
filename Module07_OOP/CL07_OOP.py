### This template is for the class demo and exercises covered in M07_Lec12_oop for CS 22B.

class Car:
    ## Initializer method - set up the attributes for Car class
    def __init__

    def get_description(self):
        '''Instance method that returns a string description of the car.'''
    
    
## Instantiate a Car object. Instance attributes 
toyota_camry = Car("Toyota", "Camry", "blue")


## Call our instance method
print(toyota_camry.get_description())


### Child class that inherits from Car
class GasCar(Car):
    def __init__(self, make, model, color, fuel_tank_size):
       
    def get_fuel_tank_info(self):
        '''Instance method that returns a string description of the fuel tank.'''
        
        
class ElectricCar(Car):
    def __init__(self, make, model, color, battery_size):
       
    def get_battery_info(self):
        '''Instance method that returns a string description of the battery.'''
       
       
class HybridCar(Car):
    def __init__(self, make, model, color, fuel_efficiency):
        
    def get_fuel_efficiency_info(self):
        '''Instance method that returns a string description of the fuel efficiency.'''
        
 
### Example usage of child classes
gas_car = GasCar("Ford", "Mustang", "red", 16)
print(gas_car.get_description())


##### Example of superclass and subclass ####
## We will create a class called Circle that has 
# attribute radius
# methods area() and circumference()   

class Circle:
    def __init__():
        
        
    def area():
       
    
    def circumference():
        
    
## Use case: Create an instance of the Circle class and call the area and circumference methods to verify that they work correctly.
my_circle = 
print("Area of the circle:", my_circle.area())


### Now we will create a subclass called Cylinder that inherits from parent class Circle
# Using super(), will set .radius attribute from inherited superclass Circle.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the cylinder using the inherited attribute
class Cylinder():
    def __init__():
        
    def surface_area():
        base_area =   # Area of the circular base
        lateral_area =  # Lateral surface area is circumference of base * height
        total_surface_area =  # SA is 2x base * lateral
   

    def volume(self):
        base_area = # Area of the circular base
        volume =  # Vol is base * height


## Use case: Create an instance of the Cylinder class and call the surface_area and volume methods to verify that they work correctly.
my_cylinder 
print("Surface area of the cylinder:", my_cylinder.surface_area())


### Now we creat a subclass Spheres that inherits from parent class Circle
# Using super(), will set .radius attribute from inherited superclass Circle.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the sphere using the inherited attribute
class Sphere():
    
    def surface_area():
        surface_area =   # SA 4x area 
        

    def volume(self):
        volume =  # Vol is (4/3)*pi*r^3
       
    
## Use case: Create an instance of the Sphere class and call the surface_area and volume methods to verify that they work correctly.
my_sphere = 
