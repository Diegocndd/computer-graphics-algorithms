import pygame
import time
from pixel import setPixel, getPixel
from bresenham_line import bresenhamLine
from bresenham_circle import bresenhamCircle
from bresenham_ellipse import bresenhamEllipse
from flood_fill import floodFill
from polygon import Polygon
from constants import WIDTH_SCREEN, HEIGHT_SCREEN
from colors import *

def cleanScreen(img):
    for i in range(0, WIDTH_SCREEN):
        for j in range(0, HEIGHT_SCREEN):
            setPixel(img=img, x=i, y=j, color=BLACK)

def main():
    #TODO: consertar escala em números racionais

    pygame.init()
    pygame.display.set_caption('AP1')
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

    # p = Polygon(img=screen, points=[[1, 1], [10, 1], [10, 10], [1, 10]], backgroundColor=RED, borderColor=GREEN)

    # p = Polygon(img=screen, points=[[50, 50], [100, 50], [100, 100], [50, 100]], backgroundColor=RED, borderColor=GREEN)
    p = Polygon(img=screen, points=[[40, 40], [60, 40], [60, 60], [40, 60]], backgroundColor=RED, borderColor=GREEN)
    # p = Polygon(img=screen, points=[[6, 13], [13, 6], [6, 13], [13, 6]], backgroundColor=RED, borderColor=BLUE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p.move(screen, -1, 0)
                if event.key == pygame.K_RIGHT:
                    p.move(screen, 1, 0)
                if event.key == pygame.K_UP:
                    p.move(screen, 0, -1)
                if event.key == pygame.K_DOWN:
                    p.move(screen, 0, 1)
                if event.key == pygame.K_SPACE:
                    p.scale(screen, 2, 2)
                if event.key == pygame.K_a:
                    # p.move(screen, -40, -40)

                    p.rotate(screen, 20)

        # p.rotate(screen, 1)
        # time.sleep(0.5)
        pygame.display.update()
     
if __name__=="__main__":
    main()