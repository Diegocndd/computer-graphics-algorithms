import math
from utils import minMatrix, maxMatrix, intersection, getPixelFromTexture, oldintersection
from DDA_line import DDALine
from pixel import setPixel
from DDA_line import DDALine
from colors import BLACK

class Polygon :
    def __init__(self, img, points, borderColor, backgroundColor = None, texture = None):
        self.borderColor = borderColor
        self.points = points
        self.texture = texture
        self.backgroundColor = backgroundColor

        if texture:
            self.fillTexture(img, texture)
        elif backgroundColor:
            self.fill(img, backgroundColor)

        self.updatePolygon(img)

    def verifyCollision(self, p):
        points = self.getPoints()
        p_points = p.getPoints()

        p_alpha = p_points[0][0]
        p_betha = p_points[0][1]
        p_delta = p_points[2][1]
        p_gama = p_points[2][0]

        alpha = points[0][0]
        betha = points[0][1]
        delta = points[2][1]
        gama = points[2][0]

        y_collision = (betha > p_betha and betha < p_delta) or (delta > p_betha and delta < p_delta)
        x_collision = (alpha < p_gama and alpha > p_alpha) or (gama < p_gama and gama > p_alpha)
        return x_collision and y_collision
            
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

    def fillTexture(self, img, tex):
        polygon = self.points
        yMin = minMatrix(polygon)[1]
        yMax = maxMatrix(polygon)[1]

        for y in range(yMin, yMax):
            # lista de interseções
            i = []

            pi = polygon[0]

            for p in range(1, len(polygon)):
                pf = polygon[p]
                pInt = intersection(y, [pi, pf])
                            
                if pInt[0] >= 0:
                    i.append(pInt)
                
                pi = pf
            
            pf = polygon[0]

            pInt = intersection(y, [pi, pf])

            if pInt[0] >= 0:
                i.append(pInt)

            if len(i) > 0:
                for pi in range(0, len(i), 2):
                    for pixel in range(i[pi][0] - 1, i[pi + 1][0], -1):
                        p1 = i[pi]
                        p2 = i[pi + 1]

                        pc = (pixel - p1[0]) / (p2[0] - p1[0])
                        tx = p1[2] + pc *(p2[2] - p1[2])
                        ty = p1[3] + pc *(p2[3] - p1[3])

                        color = getPixelFromTexture(texture=tex, x=tx, y=ty)

                        setPixel(img, pixel, y, color)

    # scanline
    def fill(self, img, color):
        polygon = self.points
        yMin = minMatrix(polygon)[1]
        yMax = maxMatrix(polygon)[1]

        for y in range(yMin, yMax):
            # lista de interseções
            i = []

            pi = polygon[0]

            piX = polygon[0][0]
            piY = polygon[0][1]

            for p in range(1, len(polygon)):
                pf = polygon[p]

                # acha o x da interseção da scanline com o segmento
                pInt = intersection(y, [pi, pf])
                
                if pInt[0] >= 0:
                    i.append(pInt)
                
                pi = pf
            
            # aresta que fecha o polígono
            pf = polygon[0]

            pInt = intersection(y, [pi, pf])
                
            if pInt[0] >= 0:
                i.append(pInt)
            
            if len(i) > 0:
                for pi in range(0, len(i), 2):
                    for pixel in range(i[pi][0] - 1, i[pi + 1][0], -1):
                        setPixel(img, pixel, y, color)

    def scale(self, img, sx, sy):
        self.deletePolygon(img)
        self.calculateScale(img, sx, sy)
        self.updatePolygon(img)

    # scale
    def calculateScale(self, img, sx, sy):
        # TODO: remover mock de 50
        self.calculateMove(img, -50, -50)

        # apply scale
        new_points = []

        for p in self.points:
            new_points.append([p[0] * sx, p[1] * sy, p[2], p[3]])

        self.points = new_points
        self.calculateMove(img, +50, +50)

    def updatePolygon(self, img):
        self.createPolygon(img, self.borderColor)

        if (self.texture):
            self.fillTexture(img, self.texture)
        elif (self.backgroundColor):
            self.fill(img, self.backgroundColor)

    # rotation
    def rotate(self, img, angle):
        self.deletePolygon(img)
        self.calculateRotation(img, angle)
        self.updatePolygon(img)

    def calculateRotation(self, img, angle):
        # TODO: remover mock de 50
        self.calculateMove(img, -50, -50)

        new_points = []
        angle = math.radians(angle)

        for p in self.points:
            x2 = (round((p[0] * math.cos(angle)) - (p[1] * math.sin(angle))))
            y2 = (round((p[0] * math.sin(angle)) + (p[1] * math.cos(angle))))
            new_points.append([x2, y2, p[2], p[3]])

        self.points = new_points

        self.calculateMove(img, +50, +50)

    def move(self, img, x, y):
        self.deletePolygon(img)
        self.calculateMove(img, x, y)
        self.updatePolygon(img)

    # translation
    def calculateMove(self, img, x, y):
        new_points = []

        for p in self.points:
            new_points.append([p[0] + x, p[1] + y, p[2], p[3]])

        self.points = new_points