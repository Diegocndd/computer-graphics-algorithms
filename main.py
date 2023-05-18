import pygame
from pixel import setPixel, getPixel
from bresenham_line import bresenhamLine
from bresenham_circle import bresenhamCircle
from bresenham_ellipse import bresenhamEllipse
from flood_fill import floodFill
from polygon import Polygon
from constants import WIDTH_SCREEN, HEIGHT_SCREEN
from colors import *
from DDA_line import DDALine
def main():
    pygame.init()
    pygame.display.set_caption('Set Pixel')
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

    p = Polygon()
    p.insertPoint(50, 100)
    p.insertPoint(100, 50)
    p.insertPoint(150, 100)
    p.insertPoint(120, 150)
    p.insertPoint(80, 150)

    p.createPolygon(screen, ORANGE)

    floodFill(screen, (70, 100), BLACK, RED)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
     
if __name__=="__main__":
    main()