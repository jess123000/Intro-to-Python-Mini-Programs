class Rectangle:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def perimeter(self):
        return self.width * 2 + self.height * 2

    def area(self):
        return self.width * self.height

    def center(self):
        return f"({self.x}, {self.y})"

    def upperLeft(self):
        upperLeftX = self.x - self.width / 2
        upperLeftY = self.y - self.width / 2
        return f"({upperLeftX}, {upperLeftY})"
