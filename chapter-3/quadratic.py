# quadratic.py
#   A program that computes the real roots of a quadratic equation
#   Illustrates use of the math library.
#   Note: this program crashes if the equaiton has no real roots.

import math  # Makes the math library available

# Calling main function


def main():

    # Printing the purpose of program
    print("This program finds the real solutions to a quadratic.")

    # Adding extra line
    print()

    # Prompting user to enter values
    a = float(input("Enter coefficent a: "))
    b = float(input("Enter coefficent b: "))
    c = float(input("Enter coefficent c: "))

    # Calculating the root
    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    # Adding blank line
    print()

    # Printing solutions
    print("The solutions are: ", root1, "and", root2)


if __name__ == '__main__':
    main()
