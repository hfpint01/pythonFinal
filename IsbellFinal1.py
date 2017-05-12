import math as m


class Circle:
    """
    1. This is a program to request a radius from the user then calculates the diameter,
    circumference and area of a circle.
    """
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        print("The circumference is %.2f" % (2*m.pi*self.radius))

    def area(self):
        print("The area is %.2f" % (m.pi*(self.radius*self.radius)))

    def diameter(self):
        print("The diameter is %.2f" % (2*self.radius))

var = input("Would you like to view the help documentation? Enter y/n: ")

if var == 'y':
    help(Circle)

rad = int(input("Please enter your radius: "))
circle = Circle(rad)
circle.circumference()
circle.area()
circle.diameter()
