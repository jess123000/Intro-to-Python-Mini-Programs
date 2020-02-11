#Alex Harris
#CS160 9am

from graphics import *

def main():
    #Create the window
    win = GraphWin("circleSquare.py", 400, 400)

    #Get where the user wants the center to be
    center = win.getMouse()

    #Show the user where they clicked is in the middle
    center.draw(win)

    #Create and draw the square around the users selected center
    square = Rectangle(Point(center.getX() - 75, center.getY() - 75), Point(center.getX() + 75, center.getY() + 75))
    square.draw(win)
    circle = Circle(center, 75)
    circle.draw(win)

    #Close the window on click
    win.getMouse()
    win.close()

main()