from polygon import Polygon

class Enemy(Polygon):
    def __init__(self, img, points, borderColor, backgroundColor):
        super().__init__(img=img, points=points, borderColor=borderColor, backgroundColor=backgroundColor)

        self.borderColor = borderColor
        self.backgroundColor = backgroundColor
        self.points = points

        self.updatePolygon(img)
        self.autoMoveCount = 0
    
    # min = 1
    # max = 100
    def autoMove(self, img, velocity):
        if 100 - velocity == self.autoMoveCount:
            self.move(img, 0, 2)
            self.autoMoveCount = 0
        self.autoMoveCount += 1