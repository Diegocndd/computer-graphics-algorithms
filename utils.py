def intersection(scan, seg):
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