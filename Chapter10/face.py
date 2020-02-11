from Chapter10.FaceExpressions import *
from Button import *

def main():
    win = GraphWin("FaceExpressions", 600, 600)
    win.setBackground("white")

    #create the normal button and enable it for clicking
    normal = Button(win, Point(100, 500), 100, 50, "Normal")
    normal.disable()

    #create the surprised button and enable it for clicking
    surprised = Button(win, Point(300, 500), 100, 50, "Surprised")
    surprised.enable()

    #create the quit button and enable it for clicking
    quit = Button(win, Point(500, 500), 100, 50, "Quit")
    quit.enable()

    #Draw the face
    face = FaceExpressions(Point(300, 250), 200, win)
    face.normalFace()

    #see which button is clicked
    click = win.getMouse()
    while not quit.clicked(click):
        if normal.clicked(click):
            face.normalFace()
            normal.disable()
            surprised.enable()
        elif surprised.clicked(click):
            face.surprisedFace()
            surprised.disable()
            normal.enable()
        else:
            click = win.getMouse()


if __name__ == "__main__":
    main()