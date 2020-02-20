# exercise6.py
#   Program to calculate the slope of a line
#   slope = (y2 - y1) / (x2 - x1)

# Calling main function
def main():

    # Prompting user to input values
    # Point 1
    x1 = int(input("Enter x value 1: "))
    y1 = int(input("Enter y value 1: "))

    # Point 3
    x2 = int(input("Enter x value 2: "))
    y2 = int(input("Enter y value 2: "))

    # Calculating point
    slope = (y2 - y1) / (x2 - x1)

    # Printing result
    print("The slope is", slope)
    
if __name__ == '__main__':
    main()
