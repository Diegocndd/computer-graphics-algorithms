from pixel import setPixel

def setPixelsInEllipse(img, point, x, y, color):
  xc, yc = point
  
  setPixel(img, xc + x, yc + y, color)
  setPixel(img, xc + x, yc - y, color)
  setPixel(img, xc - x, yc + y, color)
  setPixel(img, xc - x, yc - y, color)

def bresenhamEllipse(img, point, radius_x, radius_y, color):
  a = radius_x
  b = radius_y
  x = 0
  y = b
  p = 2 * (a ** 2 - b ** 2 * a  + (b ** 2 / 4))
  dx = 2 * b ** 2 * x
  dy = 2 * a ** 2 * y
  
  while dx < dy:
    setPixelsInEllipse(img, point, x, y, color)
    
    if p > 0:
      y -= 1
      dy -= 2 * a ** 2
      p += dx - dy + a ** 2
    else:
      x += 1
      y -= 1
      dx += 2 * b ** 2
      dy -= 2 * a ** 2
