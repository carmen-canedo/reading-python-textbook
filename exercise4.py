# exercise4.py
#   Program to determine the distance to a lightning strike
#   Based on time elapsed between the flash and sound of thunder
#
# velocity of sound = 1100 ft/sec
# 1 mile = 5280 ft
#
# Ask user: "How long did it take to hear the thunder? "
# Calculate: distance = speed_of_sound * elapsed_time
# Convert to miles: distance / 5280

def main():

    # Prompting user to enter time elapsed
    elapsed_time = float(input("How many seconds passed before you heard the thunder? "))

    # Calculating distance
    speed_of_sound = 1100
    distance = speed_of_sound * elapsed_time

    # Converting to miles
    miles = distance / 5280
    miles = round(miles, 2)

    # Printing results
    print("The lightning strikes was", miles, "miles away!")

if __name__ == '__main__':
    main()
