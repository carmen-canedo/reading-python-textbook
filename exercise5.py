# exercise5.py
#   Program to calculate the cost of an order at a coffee shop
#
#   coffee = 10.50(pound) + cost of shipping
#   cost of shipping = 0.86(pound) + 1.50

# Calling main function
def main():

    # Prompting user to enter pounds needed
    pounds = int(input("Enter the whole number of pounds needed: "))

    # Calculating cost of shipping
    shipping_cost = 0.86 * pounds + 1.50

    # Calculating total cost
    order_cost = 10.50 * pounds + shipping_cost

    # Printing result
    print("The total cost is $" + str(order_cost))


if __name__ == '__main__':
    main()
