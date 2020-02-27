# factorial.py
#   Program to comput the factorial of a number
#   Illustrates for loop with an accumulator


def main():

    # Prompting user to input a number
    number = int(input("Please input a whole number: "))

    # Initializing factorial
    factorial = 1

    # Calculating factorial
    for i in range(number, 1, -1):
        factorial = factorial * number

    # Printing solution
    print("The factorial of", number, "is", factorial)


if __name__ == '__main__':
    main()
