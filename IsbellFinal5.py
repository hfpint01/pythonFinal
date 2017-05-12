"""
Based on the chosen input method, this program will calculate the length and width of a rectangle.
If you'd like to enter corner points, enter option 1 followed by the top left point and bottom right point.
If you'd like to enter length and width, enter option 2 followed by the length and width. 
"""
import math as m

class Rectangle:
    def __init__(self, option):
        self.option = option
        if self.option == '1':
            a_tup = tuple(map(float, input("Enter top left coordinates: ").split(',')))
            b_tup = tuple(map(float, input("Enter bottom right coordinates: ").split(',')))

            length = b_tup[0]-a_tup[0]
            width = a_tup[1]-a_tup[0]
            area = length * width
            perimeter = 2*(length + width)

            print("The rectangle length is %.2f" % length)
            print("The rectangle width(height) is %.2f" % width)
            print("The area of the rectangle is %.2f" % area)
            print("The perimeter of the rectangle is %.2f" % perimeter)

            if length == width:
                print("This is a square.")

        if self.option == '2':
            width = float(input("Enter the width(height): "))
            length = float(input("Enter the length: "))

            area = length * width
            perimeter = 2 * (length + width)
            print("The area of the rectangle is: %.2f" % area)
            print("The perimeter of the rectangle is %.2f" % perimeter)

            if length == width:
                print("This is a square.")




opt = input("Would you like to calculate the perimeter and area of a rectangle based on:\n"
               "1. coordinates of top left and bottom right corner \n"
               "----or----\n"
               "2. length and width? ")

newRectangle = Rectangle (opt)