### Homework 7: Object-Oriented Programming (OOP) in Python
## In this homework we will create a superclass Rectangle and subclass Square

### Problem 1: Define a class called Rectangle that contains:
# attributes height and width 
# methods area() and perimeter() 

class Rectangle:
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def area(self):
		return f"The area is {self.height * self.width}"   

	def perimeter(self):
		return f"The perimeter is {2 * self.height + 2 * self.width}"

## Use case: Create an instance of the Rectangular class and call the area and perimeter methods to verify that they work correctly.
my_rectangle = Rectangle(11, 2)
print(my_rectangle.area())
print(my_rectangle.perimeter())


### Problem 2: Define a subclass called Square that 
# inherits from parent class Rectangle
# Using super(), will set .height and .width attributes from inherited superclass Rectangle.__init__()
class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)
		self.side = side
 
 
## Use case: Create an instance of the Square class and call the area and perimeter methods to verify that they work correctly.
my_square = Square(9)
print(my_square.area())
print(my_square.perimeter())	

### Problem 3: Create a new class Cube that inherits from parent class Square
# Use super() to set .height and .width attributes from inherited superclass Square.__init__()
# Define new methods surface_area() and volume() that calculate the surface area and volume of the cube using the inherited attribute 

class Cube(Square):
	def __init__(self, side):
		super().__init__(side)

	def surface_area(self):
		return f"The surface area is {6 * self.height**2}"

	def volume(self):
		return f"The volume is {self.height**3}"

## Use case: Create an instance of the Cube class and call the surface_area and volume methods to verify that they work correctly.
my_cube = Cube(4)
print(my_cube.surface_area())
print(my_cube.volume())

