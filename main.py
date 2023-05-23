import pygame
import time
from enemy import Enemy
from pixel import setPixel, getPixel
from bresenham_line import bresenhamLine
from bresenham_circle import bresenhamCircle
from bresenham_ellipse import bresenhamEllipse
from flood_fill import floodFill
from polygon import Polygon
from constants import WIDTH_SCREEN, HEIGHT_SCREEN, ROWS
from colors import *

def cleanScreen(img):
    for i in range(0, WIDTH_SCREEN):
        for j in range(0, HEIGHT_SCREEN):
            setPixel(img=img, x=i, y=j, color=BLACK)

def generateRow(img, enemiesList, row):
    actualRow = ROWS[row]
    for i in range(0, len(actualRow)):
        enemiesList.append(Enemy(img=img, points=[[actualRow[i], 4], [actualRow[i] + 10, 4], [actualRow[i] + 10, 14], [actualRow[i], 14]], backgroundColor=RED, borderColor=RED))

def main():
    #TODO: consertar escala em números racionais

    pygame.init()
    pygame.display.set_caption('AP1')
    screen = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))

    enemies = []

    # Polygon(img=screen, points=[[3, 4], [100, 4], [100, 50], [3, 50]], backgroundColor=BLUE, borderColor=BLUE)


    p1 = Polygon(img=screen, points=[[250, 250], [270, 250], [270, 270], [250, 270]], backgroundColor=BLUE, borderColor=BLUE)
    # p2 = Polygon(img=screen, points=[[40, 40], [60, 40], [60, 60], [40, 60]], backgroundColor=RED, borderColor=RED)
    # p3 = Polygon(img=screen, points=[[150, 150], [170, 150], [170, 170], [150, 170]], backgroundColor=GREEN, borderColor=GREEN)

    # enemies.append(p2)
    # enemies.append(p3)
    # generateRow(screen, enemiesList=enemies, row=1)
    countToGenerateRow = 0
    row = 0

    while True:
        if countToGenerateRow == 2000:
            countToGenerateRow = 0

        countToGenerateRow += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    p1.move(screen, -5, 0)
                if event.key == pygame.K_RIGHT:
                    p1.move(screen, 5, 0)
                if event.key == pygame.K_UP:
                    p1.move(screen, 0, -5)
                if event.key == pygame.K_DOWN:
                    p1.move(screen, 0, 5)

                # if event.key == pygame.K_SPACE:
                #     p.scale(screen, 2, 2)
                # if event.key == pygame.K_a:
                #     # p.move(screen, -40, -40)

                #     p.rotate(screen, 20)
        
        if countToGenerateRow == 1999:
            if row < 3:
                # print('gerou')
                generateRow(screen, enemiesList=enemies, row=row)
            row += 1
        
        for i in enemies:
            i.autoMove(img=screen, velocity=1)

        for i in range(0, len(enemies)):
            p1.verifyCollision(enemies[i])

        pygame.display.update()
     
if __name__=="__main__":
    main()