from utils import minMatrix, maxMatrix, intersection
from DDA_line import DDALine
from pixel import setPixel
from DDA_line import DDALine

class Polygon :
    def __init__(self):
        self.points = []
    
    def getPoints(self):
        return self.points

    def insertPoint(self, x, y):
        self.points.append([x, y])
    
    def createPolygon(self, img, color):
        x = self.points[0][0]
        y = self.points[0][1]

        for i in range(1, len(self.points)):
            xf = self.points[i][0]
            yf = self.points[i][1]

            DDALine(img, (x, y), (xf, yf), color)

            x = self.points[i][0]
            y = self.points[i][1]
        
        # print((x, y), (self.points[0][0], self.points[0][1]))

        DDALine(img, (x, y), (self.points[0][0], self.points[0][1]), color)

    # scanline
    def fill(self, img, color):
        polygon = self.points
        yMin = minMatrix(polygon)[1]
        yMax = maxMatrix(polygon)[1]

        for y in range(yMin, yMax):
            # lista de interseções
            i = []

            piX = polygon[0][0]
            piY = polygon[0][1]

            for p in range(1, len(polygon)):
                pfX = polygon[p][0]
                pfY = polygon[p][1]

                # acha o x da interseção da scanline com o segmento
                xi = round(intersection(y, [[piX, piY], [pfX, pfY]]))
                
                if xi >= 0:
                    i.append(xi)
                
                piX = pfX
                piY = pfY
            
            # aresta que fecha o polígono
            pfX = polygon[0][0]
            pfY = polygon[0][1]

            xi = round(intersection(y, [[piX, piY], [pfX, pfY]]))

            if xi >= 0:
                i.append(xi)
            
            if len(i) > 0:
                for pi in range(0, len(i), 2):
                    for pixel in range(i[pi], i[pi + 1], -1):
                        setPixel(img, pixel, y, color)
