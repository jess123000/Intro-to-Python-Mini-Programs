#Alex Harris
#CS160 9am

from graphics import *

def drawSquare(win, center, length):

    center.draw(win)
    square = Rectangle(Point(center.getX() - length, center.getY() - length), Point(center.getX() + length, center.getY() + length))
    square.draw(win)

def main():
    # Create the window
    win = GraphWin("squares.py", 400, 400)

    # Get where the user wants the center to be
    center = win.getMouse()

    #set the length of the square
    halfLength = 50

    # Create and draw the square around the users selected center
    drawSquare(win, center, halfLength)
    center = win.getMouse()
    drawSquare(win, center, halfLength)

    # Close the window on click
    win.getMouse()
    win.close()

main()