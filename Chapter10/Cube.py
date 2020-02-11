class cube:
    def __init(self, fLC = 'red', fRC = 'blue', tC = 'white', bC = 'yellow', bLC = 'green', bRC = 'orange'):
        for i in range(4):
            self.frontLeftFace[i] = fLC
            self.frontRightFace[i] = fRC
            self.topFace[i] = tC
            self.bottomFace[i] = bC
            self.backLeftFace[i] = bLC
            self.backRightFace[i] = bRC

    def turnBackRight(self):
        pass
        #self.backRightFace[] = [self.backRightFace[3], self.backRightFace[0]. self.backRightFace[1], self.backRightFace[2]]

    def turnBackLeft(self):
        pass

    def turnBottom(self):
        pass

    def shuffle(self):
        pass