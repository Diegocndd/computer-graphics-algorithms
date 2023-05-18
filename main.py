import pygame
from pixel import setPixel, getPixel
from bresenham_line import bresenhamLine
from bresenham_circle import bresenhamCircle
from bresenham_ellipse import bresenhamEllipse
from flood_fill import floodFill
from polygon import Polygon
from constants import WIDTH_SCREEN, HEIGHT_SCREEN
from colors import *

def main():
    pygame.init()
    pygame.display.set_caption('Set Pixel')
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    # bresenhamLine(screen, (100, 120), (200, 220), GREEN)

    # bresenhamLine(screen, (100, 100), (200, 100), GREEN)
    # bresenhamLine(screen, (200, 100), (200, 200), GREEN)
    # bresenhamLine(screen, (200, 200), (100, 200), GREEN)
    # bresenhamLine(screen, (100, 200), (100, 100), GREEN)

    # floodFill(screen, (140, 189), BLACK, RED)

    # bresenhamLine(screen, (50, 200), (100, 100), YELLOW)
    # bresenhamLine(screen, (100, 100), (50, 200), YELLOW)
    # bresenhamLine(screen, (200, 100), (20, 30), YELLOW)

    # bresenhamLine(screen,  (20, 30),(200, 100), YELLOW)

    p = Polygon()
    p.insertPoint(100, 100)
    p.insertPoint(250, 100)
    p.insertPoint(250, 250)
    p.insertPoint(100, 250)
    p.createPolygon(screen, ORANGE)

    floodFill(screen, (140, 180), BLACK, RED)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
     
if __name__=="__main__":
    main()