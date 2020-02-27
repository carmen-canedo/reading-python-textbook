# exercise1.py
#   Program to calculate the volume and surface area of a sphere
#   Illustrates use of pi from math module

import math

def main():

    # Rounding pi to 2 decimal places
    pi = round(math.pi, 2)

    # Prompting user to input radius
    radius = float(input("Enter a radius: "))

    # Rounding radius to two decimals
    radius = round(radius, 2)

    # Calculating and rounding volume
    volume = 4 / 3 * pi * radius ** 2
    volume = round(volume, 2)

    # Calculating and rounding surface area
    surface_area = 4 * pi * radius ** 2
    surface_area = round(surface_area, 2)

    # Printing results
    print("Volume: ", volume)
    print("Surface Area:", surface_area)


if __name__ == '__main__':
    main()
