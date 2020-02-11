from __future__ import annotations
from graphics import *

class FaceExpressions:

    #initialize all the face parts
    def __init__(self, center: Point, radius: float, win: GraphWin):
        """
        :param center: Where the center of the face is
        :param radius: the radius of the face
        :param win: the window in which to draw the face
        """
        self.center = center
        self.radius = radius
        self.win = win
        self.bigCirc = Circle(self.center, self.radius)
        self.bigCirc.draw(self.win)
        self.bigCirc.setWidth(3)
        self.eyesApartX = self.center.getX() / 10
        self.eyesApartY = self.center.getX() / 10
        self.eye1 = Circle(Point(self.eyesApartX * 7, self.eyesApartY * 6), 10)
        self.eye1.setWidth(2)
        self.eye1.draw(self.win)
        self.eye2 = Circle(Point(self.eyesApartX * 13, self.eyesApartY * 6), 10)
        self.eye2.setWidth(2)
        self.eye2.draw(self.win)
        self.mouthApartX = self.center.getX() / 10
        self.mouthApartY = self.center.getY() / 20
        self.mouthNormal = Rectangle(Point(self.mouthApartX * 6, self.mouthApartY * 27), Point(self.mouthApartX * 14, self.mouthApartY * 27))
        self.mouthNormal.draw(self.win)
        self.eye3 = Circle(Point(self.eyesApartX * 7, self.eyesApartY * 6), 30)
        self.eye3.setWidth(2)
        self.eye3.draw(self.win)
        self.eye4 = Circle(Point(self.eyesApartX * 13, self.eyesApartY * 6), 30)
        self.eye4.setWidth(2)
        self.eye4.draw(self.win)
        self.mouthCenterX = self.center.getX() / 10
        self.mouthCenterY = self.center.getY() / 20
        self.mouthSurprised = Oval(Point(self.mouthCenterX * 6, self.mouthCenterY * 25), Point(self.mouthCenterX * 14, self.mouthCenterY * 29))
        self.mouthSurprised.setWidth(2)
        self.mouthSurprised.draw(self.win)

    def normalFace(self):
        #draw the normal face
        self.eye3.setOutline("white")
        self.eye4.setOutline("white")
        self.mouthSurprised.setOutline("white")
        self.mouthNormal.setOutline("black")

    def surprisedFace(self):
        #draw the surprised face
        self.eye3.setOutline("black")
        self.eye4.setOutline("black")
        self.mouthSurprised.setOutline("black")
        self.mouthNormal.setOutline("white")