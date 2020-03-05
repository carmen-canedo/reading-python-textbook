# animation.py
# Creates a graphic window to display the cannonball
import graphics

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
