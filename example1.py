# cball3.py in textbook
#   Program using cannonball to demonstrate class
#
#  Needs:
#  - A class to represent projectiles
#  - Constructor to initialize instance variables
#  - `update` method to change the state of the projectile
#  - `get_x` and `get_y` methods to find current position

import math

class Projectile:

    # Initializing class
    def __init__(self, angle, velocity, height):

        # Identifying current position
        self.xpos = 0.0
        self.ypos = height

        # Converting angle to radians
        theta = math.radians(angle)

        # Calculating velocity
        self.xvel = velocity * math.cos(theta)
        self.yvel = velocity * math.sin(theta)

    # Methods
    # Return current position
    def get_x(self):

        return self.xpos

    def get_y(self):
        return self.ypos

    # Updates the state of projectile over time
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

# Prompting user for values
def get_inputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (m/s): "))
    h = float(input("Enter the initial height (m): "))
    t = float(input("Enter the time interval b/n position calculations: "))
    return a, v, h, t

# Calling main function
def main():

    angle, vel, h0, time = get_inputs()
    cball = Projectile(angle, vel, h0)

    while (cball.get_y() >= 0):
        cball.update(time)

    print("\nDistance traveled: {0:0.1f} meters.".format(cball.get_x()))

if __name__ == '__main__':
    main()
