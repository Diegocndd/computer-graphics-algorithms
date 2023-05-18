from pixel import setPixel

def bresenhamLine(img, start, end, color):
    (xi, yi) = start
    (xf, yf) = end

    if abs(xi - yi) >= abs(xf - yf):
        (xi, yi) = end
        (xf, yf) = start

    dx = abs(xf - xi)
    dy = abs(yf - yi)

    if dy == 0:
        step = -1 if xf < xi else 1
        r = range(xf, xi) if xf < xi else range(xi, xf)
        x = xi
        for i in r:
            setPixel(img, x, yi, color)
            x += step
    elif dx == 0:
        step = -1 if yf < yi else 1
        r = range(yf, yi) if yf < yi else range(yi, yf)
        y = yi
        for i in r:
            setPixel(img, xi, y, color)
            y += step
    else:
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

# def bresenhamLine(img, start, end, color):
#     (xi, yi) = start
#     (xf, yf) = end

#     dx = abs(xf - xi)
#     dy = abs(yf - yi)

#     dx2 = 2 * dx
#     dy2 = 2 * dy

#     p = - dx + dy2
#     x = round(xi)
#     y = round(yi)

#     print(dy/dx)

#     for i in range(0, abs(dx)):
#         setPixel(img, y, x, color)

#         x = x + 1

#         if p >= 0:
#             y = y + 1
#             p = p - dx2 + dy2
#         else:
#             p = p + dy2

#     # m = dy/dx
    
#     # flag = True
    
#     # step = 1
#     # if xi > xf or yi > yf:
#     #     step = -1

#     # mm = False   

#     # if m < 1:
#     #     xi, xf ,yi ,yf = yi, yf, xi, xf
#     #     dx = abs(xf - xi)
#     #     dy = abs(yf - yi)
#     #     mm = True
        
#     # p0 = 2*dx - dy
#     # x = xi
#     # y = yi
    
#     # for i in range(abs(yf-yi)):
#     #     if flag:
#     #         x_previous = xi
#     #         p_previous = p0
#     #         p = p0
#     #         flag = False
#     #     else:
#     #         x_previous = x
#     #         p_previous = p
            
#     #     if p >= 0:
#     #         x = x + step

#     #     p = p_previous + 2*dx -2*dy*(abs(x-x_previous))
#     #     y = y + 1
        
#     #     if mm:
#     #         setPixel(img, y, x, color)
#     #     else:
#     #         setPixel(img, x, y, color)