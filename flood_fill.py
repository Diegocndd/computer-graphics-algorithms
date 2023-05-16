from pixel import getPixel
from pixel import setPixel
from constants import WIDTH_SCREEN, HEIGHT_SCREEN

def isValidPixel(img, pixel, color):
    x, y = pixel

    return x <= WIDTH_SCREEN and y <= HEIGHT_SCREEN and x > 0 and y > 0 and (getPixel(img, x, y) == color)

def floodFill(img, pixel, oldColor, newColor):
    x, y = pixel
    stack = []

    if isValidPixel(img, pixel, oldColor):
        stack.append({'x': x, 'y': y})

        while len(stack) > 0:
            current = stack.pop()

            if current['x'] and current['y']:
                currentX = current['x']
                currentY = current['y']

                setPixel(img, currentX, currentY, newColor)

                if (isValidPixel(img, (currentX, currentY + 1), oldColor)):
                    stack.append({'x': currentX, 'y': currentY + 1})

                if (isValidPixel(img, (currentX + 1, currentY), oldColor)):
                    stack.append({'x': currentX + 1, 'y': currentY})
                    
                if (isValidPixel(img, (currentX - 1, currentY), oldColor)):
                    stack.append({'x': currentX - 1, 'y': currentY})
                    
                if (isValidPixel(img, (currentX, currentY - 1), oldColor)):
                    stack.append({'x': currentX, 'y': currentY - 1})

