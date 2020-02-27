# exercise3
#   A program to compute the molecular weight of a carbohydrate
#   Measured in grams per mole
#
#   Ask for number of hydrogen atoms
#   Ask for number of carbon atoms
#   Ask for number of oxygen atoms
#   Print the total combined molecular weight of all atoms
#
#   H: 1.00794
#   C: 12.0107
#   O: 15.9994
#   General formula for carbohydrate: CH20

def main():
    # Prompting user for count molecules
    hydrogen = int(input("Enter number of hydrogren atoms: "))
    carbon = int(input("Enter number of carbon atoms: "))
    oxygen = int(input("Enter number of oxygen atoms: "))

    # Accounting for individual weights
    h = 1.00794
    c = 12.00107
    o = 15.9994

    # Printing total molecular weight of individual atoms
    total_weight = h + c + o
    total_weight = round(total_weight, 2)
    print("The total combined molecular weight is: ", total_weight, "grams/mole.")

    # Calculating the molecular weight of a carbohydrate
    mol_weight = 2 * (hydrogen * h) + (carbon * c) + (oxygen * o)

    # Printing result
    mol_weight = round(mol_weight, 2)
    print("The molecular weight of the carbohydrate is: ", mol_weight, "grams/mole.")

if __name__ == '__main__':
    main()
