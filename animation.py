# animation.py
# Creates a graphic window to display the cannonball
import graphics
from projectile import Projectile

# Creating class ShotTracker
class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot. Angle, velocity,
        and height are initial projectile parameters."""

        self.proj = Projectile(angle, velocity, height)
        self.marker = graphics.Circle(graphics.Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """Move the shot dt seconds farther along its flight"""

        # Update the projectile
        self.proj.update(dt)

        # Move the circle to the new projectile location
        center = self.marker.get_center()
        dx = self.proj.get_x() - center.get_x()
        dy = self.proj.get_y() - center.get_y()
        self.marker.move(dx, dy)

    def get_x(self):
        """ Return the current x coordinate of the shot's center """
        return self.proj.get_x()

    def get_y(self):
        """ Return the current y coordinate of the shot's center """
        return self.proj.get_y()

    def undraw(self):
        """ Undraw the shot """
        self.marker.undraw()

# Calling main function
def main():

    # Creates an animation window
    win = graphics.GraphWin("Projectile Animation", 640, 480, autoflush = False)
    win.setCoords(-10, -10, 210, 155)

    # Drawing a baseline
    graphics.Line(graphics.Point(-10, 0), graphics.Point(210, 0)).draw(win)

    # Draws ticks for every 50 meters
    for i in range(0, 210, 50):
        graphics.Text(graphics.Point(i, -5), str(i)).draw(win)
        graphics.Line(graphics.Point(i, 0), graphics.Point(i, 2)).draw(win)

if __name__ == '__main__':
    main()
