#Alex Harris
#CS160 9am

from graphics import *

def main():
    #Create the window
    win = GraphWin("tennis.py", 400, 200)
    #make the background black
    win.setBackground("black")
    #unit conversion
    win.setCoords(0, 0, 120, 60)
    #make green rectangles with white outlines
    outBoundOne = Rectangle(Point(21, 12), Point(99, 16.5))
    outBoundOne.setOutline("white")
    outBoundOne.setFill("green")
    outBoundOne.draw(win)
    outBoundTwo = Rectangle(Point(21, 43.5), Point(99, 48))
    outBoundTwo.setOutline("white")
    outBoundTwo.setFill("green")
    outBoundTwo.draw(win)
    serviceLineOne = Rectangle(Point(21, 16.5), Point(39, 43.5))
    serviceLineOne.setOutline("white")
    serviceLineOne.setFill("green")
    serviceLineOne.draw(win)
    serviceLineTwo = Rectangle(Point(81, 16.5), Point(99, 43.5))
    serviceLineTwo.setOutline("white")
    serviceLineTwo.setFill("green")
    serviceLineTwo.draw(win)
    centerServiceLineOne = Rectangle(Point(39, 16.5), Point(81, 30))
    centerServiceLineOne.setOutline("white")
    centerServiceLineOne.setFill("green")
    centerServiceLineOne.draw(win)
    centerServiceLineTwo = Rectangle(Point(39, 30), Point(81, 43.5))
    centerServiceLineTwo.setOutline("white")
    centerServiceLineTwo.setFill("green")
    centerServiceLineTwo.draw(win)
    #create the net line and make it white
    net = Line(Point(60.5, 12), Point(60.5, 48))
    net.setFill("white")
    net.draw(win)
    #keep the window open
    win.getMouse()
    #close the window after the click
    win.close()

main()