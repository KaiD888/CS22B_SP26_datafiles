### Homework 7: Object-Oriented Programming (OOP) in Python
## In this homework we will create a superclass Rectangle and subclass Square

### Problem 1: Define a class called Rectangle that contains:
# attributes height and width 
# methods area() and perimeter() 

class Rectangle:
   

## Use case: Create an instance of the Rectangular class and call the area and perimeter methods to verify that they work correctly.
my_rectangle = 


### Problem 2: Define a subclass called Square that 
# inherits from parent class Rectangle
# Using super(), will set .height and .width attributes from inherited superclass Rectangle.__init__()
class Square(Rectangle):
 
 
## Use case: Create an instance of the Square class and call the area and perimeter methods to verify that they work correctly.
my_square = 

### Problem 3: Create a new class Cube that inherits from parent class Square
# Use super() to set .height and .width attributes from inherited superclass Square.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the cube using the inherited attribute 

class Cube(Square):
   

## Use case: Create an instance of the Cube class and call the surface_area and volume methods to verify that they work correctly.
my_cube = 
