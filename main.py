import pygame
import time
from enemy import Enemy
from pixel import setPixel, getPixel
from bresenham_line import bresenhamLine
from bresenham_circle import bresenhamCircle
from bresenham_ellipse import bresenhamEllipse
from utils import loadTexture
from flood_fill import floodFill
from DDA_line import DDALine
from polygon import Polygon
from constants import WIDTH_SCREEN, HEIGHT_SCREEN, ROWS
from word import typeWord
from colors import *
import math

def cleanScreen(img):
    for i in range(0, WIDTH_SCREEN):
        for j in range(0, HEIGHT_SCREEN):
            setPixel(img=img, x=i, y=j, color=BLACK)
            
def generateRow(img, enemiesList, row):
    actualRow = ROWS[row % len(ROWS)]
    for i in actualRow:
        enemiesList.append(
            Enemy(
                img=img,
                points=[[i[0], 4, 0, 0], [i[1], 4, 1, 0], [i[1], 24, 1, 1], [i[0], 24, 0, 1]],
                borderColor=GRAY,
                texture=loadTexture('rock_texture.jpg')
            )
        )

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
    
    p = Polygon(img=screen, points=[[330, 330, 0, 0], [340, 330, 1, 0], [340, 340, 1, 1], [330, 340, 0, 1]], borderColor=BLUE, backgroundColor=BLUE)

    enemies = []

    countToGenerateRow = 0
    row = 0
    c = 0
    count_splash = 0

    splashScreen(screen)

    while True:

        count_splash += 1


        if count_splash == 3000:
            cleanScreen(img=screen)
            p = Polygon(img=screen, points=[[330, 330, 0, 0], [340, 330, 1, 0], [340, 340, 1, 1], [330, 340, 0, 1]], borderColor=BLUE, backgroundColor=BLUE)
        elif count_splash > 3000:
            if countToGenerateRow == 4000:
                countToGenerateRow = 0

            countToGenerateRow += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        p.move(screen, -9, 0)
                    if event.key == pygame.K_RIGHT:
                        p.move(screen, 9, 0)
                    if event.key == pygame.K_UP:
                        p.move(screen, 0, -9)
                    if event.key == pygame.K_DOWN:
                        p.move(screen, 0, 9)

                    # if event.key == pygame.K_SPACE:
                    #     p.scale(screen, 2, 2)
                    # if event.key == pygame.K_a:
                    #     # p.move(screen, -40, -40)

                    #     p.rotate(screen, 20)
            
            if countToGenerateRow == 3999:
                generateRow(screen, enemiesList=enemies, row=row)
                row += 1
            
            for i in enemies:
                i.autoMove(img=screen, velocity=1)

            if c == 6:
                c = 0
                for i in range(0, len(enemies)):
                    r = p.verifyCollision(enemies[i])
                    if r:
                        cleanScreen(screen)
                        enemies = []
            c += 1

        pygame.display.update()
     
if __name__=="__main__":
    main()