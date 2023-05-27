import math
from pixel import setPixel
from DDA_line import DDALine
from colors import *

def typeWord(img, word, point, size = 1, fontColor = WHITE, letterSpacing=3):
    x, y = point
    actualWidth = 0
    firstLetter = True

    height = math.floor(15 * size)
    width = math.floor(10 * size)

    for letter in word:
        if letter == 'B':
            if not(firstLetter):
                x += actualWidth + letterSpacing
            elif firstLetter:
                actualWidth = width
                x += width
                firstLetter = False


            for i in range(height):
                setPixel(img, x, y - i, fontColor)
            setPixel(img, x + 1, y, fontColor)
            setPixel(img, x + 2, y, fontColor)

            for i in range(1, width - 1):
                setPixel(img, x + i, y, fontColor)

            for i in range(1, width - 1):
                setPixel(img, x + i, y - math.floor(height / 2), fontColor)

            for i in range(1, height):
                if (i != math.floor(height / 2)):
                    setPixel(img, x + (width - 1), y - i, fontColor)

            for i in range(1, width - 1):
                setPixel(img, x + i, y - height, fontColor)
        
        if letter == 'L':
            if not(firstLetter):
                x += actualWidth + letterSpacing
            elif firstLetter:
                actualWidth = width
                x += width
                firstLetter = False

            for i in range(1, width):
                setPixel(img, x + i, y, fontColor)

            for i in range(1, height):
                setPixel(img, x, y - i, fontColor)
        
        if letter == 'O':
            if not(firstLetter):
                x += actualWidth + letterSpacing
            elif firstLetter:
                actualWidth = width
                x += width
                firstLetter = False
            
            for i in range(1, width):
                setPixel(img, x + i, y, fontColor)

            for i in range(1, height):
                setPixel(img, x, y - i, fontColor)                

            for i in range(1, height):
                setPixel(img, x + width, y - i, fontColor)

            for i in range(1, width):
                setPixel(img, x + i, y - height, fontColor)
        
        if letter == 'C':
            if not(firstLetter):
                x += actualWidth + letterSpacing
            elif firstLetter:
                actualWidth = width
                x += width
                firstLetter = False
            
            for i in range(1, width):
                setPixel(img, x + i, y, fontColor)

            for i in range(1, height):
                setPixel(img, x, y - i, fontColor)                

            for i in range(1, width):
                setPixel(img, x + i, y - height, fontColor)

        if letter == 'K':
            if not(firstLetter):
                x += actualWidth + letterSpacing
            elif firstLetter:
                actualWidth = width
                x += width
                firstLetter = False
            
            for i in range(1, height):
                setPixel(img, x, y - i, fontColor)    

            DDALine(img, (x, math.floor(y - height/2)), (x + width, y - height), fontColor)            
            DDALine(img, (x, math.floor(y - height/2)), (x + width, y), fontColor)            

        if letter == 'S':
            if not(firstLetter):
                x += actualWidth + letterSpacing
            elif firstLetter:
                actualWidth = width
                x += width
                firstLetter = False
            
            for i in range(1, width):
                setPixel(img, x + i, y, fontColor)   

            for i in range(1, math.floor(height / 2)):
                setPixel(img, x + width, y - i, fontColor)   

            for i in range(1, width):
                setPixel(img, x + i, y - math.floor(height / 2), fontColor)   

            for i in range(math.floor(height / 2), height):
                setPixel(img, x, y - i, fontColor)   
            
            for i in range(1, width):
                setPixel(img, x + i, y - height, fontColor)   
