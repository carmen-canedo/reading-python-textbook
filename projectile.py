# projectile.py

"""projectile.py
Provides a simple class for modeling the flight of projectiles."""

import math

class Projectile:

    """Simulates the flight of simple projectiles near the earth's surface,
    ignoring wind resistance. Tracking is done in two dimensions, height (y)
    and distance (x)."""

    def __init__(self, angle, velocity, height):
        """Create a projectile with given launch angle, initial velocity
        and height."""
        self.xpos = 0.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def update(self, time):
        """Update the state of this projectile to move it time seconds
        farther into its flight."""
        self.xpos = self.xpos + time * self.xvel

    def get_y(self):
        "Returns the y position (height) of this projectile."
        return self.ypos

    def get_x(self):
        "Returns the x position (distance) of this projectile."
        return self.xpos

def main():

    # Prints the docstrings for class Projectile
    print(Projectile.__doc__)

    # Shows documentation for module
    help("projectile")

if __name__ == '__main__':
    main()
