# dieview.py
import graphics

class DieView:
    """DieView is a widget that displays a graphical representation
    of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
            d1 = DieView(myWin, Point(40, 50), 20)
        creates a die cetnered at (40, 50) having sides
        of length 20."""

        # Defining standard values
        self.win = win              # Save this for drawing pips later
        self.background = "white"   # Color of die face
        self.foreground = "black"   # Color of the pips
        self.psize = 0.1 * size     # Radius of each pip
        hsize = size / 2.0          # Half the size of the die
        offset = 0.6 * hsize        # Distance from center to outer pips

        # Create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point((cx - hsize), (cy - hsize))
        p2 = Point((cx + hsize), (cy + hsize))
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)
