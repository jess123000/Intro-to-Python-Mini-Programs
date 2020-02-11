from graphics import *

def main():
    win = GraphWin("Day 10", 300, 600)
    circ = Circle(Point(150, 50), 50)
    circ.setFill("red")
    circ.draw(win)

    win.getMouse()
    for i in range(5000):
        circ.move(0, .1)
    win.getMouse()
    win.close()

main()