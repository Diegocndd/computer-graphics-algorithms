from pixel import setPixel

def bresenhamLine(img, start, end, color):
    (xi, yi) = start
    (xf, yf) = end

    dx = abs(xf - xi)
    dy = abs(yf - yi)
    m = dy/dx
    
    flag = True
    
    step = 1
    if xi > xf or yi > yf:
        step = -1

    mm = False   

    if m < 1:
        xi, xf ,yi ,yf = yi, yf, xi, xf
        dx = abs(xf - xi)
        dy = abs(yf - yi)
        mm = True
        
    p0 = 2*dx - dy
    x = xi
    y = yi
    
    for i in range(abs(yf-yi)):
        if flag:
            x_previous = xi
            p_previous = p0
            p = p0
            flag = False
        else:
            x_previous = x
            p_previous = p
            
        if p >= 0:
            x = x + step

        p = p_previous + 2*dx -2*dy*(abs(x-x_previous))
        y = y + 1
        
        if mm:
            setPixel(img, y, x, color)
        else:
            setPixel(img, x, y, color)