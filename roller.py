# roller.py
# Graphics program to roll a pair of dice.
# Uses custrom widgets Button and Dieview.

import random
import graphics
from button import Button
from dieview import DieView

def main():

    # Creates the application window
    win = graphics.GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    # Draws the interface widgets
    die1 = DieView(win, graphics.Point(3, 7), 2)
    die2 = DieView(win, graphics.Point(7,7), 2)
    rollButton = Button(win, graphics.Point(4, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()
    quitButton = Button(win, graphics.Point(5, 1), 2, 1, "Quit")

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = random.randrange(1, 7)
            die1.setValue(value1)
            value2 = random.randrange(1, 7)
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # Close the window
    win.close()

if __name__ == '__main__':
    main()
