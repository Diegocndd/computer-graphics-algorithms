from PIL import Image

"""
    :param      int[][] texture
    :param      int     x
    :param      int     y
    :return:    int     value of the pixel (x,y) in texture matrix
"""
def getPixelFromTexture(texture, x, y):
    if x > 1:
        x = 1
    if x < 0:
        x = 0
    if y > 1:
        y = 1
    if y < 0:
        y = 0
    
    width = 200
    height = 200
    x = round(x * (width - 1) + 1)
    y = round(y * (height - 1) + 1)

    return texture[x, y]

def loadTexture(path):
    im = Image.open(path)
    pixels = im.load()
    return pixels

def oldintersection(scan, seg):
    xi = seg[0][0]
    yi = seg[0][1]
    xf = seg[1][0]
    yf = seg[1][1]
    y = scan

    if yi == yf:
        return -1

    if yi > yf:
        aux = xi
        xi = xf
        xf = aux
        aux = yi
        yi = yf
        yf = aux
    
    t = (y - yi) / (yf - yi)

    if t > 0 and t <= 1:
        return xi + t * (xf - xi)
    
    return -1

def intersection(scan, seg):
    pi = seg[0]
    pf = seg[1]

    y = scan

    if pi[1] == pf[1]:
        return (-1, 0, 0, 0)

    if pi[1] > pf[1]:
        aux = pi
        pi = pf
        pf = aux
    
    t = (y - pi[1]) / (pf[1] - pi[1])

    if t > 0 and t <= 1:
        x = pi[0] + t * (pf[0] - pi[0])

        tx = pi[2] + t * (pf[2] - pi[2])
        ty = pi[3] + t * (pf[3] - pi[3])

        return (round(x), y, tx, ty)
    
    return (-1, 0, 0, 0)

def minMatrix(m):
    minList = []

    for j in range(len(m[0])):
        min = m[0][j]
        for i in range(len(m)):
            if (m[i][j] < min):
                min = m[i][j]
        minList.append(min)
    
    return minList

def maxMatrix(m):
    maxList = []

    for j in range(len(m[0])):
        max = m[0][j]
        for i in range(len(m)):
            if (m[i][j] > max):
                max = m[i][j]
        maxList.append(max)

    return maxList        

def findPivot(m):
    lessX = m[0]

    for i in m:
        if lessX[0] > i[0]:
            lessX = i

    less = []

    for i in m:
        if i[0] == lessX[0]:
            less.append(i)

    lessY = less[0]

    for i in less:
        if lessY[1] > i[1]:
            lessY = i

    return lessY