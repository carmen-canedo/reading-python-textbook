# button.py
import graphics

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, width, height, label):
        "Creates a rectangular button"

        w, h = (width / 2.0), (height / 2.0)
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = (x + w), (x - w)
        self.ymax, self.ymin = (y + h), (y - h)
        p1 = Point(self.xmax, self.ymin)
        p2 = Point(self.xmin, self.xmin)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
