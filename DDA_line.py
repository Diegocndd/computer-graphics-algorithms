from pixel import setPixel

def DDALine(img, start, end, color):
    (xi, yi) = start 
    (xf, yf) = end
    
    dx = xf - xi
    dy = yf - yi

    passos = abs(dx)

    if abs(dy) > abs(dx):
        passos = abs(dy)
    
    if passos == 0:
        setPixel(img, xi, yi, color)
        return

    passosx = dx / passos
    passosy = dy / passos

    for i in range(0, passos):
        x = round(xi + i * passosx)
        y = round(yi + i * passosy)

        setPixel(img, x, y, color)
    
