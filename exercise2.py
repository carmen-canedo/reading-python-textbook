# exercise2.py
#   A program to calculate the cost per in^2 of a pizza

import math

def main():

    # Prompting user for diamter
    diameter = float(input("Enter diameter: "))

    # Converting to radius
    radius = diameter / 2

    # Prompting user for price
    cost = float(input("Price of pizza: "))

    # Calculating area
    area = math.pi * radius ** 2

    # Dividing cost by area
    c_per_in = cost / area

    # Rounding to two decimal places
    c_per_in = round(c_per_in, 2)

    # Printing result
    print("Your pizza costs $" + str(c_per_in) + " per square inch!")

if __name__ == '__main__':
    main()
