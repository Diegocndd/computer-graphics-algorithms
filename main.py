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
from word import typeWord
from colors import *
import math

def cleanScreen(img):
    for i in range(0, WIDTH_SCREEN):
        for j in range(0, HEIGHT_SCREEN):
            setPixel(img=img, x=i, y=j, color=BLACK)

def splashScreen(img):
    halfHeight = round(HEIGHT_SCREEN / 2)
    halfWidth = round(WIDTH_SCREEN / 2)
    bresenhamEllipse(img, (halfWidth, halfHeight), 200, 100, RED)
    bresenhamCircle(img, (halfWidth, halfHeight), 200, RED)
    floodFill(img, (halfWidth, halfHeight + 2), BLACK, BLUE)
    floodFill(img, (halfWidth, round(halfHeight - halfHeight / 2)), BLACK, RED)
    floodFill(img, (halfWidth, round(halfHeight + halfHeight / 2)), BLACK, RED)
    typeWord(img, 'BLOCKS', (math.floor(WIDTH_SCREEN / 2) - 100, math.floor(HEIGHT_SCREEN / 2) + 15), size=2, fontColor=WHITE, letterSpacing=10)

def main():
    #TODO: consertar escala em números racionais

    pygame.init()
    pygame.display.set_caption('AP1')
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
    
    # p = Polygon(img=screen, points=[[70, 70, 0, 0], [120, 70, 1, 0], [120, 120, 1, 1], [70, 120, 0, 1]], borderColor=GRAY, texture=loadTexture('rock_texture.jpg'))

    splashScreen(screen)

    counter_splash = 0

    while True:
        if counter_splash == 10000:
            pass
            cleanScreen(screen)

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
        counter_splash += 1
        pygame.display.update()
     
if __name__=="__main__":
    main()