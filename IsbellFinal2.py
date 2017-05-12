import math as m


def triangle(a, b):
    """
    The Pythagorean equation for a right triangle is a^2 + b^2 = c^2 , where c is the hypotenuse 
    while a and b are the remaining sides. Calculate all values for right triangles when the sides
    are no greater than 20. The program will ask for side a, side b and then return the hypotenuse.
    """

    if (a <= 20) & (b <= 20):
        c = (a * a) + (b * b)
        c = m.sqrt(c)
        print("The hypotenuse is %.2f" % c)

    else:
        print("The sides must be less than 20. Please try again.")
        a = int(input("Please enter side a: "))
        b = int(input("Please enter side b: "))
        triangle(a, b)

var = input("Would you like to view the help documentation? Enter y/n: ")

if var == 'y':
    help(triangle)

side_a = int(input("Please enter side a: "))
side_b = int(input("Please enter side b: "))

triangle(side_a, side_b)
