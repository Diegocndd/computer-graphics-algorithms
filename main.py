import pygame
from pixel import setPixel, getPixel
from bresenham_line import bresenhamLine
from bresenham_circle import bresenhamCircle
from colors import YELLOW, ORANGE

def main():
    pygame.init()
    pygame.display.set_caption('Set Pixel')
    screen = pygame.display.set_mode((300,300))

    bresenhamLine(screen, (10, 50), (200, 40), YELLOW)
    bresenhamCircle(screen, (100, 100), 40, YELLOW)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()
     
if __name__=="__main__":
    main()