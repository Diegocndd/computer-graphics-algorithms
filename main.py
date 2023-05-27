import pygame
import time
from pixel import setPixel, getPixel
from bresenham_line import bresenhamLine
from bresenham_circle import bresenhamCircle
from bresenham_ellipse import bresenhamEllipse
from utils import loadTexture
from flood_fill import floodFill
from DDA_line import DDALine
from polygon import Polygon
from constants import WIDTH_SCREEN, HEIGHT_SCREEN
from colors import *

def cleanScreen(img):
    for i in range(0, WIDTH_SCREEN):
        for j in range(0, HEIGHT_SCREEN):
            setPixel(img=img, x=i, y=j, color=BLACK)

def initScreen(img):
    halfHeight = round(HEIGHT_SCREEN / 2)
    halfWidth = round(WIDTH_SCREEN / 2)
    bresenhamEllipse(img, (halfWidth, halfHeight), 200, 100, RED)
    bresenhamCircle(img, (halfWidth, halfHeight), 200, RED)
    floodFill(img, (halfWidth, halfHeight + 2), BLACK, BLUE)
    floodFill(img, (halfWidth, round(halfHeight - halfHeight / 2)), BLACK, RED)
    floodFill(img, (halfWidth, round(halfHeight + halfHeight / 2)), BLACK, RED)

def drawLetter(img, letter, point, size = 1, fontColor = WHITE):
    x, y = point
    if letter == 'B':
        height = 6

        for i in range(height):
            setPixel(img, x, y - i, fontColor)
        setPixel(img, x + 1, y, fontColor)
        setPixel(img, x + 2, y, fontColor)

        setPixel(img, x + 1, y - 3, fontColor)
        setPixel(img, x + 2, y - 3, fontColor)

        setPixel(img, x + 1, y - 3, fontColor)
        setPixel(img, x + 2, y - 3, fontColor)

        setPixel(img, x + 4, y - 1, fontColor)
        setPixel(img, x + 4, y - 2, fontColor)

        setPixel(img, x + 4, y - 4, fontColor)
        setPixel(img, x + 4, y - 5, fontColor)

        setPixel(img, x + 1, y - 6, fontColor)
        setPixel(img, x + 2, y - 6, fontColor)


def main():
    #TODO: consertar escala em números racionais

    pygame.init()
    pygame.display.set_caption('AP1')
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    
    # p = Polygon(img=screen, points=[[70, 70, 0, 0], [200, 70, 1, 0], [200, 200, 1, 1], [70, 200, 0, 1]], borderColor=GREEN, texture=loadTexture('cat.jpeg'))

    # initScreen(screen)
    drawLetter(screen, 'B', (100, 100), size=3, fontColor=RED)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p.move(screen, -4, 0)
                if event.key == pygame.K_RIGHT:
                    p.move(screen, 4, 0)
                if event.key == pygame.K_UP:
                    p.move(screen, 0, -4)
                if event.key == pygame.K_DOWN:
                    p.move(screen, 0, 4)
        pygame.display.update()
     
if __name__=="__main__":
    main()