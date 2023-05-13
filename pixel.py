from pygame import gfxdraw

def getPixel(img, x, y):
    r, g, b, _ = img.get_at((x, y))
    return (r, g, b)

def setPixel(img, x , y, color):
    if x < 0:
        x = 0

    if y < 0:
        y = 0   
 
    gfxdraw.pixel(img, x, y, color)