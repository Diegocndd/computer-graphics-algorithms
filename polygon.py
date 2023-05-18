from bresenham_line import bresenhamLine

class Polygon :
    def __init__(self):
        self.points = []
    
    def insertPoint(self, x, y):
        self.points.append([x, y])
    
    def createPolygon(self, img, color):
        x = self.points[0][0]
        y = self.points[0][1]

        for i in range(1, len(self.points)):
            xf = self.points[i][0]
            yf = self.points[i][1]

            bresenhamLine(img, (x, y), (xf, yf), color)

            x = self.points[i][0]
            y = self.points[i][1]
        
        print((x, y), (self.points[0][0], self.points[0][1]))

        bresenhamLine(img, (x, y), (self.points[0][0], self.points[0][1]), color)
