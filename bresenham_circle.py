from pixel import setPixel

def setPixelsInCircle(img, point, x, y, color):
    xc, yc = point

    setPixel(img, xc + x, yc + y, color)
    setPixel(img, xc - x, yc + y, color)
    setPixel(img, xc + x, yc - y, color)
    setPixel(img, xc - x, yc - y, color)
    setPixel(img, xc + y, yc + x, color)
    setPixel(img, xc - y, yc + x, color)
    setPixel(img, xc + y, yc - x, color)
    setPixel(img, xc - y, yc - x, color)

def bresenhamCircle(img, point, radius, color):
    # TODO: adicionar explicação dos parâmetros de decisão
    x = 0
    y = radius
    p = 3 - 2 * radius

    # pontos iniciais
    setPixelsInCircle(img, point, x, y, color)

    while (y >= x):
        x += 1

        if p > 0:
            y -= 1
            p = p + 4 * (x - y) + 10
        else:
            p = p + 4 * x + 6
        
        setPixelsInCircle(img, point, x, y, color)

