from utils import minMatrix, maxMatrix, intersection, findPivot
from DDA_line import DDALine
from pixel import setPixel
from DDA_line import DDALine
from colors import BLACK

class Polygon :
    def __init__(self, img, points, borderColor, backgroundColor):
        self.borderColor = borderColor
        self.backgroundColor = backgroundColor
        self.points = points

        self.createPolygon(img, borderColor)
        self.fill(img, backgroundColor)
        
    def deletePolygon(self, img):
        self.createPolygon(img, BLACK)
        self.fill(img, BLACK)

    def createPolygon(self, img, color):
        x = self.points[0][0]
        y = self.points[0][1]

        for i in range(1, len(self.points)):
            xf = self.points[i][0]
            yf = self.points[i][1]

            DDALine(img, (x, y), (xf, yf), color)

            x = self.points[i][0]
            y = self.points[i][1]
        
        DDALine(img, (x, y), (self.points[0][0], self.points[0][1]), color)

    def getPoints(self):
        return self.points

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

    # scale
    def scale(self, img, sx, sy):
        pivot = findPivot(self.points)

        # move to 0 position
        self.move(img, -pivot[0], -pivot[1])

        # apply scale
        new_points = []

        for p in self.points:
            new_points.append([p[0] * sx, p[1] * sy])

        self.deletePolygon(img)

        self.points = new_points

        self.createPolygon(img, self.borderColor)
        self.fill(img, self.backgroundColor)

        #  return to initial position
        self.move(img, pivot[0], pivot[1])

    # translation
    def move(self, img, x, y):
        new_points = []

        for p in self.points:
            new_points.append([p[0] + x, p[1] + y])

        self.deletePolygon(img)

        self.points = new_points

        self.createPolygon(img, self.borderColor)
        self.fill(img, self.backgroundColor)
